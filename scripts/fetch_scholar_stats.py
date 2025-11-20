"""
更健壮的 Google Scholar 引用数抓取脚本。

优先使用 `google_scholar_crawler.robust_crawler` 中的 requests + BeautifulSoup 实现，
如遇网络问题或无法导入该模块，再降级到 `scholarly`，并为其包裹线程级超时，防止卡死。
"""
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

# 确保可以导入兄弟目录下的 google_scholar_crawler 包
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    # 复用已经写好的健壮实现（带网络重试与模拟数据）
    from google_scholar_crawler import robust_crawler
except Exception as import_error:
    robust_crawler = None  # type: ignore
    ROBUST_ERROR = import_error
else:
    ROBUST_ERROR = None

try:
    from scholarly import scholarly
except Exception as import_error:
    scholarly = None  # type: ignore
    SCHOLARLY_ERROR = import_error
else:
    SCHOLARLY_ERROR = None


class TimeoutException(Exception):
    """线程执行超时"""


def timeout_run(func, args=(), kwargs=None, timeout_duration=30):
    """在线程中运行函数，超时则抛出异常。"""
    if kwargs is None:
        kwargs = {}

    result: list[Any] = [None]
    error: list[Optional[BaseException]] = [None]

    def target():
        try:
            result[0] = func(*args, **kwargs)
        except BaseException as exc:  # 捕获所有异常，在线程外重新抛出
            error[0] = exc

    thread = __import__("threading").Thread(target=target, daemon=True)
    thread.start()
    thread.join(timeout_duration)

    if thread.is_alive():
        raise TimeoutException(f"超时：函数在 {timeout_duration} 秒内未返回")

    if error[0]:
        raise error[0]

    return result[0]


def fetch_via_robust(scholar_id: str) -> Optional[Dict[str, Any]]:
    """调用 robust_crawler，优先使用本地 requests 实现。"""
    if not robust_crawler:
        if ROBUST_ERROR:
            print(f"[INFO] 无法导入 robust_crawler: {ROBUST_ERROR}")
        return None

    try:
        data = robust_crawler.get_scholar_stats(scholar_id, max_retries=2)
        if not data:
            return None
        # 与旧脚本保持兼容，仅保留核心字段
        return {
            "name": data.get("name", "Unknown"),
            "citedby": int(data.get("citedby", 0)),
            "source": data.get("source", "robust_crawler"),
        }
    except Exception as exc:
        print(f"[WARN] robust_crawler 获取失败: {exc}")
        return None


def fetch_via_scholarly(scholar_id: str) -> Optional[Dict[str, Any]]:
    """使用 scholarly 抓取，线程超时保护，避免卡死。"""
    if not scholarly:
        if SCHOLARLY_ERROR:
            print(f"[INFO] 无法导入 scholarly: {SCHOLARLY_ERROR}")
        return None

    def _load_author() -> Dict[str, Any]:
        search_query = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(
            search_query,
            sections=["basics", "indices", "counts"],
        )
        return author

    try:
        author = timeout_run(_load_author, timeout_duration=25)
        return {
            "name": author.get("name", "Unknown"),
            "citedby": int(author.get("citedby", 0)),
            "source": "scholarly",
        }
    except TimeoutException as exc:
        print(f"[WARN] scholarly 调用超时: {exc}")
    except Exception as exc:
        print(f"[WARN] scholarly 获取失败: {exc}")

    return None


def get_scholar_stats(scholar_id: str, retries: int = 3) -> Optional[int]:
    """统一入口，携带重试与多实现降级。"""
    for attempt in range(1, retries + 1):
        print(f"尝试 {attempt}/{retries}: 获取 {scholar_id} 的引用统计...")

        data = fetch_via_robust(scholar_id)
        if not data:
            data = fetch_via_scholarly(scholar_id)

        if data and data.get("citedby") is not None:
            citedby = int(data["citedby"])
            print(f"✓ 成功获取引用数: {citedby} (数据源: {data.get('source')})")
            return citedby

        if attempt < retries:
            wait_time = attempt * 5
            print(f"✗ 获取失败，{wait_time} 秒后重试...")
            time.sleep(wait_time)
        else:
            print("✗ 所有重试均失败")

    return None

def dump_badge(citations: int, output_path: Path) -> None:
    """生成与旧版兼容的 JSON 结构"""
    payload = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations),
        "color": "blue",
        "citedby": citations,
    }
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    scholar_id = "hCvlj5cAAAAJ"

    print("=" * 50)
    print("开始获取 Google Scholar 统计信息...")
    print("=" * 50)

    citations = get_scholar_stats(scholar_id)

    if citations is None:
        print("\n❌ 错误: 无法获取统计信息")
        print("脚本将以错误代码退出")
        sys.exit(1)

    output_file = Path("gs_data.json")
    try:
        dump_badge(citations, output_file)
        print(f"\n✓ 统计信息已成功保存到 {output_file}")
        print(f"✓ 总引用数: {citations}")
        print("=" * 50)

        saved_data = json.loads(output_file.read_text(encoding="utf-8"))
        print(f"✓ 文件验证成功: {saved_data}")
    except Exception as exc:
        print(f"\n❌ 保存文件时出错: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    main()
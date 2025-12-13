#!/usr/bin/env python3
"""
使用 SerpAPI 获取 Google Scholar 统计信息
SerpAPI 提供免费额度（每月100次），非常稳定可靠

功能：
1. 从 SerpAPI 获取真实的 Google Scholar 数据
2. 自动更新保底数据（当成功获取真实数据时）
3. 生成 shields.io 徽章数据

注册获取 API Key: https://serpapi.com/ (免费注册)
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)


# ==================== 保底数据配置 ====================
# 当 SerpAPI 请求失败时使用这些值
FALLBACK_DATA = {
    "name": "Yinda Chen",
    "citedby": 436,      # 保底引用数（会被自动更新）
    "hindex": 9,         # 保底 h-index（会被自动更新）
    "i10index": 9,       # 保底 i10-index（会被自动更新）
    "affiliation": "University of Science and Technology of China",
    "interests": ["Computer Vision", "Self-Supervised Learning", "Multimodal Learning"],
}
# =====================================================


def get_scholar_stats_serpapi(scholar_id: str, api_key: str) -> dict:
    """
    使用 SerpAPI 获取 Google Scholar 统计信息
    """
    print(f"[SerpAPI] 正在获取学者信息: {scholar_id}")
    
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "api_key": api_key,
        "hl": "en"
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # 检查是否有错误
        if "error" in data:
            print(f"[SerpAPI] API 错误: {data['error']}")
            return None
        
        # 提取作者信息
        author = data.get("author", {})
        cited_by = data.get("cited_by", {})
        
        # 获取统计信息
        citations = cited_by.get("table", [])
        citations_all = 0
        citations_5y = 0
        h_index = 0
        h_index_5y = 0
        i10_index = 0
        i10_index_5y = 0
        
        for item in citations:
            if item.get("citations", {}).get("all") is not None:
                citations_all = item["citations"]["all"]
            if item.get("citations", {}).get("since_2020") is not None:
                citations_5y = item["citations"]["since_2020"]
            if item.get("h_index", {}).get("all") is not None:
                h_index = item["h_index"]["all"]
            if item.get("h_index", {}).get("since_2020") is not None:
                h_index_5y = item["h_index"]["since_2020"]
            if item.get("i10_index", {}).get("all") is not None:
                i10_index = item["i10_index"]["all"]
            if item.get("i10_index", {}).get("since_2020") is not None:
                i10_index_5y = item["i10_index"]["since_2020"]
        
        # 获取引用趋势图数据
        cited_by_graph = cited_by.get("graph", [])
        
        author_data = {
            "name": author.get("name", "Unknown"),
            "citedby": citations_all,
            "citedby5y": citations_5y,
            "hindex": h_index,
            "hindex5y": h_index_5y,
            "i10index": i10_index,
            "i10index5y": i10_index_5y,
            "affiliation": author.get("affiliations", ""),
            "interests": [interest.get("title", "") for interest in author.get("interests", [])],
            "thumbnail": author.get("thumbnail", ""),
            "citation_graph": cited_by_graph,  # 引用趋势数据
            "updated": str(datetime.now()),
            "source": "serpapi",
            "publications": {}
        }
        
        print(f"[SerpAPI] 成功获取数据:")
        print(f"  姓名: {author_data['name']}")
        print(f"  总引用数: {author_data['citedby']}")
        print(f"  近5年引用: {author_data['citedby5y']}")
        print(f"  h-index: {author_data['hindex']}")
        print(f"  i10-index: {author_data['i10index']}")
        
        return author_data
        
    except requests.exceptions.RequestException as e:
        print(f"[SerpAPI] 请求失败: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"[SerpAPI] JSON 解析失败: {e}")
        return None
    except Exception as e:
        print(f"[SerpAPI] 未知错误: {e}")
        return None


def update_fallback_in_script(citations: int, hindex: int, i10index: int):
    """
    自动更新本脚本中的保底数据
    当成功获取真实数据时调用此函数
    """
    script_path = Path(__file__)
    
    try:
        content = script_path.read_text(encoding="utf-8")
        
        # 更新 citedby
        content = re.sub(
            r'("citedby":\s*)(\d+)',
            f'\\g<1>{citations}',
            content
        )
        
        # 更新 hindex
        content = re.sub(
            r'("hindex":\s*)(\d+)',
            f'\\g<1>{hindex}',
            content
        )
        
        # 更新 i10index
        content = re.sub(
            r'("i10index":\s*)(\d+)',
            f'\\g<1>{i10index}',
            content
        )
        
        script_path.write_text(content, encoding="utf-8")
        print(f"[自动更新] 已更新保底数据: citations={citations}, h-index={hindex}, i10-index={i10index}")
        
    except Exception as e:
        print(f"[自动更新] 更新保底数据失败: {e}")


def get_fallback_data() -> dict:
    """返回保底数据"""
    print("[Fallback] 使用保底数据...")
    data = FALLBACK_DATA.copy()
    data.update({
        "updated": str(datetime.now()),
        "source": "fallback",
        "publications": {}
    })
    return data


def main():
    """主函数"""
    # 获取环境变量
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "hCvlj5cAAAAJ")
    serpapi_key = os.environ.get("SERPAPI_KEY", "")
    
    print("=" * 60)
    print("Google Scholar 统计信息获取工具 (SerpAPI 版本)")
    print("=" * 60)
    
    author_data = None
    
    # 尝试使用 SerpAPI
    if serpapi_key:
        print("\n[1] 尝试使用 SerpAPI...")
        author_data = get_scholar_stats_serpapi(scholar_id, serpapi_key)
        
        # 如果成功获取，自动更新保底数据
        if author_data and author_data.get("source") == "serpapi":
            update_fallback_in_script(
                author_data["citedby"],
                author_data["hindex"],
                author_data["i10index"]
            )
    else:
        print("\n[WARNING] SERPAPI_KEY 未设置，跳过 SerpAPI")
        print("  请在 GitHub Secrets 中设置 SERPAPI_KEY")
        print("  注册获取免费 API Key: https://serpapi.com/")
    
    # 如果 SerpAPI 失败，使用保底数据
    if not author_data:
        print("\n[2] 使用保底数据...")
        author_data = get_fallback_data()
    
    # 保存结果
    print("\n" + "=" * 60)
    print("保存结果...")
    
    os.makedirs("results", exist_ok=True)
    
    # 保存完整数据
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(author_data, f, ensure_ascii=False, indent=2)
    print("[OK] 完整数据已保存到 results/gs_data.json")
    
    # 保存 shields.io 格式数据 - 引用数
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author_data["citedby"]),
        "color": "blue"
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
    print("[OK] 引用数徽章已保存到 results/gs_data_shieldsio.json")
    
    # 保存 h-index 徽章数据
    hindex_data = {
        "schemaVersion": 1,
        "label": "h-index",
        "message": str(author_data["hindex"]),
        "color": "green"
    }
    with open("results/gs_hindex.json", "w", encoding="utf-8") as f:
        json.dump(hindex_data, f, ensure_ascii=False, indent=2)
    print("[OK] H-Index 徽章已保存到 results/gs_hindex.json")
    
    # 保存 i10-index 徽章数据
    i10index_data = {
        "schemaVersion": 1,
        "label": "i10-index",
        "message": str(author_data["i10index"]),
        "color": "orange"
    }
    with open("results/gs_i10index.json", "w", encoding="utf-8") as f:
        json.dump(i10index_data, f, ensure_ascii=False, indent=2)
    print("[OK] I10-Index 徽章已保存到 results/gs_i10index.json")
    
    # 输出摘要
    print("\n" + "=" * 60)
    print("统计摘要:")
    print(f"  姓名: {author_data['name']}")
    print(f"  引用数: {author_data['citedby']}")
    print(f"  h-index: {author_data['hindex']}")
    print(f"  i10-index: {author_data['i10index']}")
    print(f"  数据源: {author_data['source']}")
    print(f"  更新时间: {author_data['updated']}")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

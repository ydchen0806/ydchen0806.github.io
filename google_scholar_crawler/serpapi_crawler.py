#!/usr/bin/env python3
"""
使用 SerpAPI 获取 Google Scholar 统计信息
SerpAPI 提供免费额度（每月100次），非常稳定可靠

注册获取 API Key: https://serpapi.com/ (免费注册)
"""
import json
import os
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)


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
        h_index = 0
        i10_index = 0
        
        for item in citations:
            if item.get("citations", {}).get("all") is not None:
                citations_all = item["citations"]["all"]
            if item.get("h_index", {}).get("all") is not None:
                h_index = item["h_index"]["all"]
            if item.get("i10_index", {}).get("all") is not None:
                i10_index = item["i10_index"]["all"]
        
        author_data = {
            "name": author.get("name", "Unknown"),
            "citedby": citations_all,
            "hindex": h_index,
            "i10index": i10_index,
            "affiliation": author.get("affiliations", ""),
            "interests": [interest.get("title", "") for interest in author.get("interests", [])],
            "thumbnail": author.get("thumbnail", ""),
            "updated": str(datetime.now()),
            "source": "serpapi",
            "publications": {}
        }
        
        print(f"[SerpAPI] 成功获取数据:")
        print(f"  姓名: {author_data['name']}")
        print(f"  引用数: {author_data['citedby']}")
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


def get_fallback_data(scholar_id: str) -> dict:
    """保底数据"""
    print("[Fallback] 使用保底数据...")
    return {
        "name": "Yinda Chen",
        "citedby": 436,  # 保底引用数
        "hindex": 9,
        "i10index": 9,
        "affiliation": "University of Science and Technology of China",
        "interests": ["Computer Vision", "Self-Supervised Learning", "Multimodal Learning"],
        "updated": str(datetime.now()),
        "source": "fallback",
        "publications": {}
    }


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
    else:
        print("\n[WARNING] SERPAPI_KEY 未设置，跳过 SerpAPI")
        print("  请在 GitHub Secrets 中设置 SERPAPI_KEY")
        print("  注册获取免费 API Key: https://serpapi.com/")
    
    # 如果 SerpAPI 失败，使用保底数据
    if not author_data:
        print("\n[2] 使用保底数据...")
        author_data = get_fallback_data(scholar_id)
    
    # 保存结果
    print("\n" + "=" * 60)
    print("保存结果...")
    
    os.makedirs("results", exist_ok=True)
    
    # 保存完整数据
    with open("results/gs_data.json", "w", encoding="utf-8") as f:
        json.dump(author_data, f, ensure_ascii=False, indent=2)
    print("[OK] 完整数据已保存到 results/gs_data.json")
    
    # 保存 shields.io 格式数据
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author_data["citedby"]),
        "color": "blue"
    }
    
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
        json.dump(shieldio_data, f, ensure_ascii=False, indent=2)
    print("[OK] Shields.io 数据已保存到 results/gs_data_shieldsio.json")
    
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


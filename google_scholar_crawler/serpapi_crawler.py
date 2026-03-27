#!/usr/bin/env python3
"""
使用 SerpAPI 获取 Google Scholar 统计信息
SerpAPI 提供免费额度（每月100次），非常稳定可靠

功能：
1. 从 SerpAPI 获取真实的 Google Scholar 数据
2. 自动更新保底数据（当成功获取真实数据时）
3. 生成 shields.io 徽章数据
4. 生成引用趋势 SVG 图
5. 获取一作论文列表及其引用数
6. 筛选高引用论文（>50）生成徽章数据
7. 筛选符合条件的一作论文，提取研究方向关键词

注册获取 API Key: https://serpapi.com/ (免费注册)
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from collections import Counter

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)

# 导入会议/期刊等级配置
try:
    from venue_config import is_qualified_venue, get_venue_level
except ImportError:
    # 如果无法导入，定义简单版本
    def is_qualified_venue(venue_name):
        qualified = ['AAAI', 'NeurIPS', 'ICML', 'ICLR', 'CVPR', 'ICCV', 'ECCV', 
                     'ACL', 'EMNLP', 'IJCAI', 'MICCAI', 'TMI', 'TPAMI', 'TIP',
                     'TCSVT', 'JBHI', 'Medical Image Analysis']
        return any(q.upper() in venue_name.upper() for q in qualified)
    def get_venue_level(venue_name):
        return (None, None)


# ==================== 保底数据配置 ====================
# 当 SerpAPI 请求失败时使用这些值
FALLBACK_DATA = {
    "name": "Yinda Chen",
    "citedby": 567,      # 保底引用数（会被自动更新，仅当新值 > 0）
    "hindex": 12,         # 保底 h-index（会被自动更新，仅当新值 > 0）
    "i10index": 13,       # 保底 i10-index（会被自动更新，仅当新值 > 0）
    "affiliation": "University of Science and Technology of China",
    "interests": ["Computer Vision", "Self-Supervised Learning", "Multimodal Learning"],
}

# 作者姓名变体（用于匹配一作）
AUTHOR_NAME_VARIANTS = [
    "Yinda Chen",
    "Y Chen",
    "YD Chen",
    "陈胤达",
]
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
        
        # 获取统计信息 - 兼容 SerpAPI 不同语言/版本的 key 名称
        table = cited_by.get("table", [])
        citations_all = 0
        citations_5y = 0
        h_index = 0
        h_index_5y = 0
        i10_index = 0
        i10_index_5y = 0
        
        print(f"[SerpAPI] cited_by.table 原始数据: {json.dumps(table, ensure_ascii=False)}")
        
        def extract_all_and_recent(item_dict):
            """从 table 条目中提取 all 和 recent 值，兼容不同语言的 key"""
            val_all, val_recent = 0, 0
            for key, sub in item_dict.items():
                if isinstance(sub, dict):
                    if "all" in sub:
                        val_all = sub["all"]
                    for sk, sv in sub.items():
                        if sk != "all" and isinstance(sv, int):
                            val_recent = sv
            return val_all, val_recent
        
        # table[0] = citations, table[1] = h_index, table[2] = i10_index
        if len(table) >= 1:
            citations_all, citations_5y = extract_all_and_recent(table[0])
        if len(table) >= 2:
            h_index, h_index_5y = extract_all_and_recent(table[1])
        if len(table) >= 3:
            i10_index, i10_index_5y = extract_all_and_recent(table[2])
        
        # 从引用趋势图获取补充数据
        cited_by_graph = cited_by.get("graph", [])
        
        # 安全检查：如果 table 解析失败（citedby=0），尝试从 graph 数据求和
        if citations_all == 0 and cited_by_graph:
            graph_total = sum(
                int(item.get("citations", 0)) for item in cited_by_graph
            )
            if graph_total > 0:
                citations_all = graph_total
                print(f"[SerpAPI] table 解析为 0，从 citation_graph 求和得 {graph_total}")
        
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
            "citation_graph": cited_by_graph,
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


def get_articles_serpapi(scholar_id: str, api_key: str, num_articles: int = 100) -> list:
    """
    获取作者的论文列表
    """
    print(f"[SerpAPI] 正在获取论文列表...")
    
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "api_key": api_key,
        "hl": "en",
        "num": num_articles,
        "sort": "cited"  # 按引用数排序
    }
    
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            print(f"[SerpAPI] API 错误: {data['error']}")
            return []
        
        articles = data.get("articles", [])
        print(f"[SerpAPI] 获取到 {len(articles)} 篇论文")
        return articles
        
    except Exception as e:
        print(f"[SerpAPI] 获取论文失败: {e}")
        return []


def is_first_author(authors_str: str, name_variants: list) -> bool:
    """
    判断是否为一作（包括共同一作）
    """
    if not authors_str:
        return False
    
    # 获取第一作者（逗号分隔的第一个）
    first_author = authors_str.split(",")[0].strip()
    
    # 检查是否包含任何姓名变体
    for variant in name_variants:
        if variant.lower() in first_author.lower():
            return True
        # 也检查整个作者列表中是否有标注共同一作（*）
        if f"{variant}*" in authors_str or f"*{variant}" in authors_str:
            return True
    
    return False


def filter_first_author_papers(articles: list, name_variants: list) -> list:
    """
    筛选一作论文
    """
    first_author_papers = []
    
    for article in articles:
        authors = article.get("authors", "")
        title = article.get("title", "")
        
        if is_first_author(authors, name_variants):
            first_author_papers.append({
                "title": title,
                "authors": authors,
                "year": article.get("year", ""),
                "citations": article.get("cited_by", {}).get("value", 0),
                "link": article.get("link", ""),
                "citation_id": article.get("citation_id", "")
            })
    
    print(f"[筛选] 找到 {len(first_author_papers)} 篇一作论文")
    return first_author_papers


def extract_research_keywords(title: str) -> list:
    """
    从论文标题中提取研究方向关键词
    """
    # 关键词映射表
    keyword_patterns = {
        'Multimodal Learning': ['multimodal', 'multi-modal', 'vision-language', 'cross-modal'],
        'Self-Supervised Learning': ['self-supervised', 'self supervised', 'pretraining', 'pretrain', 'contrastive'],
        'Computer Vision': ['vision', 'visual', 'image segmentation', 'object detection', 'semantic'],
        'Image Compression': ['compression', 'coding', 'latent', 'entropy'],
        'Domain Adaptation': ['domain adaptation', 'unsupervised domain', 'transfer learning'],
        'Medical Imaging': ['medical', 'clinical', 'biomedical', 'health', 'CT', 'MRI', 'X-ray'],
        'Deep Learning': ['deep learning', 'neural network', 'transformer', 'attention'],
        'Generative Models': ['generative', 'generation', 'diffusion', 'GAN', 'VAE'],
        'Reinforcement Learning': ['reinforcement', 'RL', 'policy', 'reward'],
        'Natural Language Processing': ['language', 'NLP', 'text', 'speech', 'TTS'],
        'Representation Learning': ['representation', 'embedding', 'feature learning'],
        'Data-Centric AI': ['synthetic data', 'data generation', 'dataset', 'annotation'],
        'Embodied AI': ['embodied', 'robot', 'humanoid', 'manipulation'],
        '3D Vision': ['3D', 'point cloud', 'depth', 'volumetric', 'NeRF'],
    }
    
    title_lower = title.lower()
    found_keywords = []
    
    for keyword, patterns in keyword_patterns.items():
        for pattern in patterns:
            if pattern.lower() in title_lower:
                found_keywords.append(keyword)
                break
    
    return found_keywords


def filter_qualified_papers(papers: list, years_limit: int = 3) -> list:
    """
    筛选符合条件的论文：
    - 3年内
    - CCF B及以上 或 SCI 二区及以上
    """
    current_year = datetime.now().year
    min_year = current_year - years_limit
    
    qualified = []
    for paper in papers:
        year = paper.get('year', '')
        try:
            paper_year = int(year) if year else 0
        except ValueError:
            paper_year = 0
        
        # 检查年份
        if paper_year < min_year:
            continue
        
        # 从标题或其他信息推断会议/期刊
        # 注意：SerpAPI 返回的数据可能没有会议名称，需要从 pub.md 匹配
        title = paper.get('title', '')
        
        # 暂时保留所有近3年的论文，后续可以通过标题匹配 pub.md 来过滤
        paper['keywords'] = extract_research_keywords(title)
        qualified.append(paper)
    
    return qualified


def generate_research_keywords_json(papers: list, output_path: str):
    """
    从论文标题生成研究方向关键词 JSON
    """
    all_keywords = []
    
    for paper in papers:
        keywords = paper.get('keywords', [])
        if not keywords:
            keywords = extract_research_keywords(paper.get('title', ''))
        all_keywords.extend(keywords)
    
    # 统计关键词频率
    keyword_counts = Counter(all_keywords)
    
    # 转换为权重（1-5）
    max_count = max(keyword_counts.values()) if keyword_counts else 1
    
    keywords_data = []
    for keyword, count in keyword_counts.most_common(12):  # 取前12个
        weight = max(2, min(5, round((count / max_count) * 5)))
        keywords_data.append({
            'keyword': keyword,
            'count': count,
            'weight': weight
        })
    
    # 保存 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(keywords_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] 研究方向关键词已保存到 {output_path}")
    return keywords_data


def filter_high_cited_papers(papers: list, min_citations: int = 50) -> list:
    """
    筛选高引用论文（>= min_citations）
    """
    high_cited = []
    for paper in papers:
        citations = paper.get('citations', 0)
        if citations >= min_citations:
            high_cited.append(paper)
    
    # 按引用数降序排列
    high_cited.sort(key=lambda x: x.get('citations', 0), reverse=True)
    
    print(f"[筛选] 找到 {len(high_cited)} 篇高引用论文 (>={min_citations})")
    return high_cited


def generate_citation_trend_svg(citation_graph: list, output_path: str, total_citations: int = None):
    """
    生成引用趋势 SVG 图（显示累计引用数）
    
    Args:
        citation_graph: SerpAPI 返回的每年引用数据
        output_path: 输出文件路径
        total_citations: 真实的总引用数（用于校准）
    """
    if not citation_graph:
        print("[SVG] 没有引用趋势数据")
        return
    
    # 提取年份和每年新增引用数
    years = [item.get("year", 0) for item in citation_graph]
    yearly_citations = [item.get("citations", 0) for item in citation_graph]
    
    if not years or not yearly_citations:
        return
    
    # 计算累计引用数
    cumulative_citations = []
    running_total = 0
    for cite in yearly_citations:
        running_total += cite
        cumulative_citations.append(running_total)
    
    # 如果提供了真实总引用数，校准最后一年的值
    if total_citations and cumulative_citations:
        # 计算差值，分配到各年（假设早期数据缺失）
        diff = total_citations - cumulative_citations[-1]
        if diff > 0:
            # 将差值加到第一年之前（作为基础值）
            cumulative_citations = [c + diff for c in cumulative_citations]
            print(f"[SVG] 校准累计引用数: {cumulative_citations[-1] - diff} → {total_citations}")
    
    # SVG 尺寸（加宽以显示更多标签）
    width = 700
    height = 250
    padding_left = 60
    padding_right = 50
    padding_top = 50
    padding_bottom = 50
    chart_width = width - padding_left - padding_right
    chart_height = height - padding_top - padding_bottom
    
    # 计算比例
    max_citations = max(cumulative_citations) if cumulative_citations else 1
    x_step = chart_width / (len(years) - 1) if len(years) > 1 else chart_width
    y_scale = chart_height / max_citations if max_citations > 0 else 1
    
    # 生成折线点
    points = []
    for i, (year, cite) in enumerate(zip(years, cumulative_citations)):
        x = padding_left + i * x_step
        y = height - padding_bottom - cite * y_scale
        points.append(f"{x},{y}")
    
    polyline_points = " ".join(points)
    
    # 生成 SVG
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#4285f4;stop-opacity:0.6" />
      <stop offset="100%" style="stop-color:#4285f4;stop-opacity:0.05" />
    </linearGradient>
  </defs>
  
  <!-- 背景 -->
  <rect width="{width}" height="{height}" fill="#fafafa" rx="10"/>
  
  <!-- 标题 -->
  <text x="{width/2}" y="30" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#333">
    📈 Cumulative Citations (Total: {cumulative_citations[-1]})
  </text>
  
  <!-- Y轴标签 -->
  <g font-family="Arial, sans-serif" font-size="10" fill="#888">
'''
    
    # Y轴刻度标签
    for i in range(5):
        y_pos = padding_top + i * chart_height / 4
        y_val = int(max_citations * (4 - i) / 4)
        svg += f'    <text x="{padding_left - 10}" y="{y_pos + 4}" text-anchor="end">{y_val}</text>\n'
        svg += f'    <line x1="{padding_left}" y1="{y_pos}" x2="{width - padding_right}" y2="{y_pos}" stroke="#e0e0e0" stroke-width="1"/>\n'
    
    svg += '  </g>\n\n'
    
    # 添加填充区域
    first_x = padding_left
    last_x = padding_left + (len(years) - 1) * x_step
    fill_points = f"{first_x},{height-padding_bottom} " + polyline_points + f" {last_x},{height-padding_bottom}"
    svg += f'  <!-- 填充区域 -->\n'
    svg += f'  <polygon points="{fill_points}" fill="url(#gradient)"/>\n\n'
    
    # 添加折线
    svg += f'  <!-- 折线 -->\n'
    svg += f'  <polyline points="{polyline_points}" fill="none" stroke="#4285f4" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>\n\n'
    
    # 添加数据点和标签
    svg += '  <!-- 数据点和标签 -->\n'
    for i, (year, cite) in enumerate(zip(years, cumulative_citations)):
        x = padding_left + i * x_step
        y = height - padding_bottom - cite * y_scale
        
        # 数据点
        svg += f'  <circle cx="{x}" cy="{y}" r="5" fill="#4285f4" stroke="#fff" stroke-width="2"/>\n'
        
        # 年份标签（X轴）
        if len(years) <= 12 or i % 2 == 0 or i == len(years) - 1:
            svg += f'  <text x="{x}" y="{height-padding_bottom+18}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="#666">{year}</text>\n'
        
        # 每年都标注累计引用数（调整位置避免重叠）
        # 奇数年份标签在上方，偶数年份标签在下方数据点旁边
        if i % 2 == 0:
            label_y = y - 12 if y > padding_top + 30 else y + 20
        else:
            label_y = y + 18 if y < height - padding_bottom - 30 else y - 12
        
        svg += f'  <text x="{x}" y="{label_y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" font-weight="bold" fill="#4285f4">{cite}</text>\n'
    
    svg += '</svg>'
    
    # 保存文件
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    
    print(f"[SVG] 引用趋势图已保存到 {output_path}")


def update_fallback_in_script(citations: int, hindex: int, i10index: int):
    """
    自动更新本脚本中的保底数据
    只在获取到有效数据（> 0）时调用
    """
    if citations <= 0:
        print(f"[自动更新] 跳过：citations={citations} 无效，不覆盖保底数据")
        return
    
    script_path = Path(__file__)
    
    try:
        content = script_path.read_text(encoding="utf-8")
        
        content = re.sub(
            r'("citedby":\s*)(\d+)',
            f'\\g<1>{citations}',
            content
        )
        
        content = re.sub(
            r'("hindex":\s*)(\d+)',
            f'\\g<1>{hindex}',
            content
        )
        
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
    first_author_papers = []
    
    # 尝试使用 SerpAPI
    if serpapi_key:
        print("\n[1] 尝试使用 SerpAPI...")
        author_data = get_scholar_stats_serpapi(scholar_id, serpapi_key)
        
        if author_data and author_data.get("source") == "serpapi":
            # 获取论文列表
            print("\n[2] 获取论文列表...")
            articles = get_articles_serpapi(scholar_id, serpapi_key)
            
            # 筛选一作论文
            if articles:
                first_author_papers = filter_first_author_papers(articles, AUTHOR_NAME_VARIANTS)
                author_data["first_author_papers"] = first_author_papers
            
            # 安全检查：如果总引用数为 0 但论文有引用，用所有论文引用数之和作为下限
            if author_data["citedby"] == 0 and articles:
                total_from_papers = sum(
                    a.get("cited_by", {}).get("value", 0) if isinstance(a.get("cited_by"), dict)
                    else 0
                    for a in articles
                )
                if total_from_papers > 0:
                    print(f"[安全检查] citedby=0 异常！从 {len(articles)} 篇论文求和得 {total_from_papers}")
                    author_data["citedby"] = total_from_papers
            
            # 最终防线：如果 citedby 仍为 0，使用保底数据的值
            if author_data["citedby"] == 0 and FALLBACK_DATA["citedby"] > 0:
                print(f"[安全检查] citedby 仍为 0，使用保底值 {FALLBACK_DATA['citedby']}")
                author_data["citedby"] = FALLBACK_DATA["citedby"]
                author_data["hindex"] = FALLBACK_DATA["hindex"]
                author_data["i10index"] = FALLBACK_DATA["i10index"]
            
            # 只有当引用数 > 0 时才更新保底数据，防止写入 0
            if author_data["citedby"] > 0:
                update_fallback_in_script(
                    author_data["citedby"],
                    author_data["hindex"],
                    author_data["i10index"]
                )
            else:
                print("[WARNING] citedby 为 0，跳过保底数据更新以防止覆盖")
    else:
        print("\n[WARNING] SERPAPI_KEY 未设置，跳过 SerpAPI")
        print("  请在 GitHub Secrets 中设置 SERPAPI_KEY")
        print("  注册获取免费 API Key: https://serpapi.com/")
    
    # 如果 SerpAPI 失败，使用保底数据
    if not author_data:
        print("\n[3] 使用保底数据...")
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
    
    # 生成引用趋势 SVG（传入真实总引用数进行校准）
    if author_data.get("citation_graph"):
        generate_citation_trend_svg(
            author_data["citation_graph"],
            "results/citation_trend.svg",
            total_citations=author_data.get("citedby", 0)
        )
    
    # 保存一作论文列表
    if first_author_papers:
        with open("results/first_author_papers.json", "w", encoding="utf-8") as f:
            json.dump(first_author_papers, f, ensure_ascii=False, indent=2)
        print(f"[OK] 一作论文列表已保存到 results/first_author_papers.json ({len(first_author_papers)} 篇)")
        
        # 筛选高引用论文 (>=50)
        high_cited_papers = filter_high_cited_papers(first_author_papers, min_citations=50)
        if high_cited_papers:
            with open("results/high_cited_papers.json", "w", encoding="utf-8") as f:
                json.dump(high_cited_papers, f, ensure_ascii=False, indent=2)
            print(f"[OK] 高引用论文已保存到 results/high_cited_papers.json ({len(high_cited_papers)} 篇)")
        
        # 筛选近3年符合条件的论文
        qualified_papers = filter_qualified_papers(first_author_papers, years_limit=3)
        if qualified_papers:
            with open("results/qualified_papers.json", "w", encoding="utf-8") as f:
                json.dump(qualified_papers, f, ensure_ascii=False, indent=2)
            print(f"[OK] 符合条件的论文已保存到 results/qualified_papers.json ({len(qualified_papers)} 篇)")
            
            # 生成研究方向关键词
            generate_research_keywords_json(qualified_papers, "results/research_keywords.json")
        
        # 打印一作论文摘要
        print("\n一作论文列表:")
        for i, paper in enumerate(first_author_papers[:10], 1):  # 只显示前10篇
            print(f"  {i}. [{paper['citations']} 引用] {paper['title'][:60]}...")
    
    # 输出摘要
    print("\n" + "=" * 60)
    print("统计摘要:")
    print(f"  姓名: {author_data['name']}")
    print(f"  引用数: {author_data['citedby']}")
    print(f"  h-index: {author_data['hindex']}")
    print(f"  i10-index: {author_data['i10index']}")
    print(f"  一作论文数: {len(first_author_papers)}")
    print(f"  数据源: {author_data['source']}")
    print(f"  更新时间: {author_data['updated']}")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

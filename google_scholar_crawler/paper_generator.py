#!/usr/bin/env python3
"""
论文信息自动生成器
从 Google Scholar 获取论文信息，生成 pub.md 格式的内容

功能：
1. 获取一作/共一论文的详细信息
2. 自动识别会议/期刊等级（CCF 分区、SCI 分区）
3. 筛选高引用论文（>=50）
4. 生成 Markdown 格式的论文列表
"""
import json
import os
import re
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)

from venue_config import CCF_VENUES, SCI_JOURNALS, get_venue_level, is_qualified_venue


# 作者姓名变体
AUTHOR_NAME_VARIANTS = [
    "Yinda Chen",
    "Y Chen",
    "YD Chen",
    "陈胤达",
]

# 会议/期刊简称映射
VENUE_SHORTCUTS = {
    # CCF A 会议
    "AAAI": {"full": "AAAI Conference on Artificial Intelligence", "type": "conference", "ccf": "A"},
    "NeurIPS": {"full": "Neural Information Processing Systems", "type": "conference", "ccf": "A"},
    "NIPS": {"full": "Neural Information Processing Systems", "type": "conference", "ccf": "A"},
    "ICML": {"full": "International Conference on Machine Learning", "type": "conference", "ccf": "A"},
    "ICLR": {"full": "International Conference on Learning Representations", "type": "conference", "ccf": "A"},
    "CVPR": {"full": "IEEE/CVF Conference on Computer Vision and Pattern Recognition", "type": "conference", "ccf": "A"},
    "ICCV": {"full": "IEEE/CVF International Conference on Computer Vision", "type": "conference", "ccf": "A"},
    "ECCV": {"full": "European Conference on Computer Vision", "type": "conference", "ccf": "A"},
    "ACL": {"full": "Annual Meeting of the Association for Computational Linguistics", "type": "conference", "ccf": "A"},
    "IJCAI": {"full": "International Joint Conference on Artificial Intelligence", "type": "conference", "ccf": "A"},
    
    # CCF B 会议
    "MICCAI": {"full": "Medical Image Computing and Computer Assisted Intervention", "type": "conference", "ccf": "B"},
    "WACV": {"full": "IEEE/CVF Winter Conference on Applications of Computer Vision", "type": "conference", "ccf": "B"},
    "ACCV": {"full": "Asian Conference on Computer Vision", "type": "conference", "ccf": "B"},
    "ICASSP": {"full": "IEEE International Conference on Acoustics, Speech and Signal Processing", "type": "conference", "ccf": "B"},
    
    # Q1 期刊
    "TPAMI": {"full": "IEEE Transactions on Pattern Analysis and Machine Intelligence", "type": "journal", "sci": "Q1", "if": 23.6},
    "IJCV": {"full": "International Journal of Computer Vision", "type": "journal", "sci": "Q1", "if": 19.5},
    "TIP": {"full": "IEEE Transactions on Image Processing", "type": "journal", "sci": "Q1", "if": 10.6},
    "TMI": {"full": "IEEE Transactions on Medical Imaging", "type": "journal", "sci": "Q1", "if": 10.6},
    "TCSVT": {"full": "IEEE Transactions on Circuits and Systems for Video Technology", "type": "journal", "sci": "Q1", "if": 8.4},
    "MIA": {"full": "Medical Image Analysis", "type": "journal", "sci": "Q1", "if": 10.9},
    "TNNLS": {"full": "IEEE Transactions on Neural Networks and Learning Systems", "type": "journal", "sci": "Q1", "if": 10.4},
    
    # Q2 期刊
    "JBHI": {"full": "IEEE Journal of Biomedical and Health Informatics", "type": "journal", "sci": "Q2", "if": 7.7},
    "PR": {"full": "Pattern Recognition", "type": "journal", "sci": "Q1", "if": 8.0},
    "NEUCOM": {"full": "Neurocomputing", "type": "journal", "sci": "Q2", "if": 6.0},
}


def detect_venue_from_text(text: str) -> dict:
    """
    从文本中检测会议/期刊信息
    """
    text_upper = text.upper()
    
    for shortcut, info in VENUE_SHORTCUTS.items():
        if shortcut.upper() in text_upper:
            return {
                "shortcut": shortcut,
                "full_name": info["full"],
                "type": info["type"],
                "ccf": info.get("ccf"),
                "sci": info.get("sci"),
                "impact_factor": info.get("if")
            }
    
    return None


def is_first_author(authors_str: str) -> bool:
    """
    判断是否为一作（包括共同一作）
    """
    if not authors_str:
        return False
    
    # 获取前两个作者
    authors = [a.strip() for a in authors_str.split(",")[:2]]
    
    for author in authors:
        for variant in AUTHOR_NAME_VARIANTS:
            if variant.lower() in author.lower():
                return True
            # 检查共同一作标记
            if f"{variant}*" in authors_str or f"*{variant}" in authors_str:
                return True
    
    return False


def get_author_articles(scholar_id: str, api_key: str, num: int = 100) -> list:
    """
    获取作者的论文列表（包含详细信息）
    """
    print(f"[SerpAPI] 正在获取论文列表...")
    
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_scholar_author",
        "author_id": scholar_id,
        "api_key": api_key,
        "hl": "en",
        "num": num,
        "sort": "pubdate"  # 按发表时间排序
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


def process_papers(articles: list) -> list:
    """
    处理论文列表，提取详细信息
    """
    processed = []
    current_year = datetime.now().year
    
    for article in articles:
        title = article.get("title", "")
        authors = article.get("authors", "")
        year = article.get("year", "")
        cited_by = article.get("cited_by")
        if isinstance(cited_by, dict):
            _v = cited_by.get("value")
            try:
                citations = int(_v) if _v is not None else 0
            except (TypeError, ValueError):
                citations = 0
        else:
            citations = 0
        link = article.get("link", "")
        
        # 判断是否为一作
        first_author = is_first_author(authors)
        
        # 检测会议/期刊
        venue_info = detect_venue_from_text(title + " " + str(article))
        
        # 计算年份
        try:
            paper_year = int(year) if year else 0
        except ValueError:
            paper_year = 0
        
        # 判断是否符合条件
        is_high_cited = citations >= 50
        is_recent = paper_year >= current_year - 3
        is_qualified_ccf = venue_info and venue_info.get("ccf") in ["A", "B"]
        is_qualified_sci = venue_info and venue_info.get("sci") in ["Q1", "Q2"]
        
        paper_data = {
            "title": title,
            "authors": authors,
            "year": year,
            "citations": citations,
            "link": link,
            "is_first_author": first_author,
            "venue": venue_info,
            "is_high_cited": is_high_cited,
            "is_recent": is_recent,
            "is_qualified": is_qualified_ccf or is_qualified_sci,
            "should_include": first_author and (is_high_cited or (is_recent and (is_qualified_ccf or is_qualified_sci)))
        }
        
        processed.append(paper_data)
    
    return processed


def generate_paper_markdown(paper: dict) -> str:
    """
    生成单篇论文的 Markdown 格式
    """
    title = paper["title"]
    authors = paper["authors"]
    year = paper["year"]
    citations = paper["citations"]
    link = paper["link"]
    venue = paper.get("venue", {})
    
    # 生成会议/期刊徽章
    venue_badge = ""
    ccf_badge = ""
    
    if venue:
        shortcut = venue.get("shortcut", "")
        venue_type = venue.get("type", "")
        
        if venue_type == "conference":
            venue_badge = f'<div class="badge-conference">{shortcut} {year}</div>'
            if venue.get("ccf"):
                ccf_badge = f'<div class="badge-ccf badge-ccf-{venue["ccf"].lower()}">CCF {venue["ccf"]}</div>'
        else:
            venue_badge = f'<div class="badge-journal">{shortcut}</div>'
            if venue.get("sci"):
                impact = venue.get("impact_factor", "")
                if_text = f" | IF: {impact}" if impact else ""
                ccf_badge = f'<div class="badge-impact badge-q1">SCI {venue["sci"]}{if_text}</div>'
    
    # 生成高引用徽章
    citation_badge = ""
    if citations >= 50:
        citation_badge = f' <span class="citation-badge">{citations} citations</span>'
    
    # 格式化作者（高亮自己）
    formatted_authors = authors
    for variant in AUTHOR_NAME_VARIANTS:
        formatted_authors = formatted_authors.replace(variant, f"**{variant}**")
    
    # 生成 Markdown
    md = f"""<div class='paper-box'><div class='paper-box-image'><div>{venue_badge}{ccf_badge}<img src='images/placeholder.png' alt="paper" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[{title}]({link}){citation_badge} \\\\
{venue.get('shortcut', 'Publication')} | {year} \\\\
{formatted_authors}

<!-- TODO: Add paper description -->

</div>
</div>
"""
    return md


def generate_papers_json(papers: list, output_path: str):
    """
    保存论文数据为 JSON
    """
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"[OK] 论文数据已保存到 {output_path}")


def generate_papers_markdown(papers: list, output_path: str):
    """
    生成论文 Markdown 文件
    """
    # 筛选应该包含的论文
    included_papers = [p for p in papers if p["should_include"]]
    
    # 按年份和引用数排序
    included_papers.sort(key=lambda x: (-int(x.get("year", 0) or 0), -x.get("citations", 0)))
    
    # 分类：期刊和会议
    journal_papers = [p for p in included_papers if p.get("venue", {}).get("type") == "journal"]
    conference_papers = [p for p in included_papers if p.get("venue", {}).get("type") == "conference"]
    other_papers = [p for p in included_papers if not p.get("venue")]
    
    # 生成 Markdown
    md_content = """# 📝 Auto-Generated Publications

> This file is auto-generated from Google Scholar data.
> Papers included: First-author papers with CCF B+/SCI Q2+ or 50+ citations.

---

"""
    
    if journal_papers:
        md_content += "## 📰 Journal Articles\n\n"
        for paper in journal_papers:
            md_content += generate_paper_markdown(paper) + "\n"
    
    if conference_papers:
        md_content += "## 🎓 Conference Papers\n\n"
        for paper in conference_papers:
            md_content += generate_paper_markdown(paper) + "\n"
    
    if other_papers:
        md_content += "## 📄 Other Publications\n\n"
        for paper in other_papers:
            md_content += generate_paper_markdown(paper) + "\n"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"[OK] Markdown 文件已保存到 {output_path}")
    print(f"     包含 {len(included_papers)} 篇论文 ({len(journal_papers)} 期刊, {len(conference_papers)} 会议)")


def main():
    """主函数"""
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "hCvlj5cAAAAJ")
    serpapi_key = os.environ.get("SERPAPI_KEY", "")
    
    if not serpapi_key:
        print("[ERROR] SERPAPI_KEY 未设置")
        return 1
    
    print("=" * 60)
    print("论文信息自动生成器")
    print("=" * 60)
    
    # 获取论文列表
    articles = get_author_articles(scholar_id, serpapi_key)
    
    if not articles:
        print("[ERROR] 无法获取论文列表")
        return 1
    
    # 处理论文
    processed_papers = process_papers(articles)
    
    # 创建输出目录
    os.makedirs("results", exist_ok=True)
    
    # 保存 JSON
    generate_papers_json(processed_papers, "results/all_papers.json")
    
    # 筛选符合条件的论文
    qualified = [p for p in processed_papers if p["should_include"]]
    generate_papers_json(qualified, "results/qualified_papers_detail.json")
    
    # 生成 Markdown
    generate_papers_markdown(processed_papers, "results/auto_publications.md")
    
    # 输出摘要
    print("\n" + "=" * 60)
    print("统计摘要:")
    print(f"  总论文数: {len(processed_papers)}")
    print(f"  一作论文数: {len([p for p in processed_papers if p['is_first_author']])}")
    print(f"  高引用论文 (>=50): {len([p for p in processed_papers if p['is_high_cited']])}")
    print(f"  符合条件的论文: {len(qualified)}")
    print("=" * 60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())


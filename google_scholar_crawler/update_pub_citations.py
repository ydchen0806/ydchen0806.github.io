#!/usr/bin/env python3
"""
自动更新 pub.md 中 shields.io 引用徽章的数字
从 first_author_papers.json 读取最新引用数，更新 pub.md 中的硬编码值
"""

import json
import re
import os

def load_papers_data(json_path: str) -> list:
    """加载论文数据"""
    if not os.path.exists(json_path):
        print(f"[Warning] {json_path} not found")
        return []
    
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_title(title: str) -> str:
    """标准化标题用于匹配"""
    # 转小写，移除标点，保留字母数字空格
    title = title.lower()
    title = re.sub(r'[^\w\s]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def match_paper(pub_title: str, papers: list) -> dict:
    """匹配论文并返回引用数"""
    pub_words = set(normalize_title(pub_title).split())
    pub_words = {w for w in pub_words if len(w) > 3}
    
    best_match = None
    best_score = 0
    
    for paper in papers:
        paper_title = normalize_title(paper.get('title', ''))
        paper_words = [w for w in paper_title.split() if len(w) > 3]
        
        if not paper_words:
            continue
        
        match_count = sum(1 for w in paper_words if w in pub_words)
        score = match_count / len(paper_words)
        
        if score > best_score and score > 0.4:
            best_score = score
            best_match = paper
    
    return best_match

def update_pub_md(pub_md_path: str, papers: list) -> int:
    """更新 pub.md 中的引用数徽章"""
    if not os.path.exists(pub_md_path):
        print(f"[Error] {pub_md_path} not found")
        return 0
    
    with open(pub_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    update_count = 0
    
    # 匹配模式: [论文标题](链接) [![](https://img.shields.io/badge/citations-数字-blue...
    # 需要找到论文标题和对应的徽章
    pattern = r'\[([^\]]+)\]\([^\)]+\)\s*\[!\[\]\(https://img\.shields\.io/badge/citations-(\d+)-blue'
    
    def replace_citation(match):
        nonlocal update_count
        title = match.group(1)
        old_citations = int(match.group(2))
        
        # 跳过太短的标题（可能是 Code 等链接）
        if len(title) < 20:
            return match.group(0)
        
        paper = match_paper(title, papers)
        if paper and paper.get('citations') is not None:
            new_citations = paper['citations']
            if new_citations != old_citations:
                update_count += 1
                print(f"  ✓ '{title[:40]}...' : {old_citations} → {new_citations}")
                return match.group(0).replace(f'citations-{old_citations}-blue', f'citations-{new_citations}-blue')
        
        return match.group(0)
    
    content = re.sub(pattern, replace_citation, content)
    
    if content != original_content:
        with open(pub_md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n[Success] Updated {update_count} citation badges in pub.md")
    else:
        print("[Info] No updates needed for pub.md")
    
    return update_count

def main():
    print("=" * 50)
    print("更新 pub.md 中的引用数徽章")
    print("=" * 50)
    
    # 确定路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(script_dir, 'results')
    repo_root = os.path.dirname(script_dir)
    
    json_path = os.path.join(results_dir, 'first_author_papers.json')
    pub_md_path = os.path.join(repo_root, '_pages', 'includes', 'pub.md')
    
    # 加载论文数据
    papers = load_papers_data(json_path)
    if not papers:
        print("[Warning] No papers data available, skipping update")
        return
    
    print(f"[Info] Loaded {len(papers)} papers from JSON")
    print()
    
    # 更新 pub.md
    update_pub_md(pub_md_path, papers)

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
智能更新 pub.md 中的引用数徽章
- 引用数 >= 10：自动添加/更新徽章
- 引用数 < 10：不添加或移除已有徽章
"""

import json
import re
import os

MIN_CITATIONS_TO_SHOW = 10  # 最低显示引用数阈值

def load_papers_data(json_path: str) -> list:
    """加载论文数据"""
    if not os.path.exists(json_path):
        print(f"[Warning] {json_path} not found")
        return []
    
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_title(title: str) -> str:
    """标准化标题用于匹配"""
    title = title.lower()
    title = re.sub(r'[^\w\s]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def match_paper(pub_title: str, papers: list) -> dict:
    """匹配论文并返回数据"""
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

def create_badge(citations: int) -> str:
    """创建引用徽章 markdown"""
    return f' [![](https://img.shields.io/badge/citations-{citations}-blue?logo=google-scholar&logoColor=white&style=flat-square)](https://scholar.google.com/citations?user=hCvlj5cAAAAJ)'

def update_pub_md(pub_md_path: str, papers: list) -> int:
    """智能更新 pub.md 中的引用徽章"""
    if not os.path.exists(pub_md_path):
        print(f"[Error] {pub_md_path} not found")
        return 0
    
    with open(pub_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    update_count = 0
    
    # 正则匹配论文标题链接（带或不带徽章）
    # 模式1: [标题](链接) [![徽章]...]  - 已有徽章
    # 模式2: [标题](链接) <span  - 无徽章
    # 模式3: [标题](链接) \\  - 无徽章，直接换行
    
    def process_paper_line(match):
        nonlocal update_count
        full_match = match.group(0)
        title = match.group(1)
        link = match.group(2)
        existing_badge = match.group(3) if match.lastindex >= 3 else ''
        after_part = match.group(4) if match.lastindex >= 4 else ''
        
        # 跳过太短的标题（可能是 Code 等链接）
        if len(title) < 25:
            return full_match
        
        # 匹配论文
        paper = match_paper(title, papers)
        
        if paper:
            citations = paper.get('citations', 0) or 0
            
            if citations >= MIN_CITATIONS_TO_SHOW:
                # 需要显示徽章
                new_badge = create_badge(citations)
                
                if existing_badge:
                    # 已有徽章，检查是否需要更新
                    old_num_match = re.search(r'citations-(\d+)-blue', existing_badge)
                    if old_num_match:
                        old_num = int(old_num_match.group(1))
                        if old_num != citations:
                            update_count += 1
                            print(f"  ✓ 更新 '{title[:35]}...' : {old_num} → {citations}")
                            return f'[{title}]({link}){new_badge}{after_part}'
                    return full_match  # 数字相同，不变
                else:
                    # 没有徽章，添加新徽章
                    update_count += 1
                    print(f"  + 添加 '{title[:35]}...' : {citations} citations")
                    return f'[{title}]({link}){new_badge}{after_part}'
            else:
                # 引用数不够，移除徽章（如果有）
                if existing_badge:
                    update_count += 1
                    print(f"  - 移除 '{title[:35]}...' : {citations} < {MIN_CITATIONS_TO_SHOW}")
                    return f'[{title}]({link}){after_part}'
        
        return full_match
    
    # 匹配: [论文标题](链接) 可选的徽章 后续内容
    # 徽章格式: [![](https://img.shields.io/badge/citations-数字-blue...)](...)
    pattern = r'\[([^\]]{25,})\]\(([^\)]+)\)(\s*\[!\[\]\(https://img\.shields\.io/badge/citations-\d+-blue[^\)]*\)\]\([^\)]+\))?(\s*<span|\s*\\\\)'
    
    content = re.sub(pattern, process_paper_line, content)
    
    if content != original_content:
        with open(pub_md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n[Success] 共更新 {update_count} 处引用徽章")
    else:
        print("[Info] pub.md 无需更新")
    
    return update_count

def main():
    print("=" * 50)
    print(f"智能更新引用徽章 (阈值: >= {MIN_CITATIONS_TO_SHOW})")
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
        print("[Warning] 无论文数据，跳过更新")
        return
    
    print(f"[Info] 加载 {len(papers)} 篇论文数据")
    print()
    
    # 更新 pub.md
    update_pub_md(pub_md_path, papers)

if __name__ == '__main__':
    main()

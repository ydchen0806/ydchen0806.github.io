#!/usr/bin/env python3
"""
简化测试脚本，用于调试 Google Scholar 爬虫问题
"""
import os
import sys
import json
from datetime import datetime

def test_connection():
    """测试网络连接"""
    print("测试网络连接...")
    
    try:
        import requests
        
        url = "https://scholar.google.com"
        print(f"尝试访问: {url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # 禁用代理
        proxies = {
            'http': None,
            'https': None,
        }
        
        response = requests.get(url, headers=headers, timeout=10, proxies=proxies, verify=False)
        print(f"响应状态码: {response.status_code}")
        content = response.text[:200]
        print(f"响应内容预览: {content}...")
        
        return response.status_code == 200
            
    except Exception as e:
        print(f"连接测试失败: {e}")
        return False

def test_scholarly():
    """测试scholarly库"""
    print("\n测试scholarly库...")
    
    try:
        from scholarly import scholarly
        
        # 尝试搜索作者
        print("尝试搜索作者...")
        author_id = "hCvlj5cAAAAJ"  # 使用默认ID
        
        try:
            # 简单搜索，不获取详细数据
            print("正在搜索作者ID...")
            author = scholarly.search_author_id(author_id)
            print(f"找到作者: {author.get('name', 'Unknown')}")
            print(f"引用数: {author.get('citedby', 'Unknown')}")
            return True
        except Exception as e:
            print(f"搜索作者失败: {e}")
            return False
            
    except ImportError as e:
        print(f"无法导入scholarly库: {e}")
        print("请尝试运行: pip install scholarly")
        return False

def main():
    """主函数"""
    print("Google Scholar 爬虫简化测试")
    print(f"当前时间: {datetime.now()}")
    print("=" * 50)
    
    # 测试网络连接
    connection_ok = test_connection()
    
    # 如果连接正常，测试scholarly库
    if connection_ok:
        scholarly_ok = test_scholarly()
        
        if scholarly_ok:
            print("\n[OK] 测试成功")
            return 0
        else:
            print("\n[ERROR] scholarly库测试失败")
            return 1
    else:
        print("\n[ERROR] 网络连接测试失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())
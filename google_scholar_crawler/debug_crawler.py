#!/usr/bin/env python3
"""
调试版 Google Scholar 爬虫
"""
import requests
import json
from datetime import datetime
import os
import sys
import ssl

def test_basic_request():
    """测试基本请求"""
    print("测试基本请求...")
    
    # 禁用代理
    proxies = {
        'http': None,
        'https': None,
    }
    
    try:
        print("测试请求1: www.google.com")
        response = requests.get("https://www.google.com", timeout=10, proxies=proxies, verify=False)
        print(f"成功: 状态码 {response.status_code}")
        
        print("测试请求2: scholar.google.com")
        response = requests.get("https://scholar.google.com", timeout=10, proxies=proxies, verify=False)
        print(f"成功: 状态码 {response.status_code}")
        
        return True
        
    except Exception as e:
        print(f"请求失败: {e}")
        return False

def get_scholar_stats_debug(scholar_id):
    """
    调试版获取Google Scholar数据
    """
    try:
        print(f"[DEBUG] 正在获取学者信息: {scholar_id}")
        url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }
        
        # 禁用代理
        proxies = {
            'http': None,
            'https': None,
        }
        
        print(f"[DEBUG] 请求URL: {url}")
        print("[DEBUG] 正在发送请求...")
        
        # 发送请求
        response = requests.get(
            url, 
            headers=headers, 
            timeout=30, 
            verify=False,
            proxies=proxies
        )
        
        print(f"[DEBUG] 响应状态码: {response.status_code}")
        print(f"[DEBUG] 响应头: {response.headers}")
        print(f"[DEBUG] 响应内容长度: {len(response.text)}")
        print(f"[DEBUG] 响应内容前200字符: {response.text[:200]}")
        
        if response.status_code != 200:
            print(f"[ERROR] 无法访问Google Scholar页面，状态码: {response.status_code}")
            return None
            
        print("[DEBUG] 正在解析HTML内容...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取基本信息
        name_element = soup.find('div', {'id': 'gsc_prf_in'})
        name = name_element.text if name_element else "Unknown"
        print(f"[DEBUG] 找到学者姓名: {name}")
        
        # 构建简化版数据对象
        author_data = {
            'name': name,
            'citedby': 9999,  # 示例数据
            'hindex': 99,      # 示例数据
            'i10index': 99,    # 示例数据
            'updated': str(datetime.now()),
            'publications': {},
            'source': 'debug_scraper'
        }
        
        print("[DEBUG] 成功构建数据对象")
        return author_data
        
    except Exception as e:
        print(f"[ERROR] 获取数据时出错: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """主函数"""
    print("Google Scholar 爬虫调试版")
    print("=" * 50)
    
    # 测试基本网络连接
    if not test_basic_request():
        print("[ERROR] 基本网络连接测试失败")
        return 1
        
    # 获取环境变量
    scholar_id = 'hCvlj5cAAAAJ'  # 直接使用测试ID
    print(f"使用测试 GOOGLE_SCHOLAR_ID: {scholar_id}")
    
    print("=" * 50)
    
    # 尝试获取数据
    author = get_scholar_stats_debug(scholar_id)
    
    if not author:
        print("[ERROR] 无法获取Google Scholar数据")
        return 1
        
    print("=" * 50)
    print("[OK] 测试成功")
    print(f"姓名: {author['name']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
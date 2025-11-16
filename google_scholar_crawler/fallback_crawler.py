import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import os
import sys
import time

def get_scholar_stats_fallback(scholar_id):
    """
    备用方法：直接抓取Google Scholar页面获取基本统计信息
    """
    try:
        print("使用备用方法获取Google Scholar数据...")
        url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"无法访问Google Scholar页面，状态码: {response.status_code}")
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取基本信息
        name_element = soup.find('div', {'id': 'gsc_prf_in'})
        name = name_element.text if name_element else "Unknown"
        
        # 提取统计信息
        stats_table = soup.find('table', {'class': 'gsc_rsb_std'})
        if not stats_table:
            print("无法找到统计信息表格")
            return None
            
        stats_cells = stats_table.find_all('td', {'class': 'gsc_rsb_std'})
        
        if len(stats_cells) < 3:
            print("统计信息不完整")
            return None
            
        citations = stats_cells[0].text.replace(',', '')
        h_index = stats_cells[2].text.replace(',', '')
        i10_index = stats_cells[4].text.replace(',', '')
        
        # 构建数据对象
        author_data = {
            'name': name,
            'citedby': int(citations) if citations.isdigit() else 0,
            'hindex': int(h_index) if h_index.isdigit() else 0,
            'i10index': int(i10_index) if i10_index.isdigit() else 0,
            'updated': str(datetime.now()),
            'publications': {},  # 备用方法不获取详细论文列表
            'source': 'fallback_scraper'
        }
        
        print(f"✓ 备用方法成功获取基本信息: {name}")
        print(f"✓ 总引用数: {author_data['citedby']}")
        print(f"✓ h-index: {author_data['hindex']}")
        print(f"✓ i10-index: {author_data['i10index']}")
        
        return author_data
        
    except Exception as e:
        print(f"备用方法也失败了: {e}")
        return None

def main():
    try:
        # 获取环境变量
        scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
        if not scholar_id:
            print("❌ 错误: GOOGLE_SCHOLAR_ID 环境变量未设置")
            scholar_id = 'hCvlj5cAAAAJ'  # 替代ID
            print(f"使用替代的 GOOGLE_SCHOLAR_ID: {scholar_id}")
        
        print(f"正在获取学者信息: {scholar_id}")
        print("=" * 50)
        
        # 尝试使用备用方法获取数据
        author = get_scholar_stats_fallback(scholar_id)
        
        if not author:
            print("❌ 无法获取Google Scholar数据")
            sys.exit(1)
        
        print("=" * 50)
        
        # 创建results目录
        os.makedirs('results', exist_ok=True)
        
        # 保存完整数据
        with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
            json.dump(author, outfile, ensure_ascii=False, indent=2)
        print("✓ 完整数据已保存到 results/gs_data.json")
        
        # 保存shields.io格式数据
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{author['citedby']}",
            "color": "blue"
        }
        
        with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)
        print("✓ Shields.io 数据已保存到 results/gs_data_shieldsio.json")
        
        # 输出基本信息用于调试
        print("\n" + "=" * 50)
        print("基本统计信息:")
        print(f"  姓名: {author['name']}")
        print(f"  引用数: {author['citedby']}")
        print(f"  h-index: {author['hindex']}")
        print(f"  i10-index: {author['i10index']}")
        print(f"  更新时间: {author['updated']}")
        print(f"  数据源: {author.get('source', 'unknown')}")
        print("=" * 50)
        
        return 0
        
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
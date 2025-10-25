import json
import sys
from scholarly import scholarly
import time

def get_scholar_stats(scholar_id, retries=3):
    """
    获取Google Scholar统计信息，带重试机制
    """
    for attempt in range(retries):
        try:
            print(f"尝试 {attempt + 1}/{retries}: 正在获取学者ID: {scholar_id} 的信息...")
            
            # 搜索作者
            search_query = scholarly.search_author_id(scholar_id)
            author = scholarly.fill(search_query)
            
            # 获取引用数
            citations = author.get('citedby', 0)
            
            print(f"✓ 成功获取引用数: {citations}")
            return citations
            
        except Exception as e:
            print(f"✗ 第 {attempt + 1} 次尝试失败: {e}")
            if attempt < retries - 1:
                wait_time = (attempt + 1) * 5  # 递增等待时间
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                print("所有重试都失败了")
                return None
    
    return None

def main():
    # 你的Google Scholar ID
    scholar_id = "hCvlj5cAAAAJ"
    
    print("=" * 50)
    print("开始获取Google Scholar统计信息...")
    print("=" * 50)
    
    citations = get_scholar_stats(scholar_id)
    
    if citations is None:
        print("\n❌ 错误: 无法获取统计信息")
        print("脚本将以错误代码退出")
        sys.exit(1)  # 以非零退出码退出，让 GitHub Actions 知道失败了
    
    # 创建JSON数据
    data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations),
        "color": "blue",
        "citedby": citations
    }
    
    # 保存JSON文件
    try:
        with open('gs_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ 统计信息已成功保存到 gs_data.json")
        print(f"✓ 总引用数: {citations}")
        print("=" * 50)
        
        # 验证文件是否真的被创建
        with open('gs_data.json', 'r') as f:
            saved_data = json.load(f)
            print(f"✓ 文件验证成功: {saved_data}")
            
    except Exception as e:
        print(f"\n❌ 保存文件时出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
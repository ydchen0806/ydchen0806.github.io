import json
from scholarly import scholarly
import time

def get_scholar_stats(scholar_id):
    """
    获取Google Scholar统计信息
    """
    try:
        print(f"正在获取学者ID: {scholar_id} 的信息...")
        
        # 搜索作者
        search_query = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(search_query)
        
        # 获取引用数
        citations = author.get('citedby', 0)
        
        print(f"成功获取引用数: {citations}")
        return citations
    except Exception as e:
        print(f"获取统计信息时出错: {e}")
        # 如果失败，返回一个默认值
        return 200

def main():
    # 你的Google Scholar ID
    scholar_id = "hCvlj5cAAAAJ"
    
    print("开始获取Google Scholar统计信息...")
    citations = get_scholar_stats(scholar_id)
    
    if citations is not None:
        # 创建JSON数据
        data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(citations),
            "color": "blue",
            "citedby": citations
        }
        
        # 保存JSON文件
        with open('gs_data.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"统计信息已保存到 gs_data.json")
        print(f"总引用数: {citations}")
    else:
        print("获取统计信息失败")

if __name__ == "__main__":
    main()
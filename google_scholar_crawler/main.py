from scholarly import scholarly
import json
from datetime import datetime
import os
import sys

def main():
    try:
        # 获取环境变量
        scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID')
        if not scholar_id:
            print("❌ 错误: GOOGLE_SCHOLAR_ID 环境变量未设置")
            sys.exit(1)
        
        print(f"正在获取学者信息: {scholar_id}")
        print("=" * 50)
        
        # 搜索并填充作者信息
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        
        name = author['name']
        author['updated'] = str(datetime.now())
        
        # 转换publications为字典格式
        author['publications'] = {v['author_pub_id']: v for v in author['publications']}
        
        print(f"✓ 成功获取 {name} 的信息")
        print(f"✓ 总引用数: {author['citedby']}")
        print(f"✓ 论文数量: {len(author['publications'])}")
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
        print(f"  姓名: {name}")
        print(f"  引用数: {author['citedby']}")
        print(f"  h-index: {author.get('hindex', 'N/A')}")
        print(f"  i10-index: {author.get('i10index', 'N/A')}")
        print(f"  更新时间: {author['updated']}")
        print("=" * 50)
        
        return 0
        
    except KeyError as e:
        print(f"❌ 数据键错误: {e}")
        print("可能是 Google Scholar 返回的数据格式有变化")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
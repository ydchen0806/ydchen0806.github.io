#!/usr/bin/env python3
"""
模拟爬虫 - 用于生成测试数据并验证数据保存流程
"""
import json
from datetime import datetime
import os
import sys

def create_mock_data():
    """创建基于真实Google Scholar数据的模拟数据"""
    return {
        'name': 'Yinda Chen',
        'citedby': 436,  # 真实总引用数
        'citedby5y': 429,  # 自2020年引用数
        'hindex': 9,    # 真实h-index
        'hindex5y': 9,  # 自2020年h-index
        'i10index': 9,  # 真实i10-index
        'i10index5y': 9,  # 自2020年i10-index
        'affiliation': 'University of Science and Technology of China',
        'email': 'ydchen0806@gmail.com',
        'interests': ['Computer Vision', 'Self-Supervised Learning', 'Multimodal Learning', 'Image Processing'],
        'homepage': 'https://ydchen0806.github.io/',
        'updated': str(datetime.now()),
        'publications': {
            'pub1': {
                'title': 'EMPOWER: Evolutionary Medical Prompt Optimization With Reinforcement Learning',
                'author': 'Yinda Chen, Yangfan He, Jing Yang, Dapeng Zhang, Zhenlong Yuan, Muhammad Attique Khan, Jamel Baili, Por Lip Yee',
                'pub_year': '2025',
                'venue': 'IEEE Journal of Biomedical and Health Informatics',
                'citedby': 15,
                'url': 'https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11205280'
            },
            'pub2': {
                'title': 'Unsupervised Domain Adaptation for EM Image Denoising with Invertible Networks',
                'author': 'Shiyu Deng, Yinda Chen, Wei Huang, Ruobing Zhang, Zhiwei Xiong',
                'pub_year': '2024',
                'venue': 'IEEE Transactions on Medical Imaging',
                'citedby': 35,
                'url': ''
            },
            'pub3': {
                'title': 'TokenUnify: Scaling Up Autoregressive Pretraining for Computer Vision',
                'author': 'Yinda Chen, Haoyuan Shi, Xiaoyu Liu, Te Shi, Ruobing Zhang, Dong Liu, Zhiwei Xiong, Feng Wu',
                'pub_year': '2025',
                'venue': 'ICCV',
                'citedby': 8,
                'url': 'https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_TokenUnify_Scaling_Up_Autoregressive_Pretraining_for_Neuron_Segmentation_ICCV_2025_paper.pdf'
            },
            'pub4': {
                'title': 'MaskTwins: Dual-form Complementary Masking for Domain-Adaptive Image Segmentation',
                'author': 'Jiawen Wang, Yinda Chen, Xiaoyu Liu, Che Liu, Dong Liu, Jianqing Gao, Zhiwei Xiong',
                'pub_year': '2025',
                'venue': 'ICML',
                'citedby': 5,
                'url': 'https://openreview.net/pdf?id=9CpeZ8BzPO'
            },
            'pub5': {
                'title': 'Condition-generation Latent Coding with an External Dictionary for Deep Image Compression',
                'author': 'Siqi Wu, Yinda Chen, Dong Liu, Zhihai He',
                'pub_year': '2025',
                'venue': 'AAAI',
                'citedby': 12,
                'url': ''
            }
        },
        'source': 'mock_data_based_on_real_scholar',
        'note': '这是基于真实Google Scholar数据的模拟数据'
    }

def main():
    """主函数"""
    print("Google Scholar 模拟爬虫")
    print("=" * 50)
    
    # 创建模拟数据
    print("正在生成模拟数据...")
    author = create_mock_data()
    
    print(f"姓名: {author['name']}")
    print(f"引用数: {author['citedby']}")
    print(f"h-index: {author['hindex']}")
    print(f"i10-index: {author['i10index']}")
    print(f"论文数量: {len(author['publications'])}")
    
    print("=" * 50)
    
    # 创建results目录
    os.makedirs('results', exist_ok=True)
    
    # 保存完整数据
    with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)
    print("[OK] 完整数据已保存到 results/gs_data.json")
    
    # 保存shields.io格式数据
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
        "color": "blue"
    }
    
    with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)
    print("[OK] Shields.io 数据已保存到 results/gs_data_shieldsio.json")
    
    # 验证文件是否创建
    print("\n验证文件:")
    if os.path.exists('results/gs_data.json'):
        print("[OK] gs_data.json 文件已创建")
        with open('results/gs_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"姓名: {data['name']}, 引用数: {data['citedby']}")
    else:
        print("[ERROR] gs_data.json 文件未创建")
        
    if os.path.exists('results/gs_data_shieldsio.json'):
        print("[OK] gs_data_shieldsio.json 文件已创建")
        with open('results/gs_data_shieldsio.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"Badge数据: {data}")
    else:
        print("[ERROR] gs_data_shieldsio.json 文件未创建")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
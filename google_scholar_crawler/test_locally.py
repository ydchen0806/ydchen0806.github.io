#!/usr/bin/env python3
"""
本地测试脚本，用于测试Google Scholar爬虫
"""
import os
import subprocess
import sys
from datetime import datetime

def test_method(method_name, script_path):
    """测试指定的方法"""
    print(f"\n{'='*60}")
    print(f"测试方法: {method_name}")
    print(f"脚本路径: {script_path}")
    print(f"开始时间: {datetime.now()}")
    print(f"{'='*60}")
    
    try:
        # 设置环境变量
        env = os.environ.copy()
        env['GOOGLE_SCHOLAR_ID'] = 'hCvlj5cAAAAJ'
        
        # 运行脚本
        start_time = datetime.now()
        result = subprocess.run(
            [sys.executable, script_path],
            env=env,
            capture_output=True,
            text=True,
            timeout=60  # 60秒超时
        )
        end_time = datetime.now()
        
        # 输出结果
        print(f"结束时间: {end_time}")
        print(f"耗时: {end_time - start_time}")
        print(f"返回代码: {result.returncode}")
        
        if result.stdout:
            print("\n标准输出:")
            print(result.stdout)
            
        if result.stderr:
            print("\n标准错误:")
            print(result.stderr)
        
        # 检查结果文件
        if os.path.exists('results/gs_data.json'):
            print("\n✓ 结果文件已生成")
            with open('results/gs_data.json', 'r', encoding='utf-8') as f:
                data = f.read()
                print("文件内容预览:")
                print(data[:200] + "..." if len(data) > 200 else data)
        else:
            print("\n❌ 结果文件未生成")
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("\n❌ 测试超时")
        return False
    except Exception as e:
        print(f"\n❌ 测试出错: {e}")
        return False

def main():
    """主函数"""
    print("Google Scholar爬虫本地测试")
    print(f"当前工作目录: {os.getcwd()}")
    
    # 切换到爬虫目录
    crawler_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(crawler_dir)
    
    # 测试主要方法
    primary_success = test_method("主要方法 (scholarly库)", "main.py")
    
    # 如果主要方法失败，测试备用方法
    if not primary_success:
        print("\n主要方法失败，测试备用方法...")
        fallback_success = test_method("备用方法 (直接爬取)", "fallback_crawler.py")
    else:
        print("\n主要方法成功，无需测试备用方法")
        fallback_success = True
    
    # 总结
    print(f"\n{'='*60}")
    if primary_success or fallback_success:
        print("✓ 至少有一种方法成功获取数据")
    else:
        print("❌ 所有方法都失败了")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
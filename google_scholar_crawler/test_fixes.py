#!/usr/bin/env python3
"""
测试修复的爬虫脚本
"""
import os
import sys
import subprocess

def run_script(script_name):
    """运行指定脚本并返回结果"""
    print(f"\n{'='*60}")
    print(f"测试脚本: {script_name}")
    print(f"{'='*60}")
    
    try:
        # 设置环境变量
        env = os.environ.copy()
        env['GOOGLE_SCHOLAR_ID'] = 'hCvlj5cAAAAJ'
        
        # 运行脚本
        result = subprocess.run(
            [sys.executable, script_name],
            env=env,
            capture_output=True,
            text=True,
            timeout=20  # 20秒超时
        )
        
        # 检查结果文件
        success = os.path.exists('results/gs_data.json') and os.path.exists('results/gs_data_shieldsio.json')
        
        if success:
            print("[OK] 测试成功 - 结果文件已生成")
            if result.stdout:
                print("标准输出预览:")
                print(result.stdout[:500] + ("..." if len(result.stdout) > 500 else ""))
            if result.stderr:
                print("标准错误预览:")
                print(result.stderr[:500] + ("..." if len(result.stderr) > 500 else ""))
        else:
            print("[ERROR] 测试失败 - 结果文件未生成")
            if result.stdout:
                print("标准输出:")
                print(result.stdout)
            if result.stderr:
                print("标准错误:")
                print(result.stderr)
        
        return success
        
    except subprocess.TimeoutExpired:
        print("[ERROR] 测试超时")
        return False
    except Exception as e:
        print(f"[ERROR] 测试出错: {e}")
        return False

def main():
    """主函数"""
    print("Google Scholar 爬虫修复测试")
    
    # 确保在正确的目录中
    crawler_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(crawler_dir)
    
    # 测试各个脚本
    scripts = [
        'mock_crawler.py',      # 首先测试模拟数据
        'simple_crawler.py',    # 然后测试简单爬虫
        'fallback_crawler.py',  # 然后测试备用爬虫
        'robust_crawler.py',    # 最后测试健壮爬虫
    ]
    
    results = {}
    for script in scripts:
        if os.path.exists(script):
            results[script] = run_script(script)
        else:
            print(f"脚本 {script} 不存在")
            results[script] = False
    
    # 总结
    print(f"\n{'='*60}")
    print("测试总结:")
    print(f"{'='*60}")
    
    for script, success in results.items():
        status = "[OK]" if success else "[ERROR]"
        print(f"{status} {script}")
    
    # 推荐使用的脚本
    successful_scripts = [s for s, success in results.items() if success]
    
    if successful_scripts:
        print("\n推荐使用的脚本:")
        print(f"1. {successful_scripts[-1]} (最健壮的解决方案)")
    else:
        print("\n[WARNING] 所有脚本都失败了")
    
    print(f"\n{'='*60}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
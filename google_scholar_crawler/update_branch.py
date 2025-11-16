#!/usr/bin/env python3
"""
手动更新google-scholar-stats分支的脚本
"""
import os
import sys
import subprocess

def run_command(command, check=True):
    """运行shell命令"""
    print(f"执行命令: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"错误: {result.stderr}")
        return False
    if result.stdout:
        print(result.stdout)
    return True

def main():
    """主函数"""
    # 切换到主仓库目录
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_dir)
    print(f"当前工作目录: {os.getcwd()}")
    
    # 确保最新数据已生成
    if not os.path.exists("google_scholar_crawler/results/gs_data.json"):
        print("错误: 未找到Google Scholar数据文件")
        print("请先运行: python google_scholar_crawler/robust_crawler.py")
        return 1
    
    # 检查git状态
    run_command("git status")
    
    # 配置Git
    run_command('git config user.email "github-actions[bot]@users.noreply.github.com"')
    run_command('git config user.name "github-actions[bot]"')
    
    # 获取远程分支信息
    run_command("git fetch origin")
    
    # 切换到目标分支（如果不存在则创建）
    if run_command("git checkout google-scholar-stats", check=False) and run_command("git pull origin google-scholar-stats", check=False):
        print("已切换到google-scholar-stats分支并更新")
    else:
        print("创建新的google-scholar-stats分支")
        run_command("git checkout --orphan google-scholar-stats")
    
    # 清理分支内容
    run_command("git rm -rf .", check=False)
    run_command("git clean -fd")
    
    # 复制新数据
    run_command("cp google_scholar_crawler/results/* .")
    
    # 创建README
    readme_content = """# Google Scholar Statistics

This branch contains automatically updated Google Scholar statistics.

## Files

- `gs_data.json`: Complete scholar profile data
- `gs_data_shieldsio.json`: Shields.io badge format data

**Last updated:** {}

## Usage

### Display Citation Badge

Add this to your README.md:

```markdown
![Google Scholar Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)
```

Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual GitHub username and repository name.

### Access Raw Data

```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data.json
```

---

*This data is automatically updated by GitHub Actions.*
""".format(subprocess.check_output("date -u +'%Y-%m-%d %H:%M:%S UTC'", shell=True).decode().strip())
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    # 提交更改
    run_command("git add .")
    
    # 检查是否有变化需要提交
    result = subprocess.run("git diff --staged --quiet", shell=True)
    if result.returncode == 0:
        print("没有变化需要提交")
    else:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        run_command(f'git commit -m "Update Google Scholar stats - {timestamp}"')
        run_command("git push -f origin google-scholar-stats")
        print("✅ 成功推送更新")
    
    # 切换回主分支
    run_command("git checkout main")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
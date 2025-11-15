# Google Scholar Stats Crawler

自动获取并更新 Google Scholar 统计数据的工具。

## 功能特性

- ✅ 自动抓取 Google Scholar 个人主页数据
- ✅ 生成 Shields.io 兼容的徽章数据
- ✅ 每周三次自动更新（周一、周三、周五，可手动触发）
- ✅ 数据保存在独立的 orphan 分支

## 文件结构

```
google_scholar_crawler/
├── main.py              # 主脚本
├── requirements.txt     # Python 依赖
└── README.md           # 本文档

.github/
└── workflows/
    └── scholar_stats.yml  # GitHub Actions 工作流
```

## 快速开始

### 1. 设置 GitHub Secret

1. 进入仓库的 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 添加以下 secret：
   - Name: `GOOGLE_SCHOLAR_ID`
   - Value: 你的 Google Scholar ID（例如：`hCvlj5cAAAAJ`）

> 💡 **如何找到你的 Scholar ID？**
> 访问你的 Google Scholar 个人主页，URL 中 `user=` 后面的字符串就是你的 ID
> 
> 例如：`https://scholar.google.com/citations?user=hCvlj5cAAAAJ`
> 
> 你的 ID 就是：`hCvlj5cAAAAJ`

### 2. 运行 Workflow

#### 方式一：手动触发

1. 进入仓库的 **Actions** 页面
2. 选择 **Get Google Scholar Stats** workflow
3. 点击 **Run workflow** → **Run workflow**

#### 方式二：自动运行

Workflow 会在每周一、周三、周五 UTC 00:00 自动运行（每周三次）。

### 3. 查看结果

运行成功后，数据会保存在 `google-scholar-stats` 分支：

- `gs_data.json` - 完整的学者数据
- `gs_data_shieldsio.json` - Shields.io 徽章数据格式

## 使用方法

### 在 README 中显示引用数徽章

在你的 README.md 中添加：

```markdown
![Google Scholar Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)
```

记得替换 `YOUR_USERNAME` 和 `YOUR_REPO`！

### 自定义徽章样式

```markdown
<!-- 蓝色徽章 -->
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&color=blue)

<!-- 绿色徽章 -->
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&color=green)

<!-- 带 Google Scholar 图标 -->
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)

<!-- 扁平风格 -->
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data_shieldsio.json&style=flat-square)
```

### 访问原始数据

```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/google-scholar-stats/gs_data.json
```

## 本地测试

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export GOOGLE_SCHOLAR_ID="你的Scholar ID"

# 运行脚本
python main.py

# 查看结果
cat results/gs_data_shieldsio.json
```

## 输出数据格式

### gs_data_shieldsio.json

```json
{
  "schemaVersion": 1,
  "label": "citations",
  "message": "1234",
  "color": "blue"
}
```

### gs_data.json

包含完整的学者信息：
- 基本信息（姓名、机构等）
- 引用统计（总引用数、h-index、i10-index）
- 论文列表
- 引用历史

## 常见问题

### Q: Workflow 失败了怎么办？

A: 检查以下几点：
1. 确认 `GOOGLE_SCHOLAR_ID` secret 已正确设置
2. 查看 Actions 日志中的具体错误信息
3. Google Scholar 可能有反爬虫限制，稍后重试

### Q: 如何更改更新频率？

A: 编辑 `.github/workflows/scholar_stats.yml`，修改 cron 表达式：

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'  # 每周日
    # - cron: '0 0 1 * *'  # 每月1日
    # - cron: '0 0 * * 1'  # 每周一
```

### Q: 可以不使用 Secret 吗？

A: 可以，直接在 workflow 中硬编码：

```yaml
- name: Fetch Google Scholar stats
  env:
    GOOGLE_SCHOLAR_ID: 'hCvlj5cAAAAJ'  # 直接写你的 ID
  run: |
    python google_scholar_crawler/main.py
```

但使用 Secret 更安全，建议采用。

## 许可证

MIT License

## 相关链接

- [scholarly 文档](https://scholarly.readthedocs.io/)
- [Shields.io 文档](https://shields.io/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
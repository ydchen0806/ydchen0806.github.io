# Google Scholar 自动更新系统

## 📋 工作原理

### 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                     GitHub Actions (定时任务)                      │
│                    每周一/三/五 UTC 00:00 自动运行                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    serpapi_crawler.py                            │
│  1. 调用 SerpAPI 获取 Google Scholar 真实数据                      │
│  2. 成功后自动更新脚本中的保底数据                                   │
│  3. 失败时使用保底数据                                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                 google-scholar-stats 分支                        │
│  存储 JSON 数据文件:                                              │
│  - gs_data.json (完整数据)                                        │
│  - gs_data_shieldsio.json (徽章格式)                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      你的个人主页                                  │
│  通过 shields.io 读取 JSON 动态显示引用数徽章                        │
│  img.shields.io/endpoint?url=raw.github...gs_data_shieldsio.json │
└─────────────────────────────────────────────────────────────────┘
```

### 核心流程

1. **GitHub Actions 定时触发** → 每周 3 次自动运行
2. **SerpAPI 请求** → 调用 Google Scholar Author API 获取真实数据
3. **数据处理** → 提取引用数、h-index、i10-index 等指标
4. **自动更新保底** → 成功后自动更新脚本中的保底值（下次失败时使用）
5. **保存到分支** → 将 JSON 数据推送到 `google-scholar-stats` 分支
6. **主页显示** → shields.io 读取 JSON 生成动态徽章

---

## 🔧 设置步骤

### 1. 注册 SerpAPI 账号

访问 [https://serpapi.com/](https://serpapi.com/) 注册免费账号。

- ✅ 免费额度：**100 次/月**
- ✅ 每周 3 次更新约 12-13 次/月，完全够用

### 2. 获取 API Key

登录后，在 Dashboard 页面可以找到你的 API Key。

### 3. 在 GitHub 设置 Secret

1. 进入你的 GitHub 仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 名称：`SERPAPI_KEY`
5. 值：你的 SerpAPI API Key
6. 点击 **Add secret**

### 4. 测试运行

1. 进入仓库的 **Actions** 页面
2. 选择 **Get Google Scholar Stats** workflow
3. 点击 **Run workflow** 手动触发
4. 查看运行日志，确认数据获取成功

---

## 📊 可用数据与主页集成

SerpAPI 返回的数据可以用于主页的多种展示：

### 1. 引用数徽章（已集成）

```markdown
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white&label=citations)
```

显示效果：动态引用数徽章

### 2. H-Index 徽章

可以添加 h-index 显示，修改爬虫生成额外的 JSON：

```markdown
![H-Index](https://img.shields.io/badge/h--index-9-blue?logo=google-scholar&logoColor=white)
```

### 3. 引用趋势图

爬虫已获取 `citation_graph` 数据（每年引用数），可用于：
- 生成 SVG 趋势图
- 在主页展示引用增长曲线

### 4. 研究兴趣标签

爬虫获取的 `interests` 字段可自动更新主页的研究兴趣标签。

---

## 🔄 自动更新保底数据

当 SerpAPI 成功获取数据后，脚本会**自动更新**保底值：

```python
# serpapi_crawler.py 中的保底数据会被自动更新
FALLBACK_DATA = {
    "citedby": 436,   # ← 自动更新
    "hindex": 9,      # ← 自动更新
    "i10index": 9,    # ← 自动更新
}
```

这样即使下次 API 请求失败，也会使用最近一次成功的数据。

---

## 📈 扩展功能（可选）

### 自动更新 h-index 徽章

在 `_includes/` 或主页模板中添加：

```html
<!-- 动态 h-index（需要额外生成 JSON） -->
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/gs_hindex.json&logo=google-scholar&logoColor=white"/>
```

### 自动更新论文列表

SerpAPI 可以获取论文列表（`articles` 字段），可用于：
- 自动生成论文页面
- 按引用数排序展示
- 显示每篇论文的引用数

需要修改爬虫添加 `num` 参数获取论文：
```python
params = {
    "engine": "google_scholar_author",
    "author_id": scholar_id,
    "api_key": api_key,
    "num": 100,  # 获取最多100篇论文
}
```

---

## 🔍 查看 API 额度

1. 登录 https://serpapi.com/manage-api-key
2. 查看 **Searches this month** 和 **Searches left**

---

## ⚙️ 调整更新频率

修改 `.github/workflows/google-scholar-stats.yml`：

```yaml
# 每天更新（约30次/月，仍在免费额度内）
schedule:
  - cron: '0 0 * * *'

# 每周一次（约4次/月）
schedule:
  - cron: '0 0 * * 1'

# 当前配置：每周三次
schedule:
  - cron: '0 0 * * 1'  # 周一
  - cron: '0 0 * * 3'  # 周三
  - cron: '0 0 * * 5'  # 周五
```

---

## 🆘 故障排查

| 问题 | 解决方案 |
|------|----------|
| API 请求失败 | 检查 SERPAPI_KEY 是否正确设置 |
| 数据未更新 | 查看 Actions 运行日志 |
| 徽章显示旧数据 | shields.io 有缓存，等待几分钟或加 `?cacheSeconds=3600` |
| 额度用完 | 等待下月重置或升级付费计划 |

---

*如有问题，请查看 GitHub Actions 的运行日志进行排查。*

# 设置 SerpAPI 获取稳定的 Google Scholar 数据

## 为什么需要 SerpAPI？

直接爬取 Google Scholar 容易被封禁，尤其是在 GitHub Actions 环境中。SerpAPI 是一个专业的搜索引擎 API 服务，提供稳定可靠的 Google Scholar 数据访问。

## 优势

- ✅ **稳定可靠**：专业的代理池和反封禁机制
- ✅ **免费额度**：每月 100 次免费请求（足够周 3 次更新）
- ✅ **结构化数据**：返回干净的 JSON 格式
- ✅ **快速响应**：通常 1-2 秒返回结果

## 设置步骤

### 1. 注册 SerpAPI 账号

访问 [https://serpapi.com/](https://serpapi.com/) 注册免费账号。

### 2. 获取 API Key

登录后，在 Dashboard 页面可以找到你的 API Key。

### 3. 在 GitHub 仓库设置 Secret

1. 进入你的 GitHub 仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 名称填写：`SERPAPI_KEY`
5. 值填写：你的 SerpAPI API Key
6. 点击 **Add secret**

### 4. 测试运行

1. 进入仓库的 **Actions** 页面
2. 选择 **Get Google Scholar Stats** workflow
3. 点击 **Run workflow** 手动触发
4. 查看运行日志，确认数据获取成功

## 免费额度说明

- 新用户：100 次/月免费请求
- 周 3 次更新：每月约 12-13 次请求
- 完全足够使用，无需付费

## 备用方案

如果未设置 `SERPAPI_KEY`，系统会自动使用保底数据（手动更新的引用数）。

## 更新保底数据

如果需要更新保底引用数，修改以下文件中的 `citedby` 值：

- `google_scholar_crawler/serpapi_crawler.py`
- `google_scholar_crawler/robust_crawler.py`
- `google_scholar_crawler/main.py`
- `google_scholar_crawler/mock_crawler.py`
- `gs_data.json`

---

*如有问题，请查看 GitHub Actions 的运行日志进行排查。*


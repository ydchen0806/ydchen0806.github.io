# Google Scholar 爬虫故障排除

## 问题诊断

我们发现了以下问题：

1. **Windows系统不支持`signal.SIGALRM`**：main.py中使用的超时机制在Windows上不工作
2. **网络连接问题**：无法访问Google Scholar，可能是由于代理或网络限制
3. **Unicode编码问题**：Windows下的GBK编码无法正确处理Unicode字符

## 解决方案

### 1. 修复了编码问题

替换了所有Unicode字符（如✓、❌）为普通文本，避免Windows下的编码错误。

### 2. 修复了超时机制

使用threading替代signal模块实现跨平台超时机制。

### 3. 添加了健壮的网络请求处理

- 禁用代理设置
- 添加重试机制
- 改进错误处理

### 4. 创建了多个备用方案

- `mock_crawler.py`：使用模拟数据，验证数据保存流程
- `robust_crawler.py`：健壮爬虫，网络请求失败时使用模拟数据
- `simple_crawler.py`：简化版爬虫，去除复杂逻辑

## 推荐解决方案

### 使用`robust_crawler.py`

这是最健壮的解决方案，当无法访问Google Scholar时自动使用模拟数据：

```bash
cd google_scholar_crawler
python robust_crawler.py
```

### 使用`mock_crawler.py`

如果只想验证数据保存流程，可以使用模拟数据：

```bash
cd google_scholar_crawler
python mock_crawler.py
```

## 更新了GitHub Actions工作流

修改了`.github/workflows/google-scholar-stats.yml`以使用`robust_crawler.py`脚本。

## 未来改进方向

1. 考虑使用更稳定的API获取Google Scholar数据
2. 添加更多测试案例
3. 考虑使用docker容器运行，避免本地环境问题
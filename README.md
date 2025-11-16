# Google Scholar Statistics

This branch contains automatically updated Google Scholar statistics.

## Files

- `gs_data.json`: Complete scholar profile data
- `gs_data_shieldsio.json`: Shields.io badge format data

**Last updated:** $(date -u +'%Y-%m-%d %H:%M:%S UTC')

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

*This data is automatically updated three times per week (Monday, Wednesday, Friday) by GitHub Actions.*

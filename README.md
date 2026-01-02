# Google Scholar Statistics

This branch contains automatically updated Google Scholar statistics.

## Files

- `gs_data.json`: Complete scholar profile data
- `gs_data_shieldsio.json`: Citations badge (Shields.io format)
- `gs_hindex.json`: H-Index badge
- `gs_i10index.json`: I10-Index badge
- `citation_trend.svg`: Citation trend chart
- `first_author_papers.json`: First-author papers list
- `high_cited_papers.json`: High-cited papers (>=50)
- `all_papers.json`: All papers with details
- `auto_publications.md`: Auto-generated publication list

**Last updated:** 2026-01-02 01:57:57 UTC

## Usage

### Citation Badge
```markdown
![Citations](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)
```

### Citation Trend Chart
```markdown
![Citation Trend](https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/citation_trend.svg)
```

---
*Updated 3x weekly (Mon/Wed/Fri) via GitHub Actions | Source: SerpAPI*

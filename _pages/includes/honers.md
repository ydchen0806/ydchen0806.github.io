# 🥇 Honors and Awards

<style>
/* ===== Honors Section - Collapsible Categories ===== */
#honors-awards details {
  margin-bottom: 1em;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8e8e8;
  transition: box-shadow 0.3s;
}
#honors-awards details:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#honors-awards details[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}

#honors-awards summary {
  padding: 0.9em 1.2em;
  cursor: pointer;
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  background: linear-gradient(135deg, #f8f9fa 0%, #eef1f5 100%);
  user-select: none;
  display: flex;
  align-items: center;
  gap: 0.5em;
  list-style: none;
  transition: background 0.2s;
}
#honors-awards summary::-webkit-details-marker { display: none; }
#honors-awards summary::before {
  content: "▶";
  font-size: 0.7em;
  color: #2196F3;
  transition: transform 0.25s;
  display: inline-block;
}
#honors-awards details[open] > summary::before {
  transform: rotate(90deg);
}
#honors-awards summary:hover {
  background: linear-gradient(135deg, #eef1f5 0%, #e3e8ef 100%);
}

#honors-awards .badge-count {
  font-size: 0.75em;
  font-weight: 500;
  color: #fff;
  background: #2196F3;
  padding: 2px 9px;
  border-radius: 12px;
  margin-left: auto;
}

#honors-awards .award-list {
  list-style: none;
  padding: 0;
  margin: 0;
  counter-reset: award-counter;
}
#honors-awards .award-list > li {
  counter-increment: award-counter;
  padding: 1em 1.3em;
  border-bottom: 1px solid #f0f0f0;
  position: relative;
  transition: background 0.15s;
}
#honors-awards .award-list > li:last-child { border-bottom: none; }
#honors-awards .award-list > li:hover { background: #fafbfc; }
#honors-awards .award-list > li::before {
  content: "[" counter(award-counter) "]";
  font-weight: bold;
  color: #2196F3;
  margin-right: 0.5em;
  font-size: 0.95em;
}

#honors-awards .award-list > li > strong {
  font-size: 1.02em;
  color: #1a1a1a;
}

#honors-awards .award-list > li > ul {
  margin-top: 0.5em;
  margin-bottom: 0;
  padding-left: 1.5em;
  list-style-type: none;
}
#honors-awards .award-list > li > ul > li {
  margin-bottom: 0.3em;
  line-height: 1.6;
  color: #555;
  position: relative;
  padding-left: 0;
}
#honors-awards .award-list > li > ul > li::before {
  content: "▪ ";
  color: #2196F3;
  font-weight: bold;
  margin-right: 0.3em;
}

#honors-awards a {
  color: #2196F3;
  text-decoration: none;
  transition: all 0.2s;
  padding: 1px 4px;
  border-radius: 4px;
  display: inline;
}
#honors-awards a:hover {
  color: #1976D2;
  background: #e3f2fd;
}
#honors-awards .award-date {
  color: #666;
  font-style: italic;
  margin-left: 0.5em;
  font-size: 0.92em;
}
#honors-awards img[src*="shields.io"] {
  vertical-align: middle;
  margin-left: 4px;
}
</style>

<div id="honors-awards">

<!-- ====== National Awards & Research Funding ====== -->
<details open>
<summary>🏅 National Awards & Research Funding <span class="badge-count">3</span></summary>
<ul class="award-list">

<li><strong><a href="/docs/国自然.png">National Natural Science Foundation of China (NSFC) PhD Program</a></strong> <span class="award-date">(December 2024)</span>
  <ul>
    <li><strong>Role:</strong> Principal Investigator</li>
    <li><strong>Achievement:</strong> Sole awardee in Information Science, Anhui Province</li>
    <li><strong>Description:</strong> Prestigious national research funding program for doctoral students</li>
  </ul>
</li>

<li><strong><a href="/docs/国奖证书研究生.png">National Graduate Scholarship (国家奖学金)</a></strong> <span class="award-date">(December 2022)</span>
  <ul>
    <li><strong>Achievement:</strong> National award for academic performance and research contributions (Top 1%)</li>
    <li><strong>Reference:</strong> 🔗 <a href="https://iat.ustc.edu.cn/iat/x198/20221017/5920.html">Official Announcement</a></li>
  </ul>
</li>

<li><strong><a href="https://www.overleaf.com/read/hjrjffjfthgc#d8acfd">Interdisciplinary Contest in Modeling (ICM), Outstanding Winner</a></strong> <span class="award-date">(May 2024)</span>
  <ul>
    <li><strong>Competition:</strong> International mathematical modeling competition organized by COMAP</li>
    <li><strong>Ranking:</strong> Top 0.17% of 10,388 participating teams worldwide</li>
    <li><strong>Resources:</strong> 📝 <a href="https://github.com/ydchen0806/24ICM_E_O_Award_Paper_code">Paper &amp; Code</a> <a href="https://github.com/ydchen0806/24ICM_E_O_Award_Paper_code"><img src="https://img.shields.io/github/stars/ydchen0806/24ICM_E_O_Award_Paper_code?style=social&amp;label=Stars" alt="Stars"></a></li>
  </ul>
</li>

</ul>
</details>

<!-- ====== Academic Honors & Scholarships ====== -->
<details open>
<summary>🎓 Academic Honors & Scholarships <span class="badge-count">2</span></summary>
<ul class="award-list">

<li><strong><a href="/docs/学术之星奖杯.jpg">Xiamen University Academic Star (学术之星)</a></strong> <span class="award-date">(December 2021)</span>
  <ul>
    <li><strong>Achievement:</strong> Sole undergraduate awardee university-wide</li>
    <li><strong>Recognition:</strong> Outstanding academic achievements and research excellence</li>
    <li><strong>Media:</strong> 🔗 <a href="https://xaxq.xmu.edu.cn/info/1032/10951.htm">University News</a> | <a href="https://cee.xmu.edu.cn/info/1045/7524.htm">Feature Report</a></li>
  </ul>
</li>

<li><strong><a href="/docs/增华奖学金.jpg">Zenghua Scholarship (增华奖学金)</a></strong> <span class="award-date">(January 2026)</span>
  <ul>
    <li><strong>Level:</strong> University-level scholarship, USTC</li>
    <li><strong>Achievement:</strong> Awarded for outstanding academic performance and research contributions</li>
  </ul>
</li>

</ul>
</details>

<!-- ====== Competition Awards ====== -->
<details>
<summary>🏆 Competition Awards <span class="badge-count">5</span></summary>
<ul class="award-list">

<li><strong><a href="/docs/数竞决赛.png">National Undergraduate Mathematics Competition (Non-Major Category), Second Prize</a></strong> <span class="award-date">(May 2021)</span>
  <ul>
    <li><strong>Competition:</strong> National finals organized by the Chinese Mathematical Society</li>
    <li><strong>Progress:</strong> Advanced from provincial first place</li>
    <li><strong>Reference:</strong> 🔗 <a href="https://math.xmu.edu.cn/info/1017/10611.htm">Competition News</a></li>
  </ul>
</li>

<li><strong><a href="/docs/数竞.png">National Undergraduate Mathematics Competition (Non-Major Category), First Prize</a></strong> <span class="award-date">(November 2020)</span>
  <ul>
    <li><strong>Competition:</strong> High-level national mathematics competition for undergraduate students</li>
    <li><strong>Ranking:</strong> Provincial First Place, Fujian Province</li>
  </ul>
</li>

<li><strong><a href="/docs/景润杯奖状.png">"Jingrun Cup" Mathematics Competition (Professional Category), First Prize</a></strong> <span class="award-date">(September 2021)</span>
  <ul>
    <li><strong>Level:</strong> Campus-level competition named after renowned mathematician Chen Jingrun</li>
    <li><strong>Ranking:</strong> University First Place</li>
    <li><strong>Reference:</strong> 🔗 <a href="https://math.xmu.edu.cn/info/1024/11221.htm">Competition News</a></li>
  </ul>
</li>

<li><strong><a href="/docs/挑战杯.png">"Challenge Cup" National Undergraduate Academic Science and Technology Competition, First Prize</a></strong> <span class="award-date">(May 2021)</span>
  <ul>
    <li><strong>Level:</strong> Provincial level competition</li>
    <li><strong>Region:</strong> Fujian Province</li>
  </ul>
</li>

<li><strong><a href="/docs/互联网+.png">"Internet+" Innovation and Entrepreneurship Competition, Gold Medal</a></strong> <span class="award-date">(August 2021)</span>
  <ul>
    <li><strong>Level:</strong> Provincial level competition</li>
    <li><strong>Region:</strong> Fujian Province</li>
  </ul>
</li>

</ul>
</details>

</div>

# 🥇 Honors and Awards

<style>
/* 重置并初始化Honors and Awards的计数器 */
#honors-awards {
  counter-reset: award-counter;
}

/* Honors and Awards自动编号 - 内联显示 */
#honors-awards > ul > li {
  counter-increment: award-counter;
  list-style-type: none;
  position: relative;
  margin-left: 0;
  margin-bottom: 2em;
  padding: 1.2em;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #2196F3;
}

#honors-awards > ul > li::before {
  content: "[" counter(award-counter) "] ";
  font-weight: bold;
  color: #2196F3;
  margin-right: 0.5em;
  display: inline;
  font-size: 1.1em;
}

/* 奖项标题样式 */
#honors-awards > ul > li > strong {
  font-size: 1.05em;
  color: #1a1a1a;
}

/* 子列表样式 - 移除默认的 list-style */
#honors-awards > ul > li > ul {
  margin-top: 0.8em;
  margin-bottom: 0;
  padding-left: 1.5em;
  list-style-type: none;
}

#honors-awards > ul > li > ul > li {
  margin-bottom: 0.5em;
  line-height: 1.6;
  color: #555;
  position: relative;
  padding-left: 0;
}

#honors-awards > ul > li > ul > li::before {
  content: "▪ ";
  color: #2196F3;
  font-weight: bold;
  margin-right: 0.5em;
}

/* 链接样式优化 */
#honors-awards a {
  color: #2196F3;
  text-decoration: none;
  transition: all 0.2s;
  padding: 2px 6px;
  border-radius: 4px;
  display: inline-block;
  margin: 0 4px;
}

#honors-awards a:hover {
  color: #1976D2;
  background: #e3f2fd;
}

/* 时间标签样式 */
#honors-awards .award-date {
  color: #666;
  font-style: italic;
  margin-left: 0.5em;
}

/* GitHub badge 样式 */
#honors-awards img[src*="shields.io"] {
  vertical-align: middle;
  margin-left: 4px;
}
</style>

<div id="honors-awards" markdown="1">

- **🎓 [National Natural Science Foundation of China (NSFC) PhD Program](/docs/国自然.png)** <span class="award-date">(December 2024)</span>
  - **Role:** Principal Investigator
  - **Achievement:** Sole awardee in Information Science, Anhui Province
  - **Description:** Prestigious national research funding program for doctoral students

- **🏆 [Interdisciplinary Contest in Modeling (ICM), Outstanding Winner](https://www.overleaf.com/read/hjrjffjfthgc#d8acfd)** <span class="award-date">(May 2024)</span>
  - **Competition:** International mathematical modeling competition organized by COMAP
  - **Ranking:** Top 0.17% of 10,388 participating teams worldwide
  - **Resources:** 📝 [Paper & Code](https://github.com/ydchen0806/24ICM_E_O_Award_Paper_code) [![](https://img.shields.io/github/stars/ydchen0806/24ICM_E_O_Award_Paper_code?style=social&label=Stars)](https://github.com/ydchen0806/24ICM_E_O_Award_Paper_code)

- **🎓 [National Graduate Scholarship](/docs/国奖证书研究生.png)** <span class="award-date">(December 2022)</span>
  - **Achievement:** National award for academic performance and research contributions (Top 1%)
  - **Reference:** 🔗 [Official Announcement](https://iat.ustc.edu.cn/iat/x198/20221017/5920.html)

- **🎓 [Xiamen University Academic Star](/docs/学术之星奖杯.jpg)** <span class="award-date">(December 2021)</span>
  - **Achievement:** Sole undergraduate awardee university-wide
  - **Recognition:** Outstanding academic achievements and research excellence
  - **Media:** 🔗 [University News](https://xaxq.xmu.edu.cn/info/1032/10951.htm) | [Feature Report](https://cee.xmu.edu.cn/info/1045/7524.htm)

- **🏆 ["Jingrun Cup" Mathematics Competition (Professional Category), First Prize](/docs/景润杯奖状.png)** <span class="award-date">(September 2021)</span>
  - **Level:** Campus-level competition named after renowned mathematician Chen Jingrun
  - **Ranking:** University First Place
  - **Reference:** 🔗 [Competition News](https://math.xmu.edu.cn/info/1024/11221.htm)

- **🏆 ["Internet+" Innovation and Entrepreneurship Competition, Gold Medal](/docs/互联网+.png)** <span class="award-date">(August 2021)</span>
  - **Level:** Provincial level competition
  - **Region:** Fujian Province

- **🏆 [National Undergraduate Mathematics Competition (Non-Major Category), Second Prize](/docs/数竞决赛.png)** <span class="award-date">(May 2021)</span>
  - **Competition:** National finals organized by the Chinese Mathematical Society
  - **Progress:** Advanced from provincial first place
  - **Reference:** 🔗 [Competition News](https://math.xmu.edu.cn/info/1017/10611.htm)

- **🏆 ["Challenge Cup" National Undergraduate Academic Science and Technology Competition, First Prize](/docs/挑战杯.png)** <span class="award-date">(May 2021)</span>
  - **Level:** Provincial level competition
  - **Region:** Fujian Province

- **🏆 [National Undergraduate Mathematics Competition (Non-Major Category), First Prize](/docs/数竞.png)** <span class="award-date">(November 2020)</span>
  - **Competition:** High-level national mathematics competition for undergraduate students
  - **Ranking:** Provincial First Place, Fujian Province

</div>
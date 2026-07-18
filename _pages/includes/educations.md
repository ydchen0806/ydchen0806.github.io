# 📖 Education

<style>
#education-section details {
  margin-bottom: 1em;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8e8e8;
  transition: box-shadow 0.3s;
}
#education-section details:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#education-section details[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#education-section summary {
  padding: 0.9em 1.2em;
  cursor: pointer;
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  background: linear-gradient(135deg, #f0faf0 0%, #e8f5e9 100%);
  user-select: none;
  display: flex;
  align-items: center;
  gap: 0.5em;
  list-style: none;
  transition: background 0.2s;
}
#education-section summary::-webkit-details-marker { display: none; }
#education-section summary::before {
  content: "▶";
  font-size: 0.7em;
  color: #4CAF50;
  transition: transform 0.25s;
  display: inline-block;
}
#education-section details[open] > summary::before {
  transform: rotate(90deg);
}
#education-section summary:hover {
  background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
}

#education-section .badge-count {
  font-size: 0.75em;
  font-weight: 500;
  color: #fff;
  background: #4CAF50;
  padding: 2px 9px;
  border-radius: 12px;
  margin-left: auto;
}

#education-section .edu-item {
  padding: 1.2em 1.5em;
  border-bottom: 1px solid #f0f0f0;
  transition: background 0.15s;
}
#education-section .edu-item:last-child { border-bottom: none; }
#education-section .edu-item:hover { background: #fafff8; }

#education-section .school-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 0.5em;
}
#education-section .school-header img {
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
#education-section .school-name {
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
}
#education-section .degree-info {
  color: #555;
  font-size: 0.95em;
  margin: 0.3em 0;
  font-style: italic;
}
#education-section .location {
  color: #666;
  font-size: 0.9em;
  margin: 0;
}

#education-section .edu-details {
  margin-top: 0.8em;
  padding-left: 0;
  list-style-type: none;
}
#education-section .edu-details > li {
  margin-bottom: 0.5em;
  line-height: 1.7;
  color: #444;
  padding-left: 1.2em;
  position: relative;
}
#education-section .edu-details > li::before {
  content: "•";
  color: #4CAF50;
  font-weight: bold;
  position: absolute;
  left: 0;
}

#education-section a {
  color: #2196F3;
  text-decoration: none;
  transition: color 0.2s;
}
#education-section a:hover {
  color: #1976D2;
  text-decoration: underline;
}
</style>

<div id="education-section">

<details open>
<summary>🎓 Academic Background <span class="badge-count">3</span></summary>

<div class="edu-item">
<div class="school-header">
  <img src="/images/ustc_logo.png" alt="USTC Logo" width="60"/>
  <div>
    <p class="school-name">University of Science and Technology of China & Shanghai AI Lab</p>
    <p class="degree-info">Ph.D. in Information and Communication Engineering (Expected 2027)</p>
    <p class="location">📍 Hefei & Shanghai · Sept 2024 - Present</p>
  </div>
</div>
<ul class="edu-details">
  <li>Research focus: Machine Learning Theory, Self-Supervised Pretraining, Multimodal Large Models, Image Coding & Compression</li>
  <li>Working with <a href="https://scholar.google.com/citations?user=5bInRDEAAAAJ&hl=en">Prof. Feng Wu</a> (CAE Academician, IEEE Fellow) and <a href="https://scholar.google.com/citations?user=Snl0HPEAAAAJ&hl=en&oi=ao">Prof. Zhiwei Xiong</a></li>
  <li>Co-supervised by <a href="https://scholar.google.com/citations?user=qpBtpGsAAAAJ&hl=en">Prof. Xiaoou Tang</a> (IEEE Fellow) at Shanghai AI Lab</li>
  <li>Selected coursework: Algorithm Design and Analysis, Statistical Learning, Deep Learning, Reinforcement Learning</li>
  <li>Principal Investigator for NSFC Ph.D. Project (2024)</li>
</ul>
</div>

<div class="edu-item">
<div class="school-header">
  <img src="/images/ustc_logo.png" alt="USTC Logo" width="60"/>
  <div>
    <p class="school-name">University of Science and Technology of China</p>
    <p class="degree-info">M.S. in Computer Technology</p>
    <p class="location">📍 Hefei · Sept 2022 - July 2024</p>
  </div>
</div>
<ul class="edu-details">
  <li>Recipient of National Graduate Scholarship (2022)</li>
</ul>
</div>

<div class="edu-item">
<div class="school-header">
  <img src="/images/xmu_logo.jpeg" alt="XMU Logo" width="60"/>
  <div>
    <p class="school-name">Xiamen University</p>
    <p class="degree-info">B.S. in Environmental Ecological Engineering & Economics (Dual Degree)</p>
    <p class="location">📍 Xiamen · Sept 2018 - July 2022</p>
  </div>
</div>
<ul class="edu-details">
  <li>Academic ranking: <a href="/docs/排名第一.png">1st/31 overall</a></li>
  <li>Xiamen University Academic Star (2021), CDA Level 1 Certification (2022), <a href="https://www.kaggle.com/yindachen">Kaggle Expert</a></li>
  <li>Research advisor: <a href="https://scholar.google.com/citations?user=l1GMXf4AAAAJ&hl=en&oi=ao">Prof. Yuanye Zhang</a></li>
</ul>
</div>

</details>

</div>

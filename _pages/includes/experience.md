# 💼 Professional Experience

<style>
#work-section details {
  margin-bottom: 1em;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8e8e8;
  transition: box-shadow 0.3s;
}
#work-section details:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#work-section details[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}

#work-section summary {
  padding: 0.9em 1.2em;
  cursor: pointer;
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  background: linear-gradient(135deg, #fff8f0 0%, #fff3e6 100%);
  user-select: none;
  display: flex;
  align-items: center;
  gap: 0.5em;
  list-style: none;
  transition: background 0.2s;
}
#work-section summary::-webkit-details-marker { display: none; }
#work-section summary::before {
  content: "▶";
  font-size: 0.7em;
  color: #FF9800;
  transition: transform 0.25s;
  display: inline-block;
}
#work-section details[open] > summary::before {
  transform: rotate(90deg);
}
#work-section summary:hover {
  background: linear-gradient(135deg, #fff3e6 0%, #ffe8cc 100%);
}

#work-section .badge-count {
  font-size: 0.75em;
  font-weight: 500;
  color: #fff;
  background: #FF9800;
  padding: 2px 9px;
  border-radius: 12px;
  margin-left: auto;
}

#work-section .exp-item {
  padding: 1.2em 1.5em;
  border-bottom: 1px solid #f0f0f0;
  transition: background 0.15s;
}
#work-section .exp-item:last-child { border-bottom: none; }
#work-section .exp-item:hover { background: #fffcf8; }

#work-section .company-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 0.5em;
}
#work-section .company-header img {
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
#work-section .company-name {
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  margin: 0;
}
#work-section .position-info {
  color: #555;
  font-size: 0.95em;
  margin: 0.3em 0;
  font-style: italic;
}
#work-section .location {
  color: #666;
  font-size: 0.9em;
  margin: 0;
}

#work-section .exp-details {
  margin-top: 0.8em;
  padding-left: 0;
  list-style-type: none;
}
#work-section .exp-details > li {
  margin-bottom: 0.5em;
  line-height: 1.7;
  color: #444;
  padding-left: 1.2em;
  position: relative;
}
#work-section .exp-details > li::before {
  content: "•";
  color: #FF9800;
  font-weight: bold;
  position: absolute;
  left: 0;
}

#work-section a {
  color: #2196F3;
  text-decoration: none;
  transition: color 0.2s;
}
#work-section a:hover {
  color: #1976D2;
  text-decoration: underline;
}
</style>

<div id="work-section">

<details open>
<summary>🏢 Industry Experience <span class="badge-count">4</span></summary>

<div class="exp-item">
<div class="company-header">
  <img src="/images/X-humanoid.png" alt="X-Humanoid logo" width="144" loading="lazy"/>
  <div>
    <p class="company-name"><a href="https://www.x-humanoid.com/">Beijing Innovation Center of Humanoid Robotics (X-Humanoid)</a></p>
    <p class="position-info">Core Member, Embodied Intelligence World Model Team</p>
    <p class="location">📍 Beijing · Dec 2025 - Present</p>
  </div>
</div>
<ul class="exp-details">
  <li>Developing unified embodied models that connect scene and instruction understanding, future prediction, and robot action.</li>
  <li>Core contributor to <a href="https://arxiv.org/abs/2605.15153">Pelican-Unified 1.0</a>, focusing on unified vision-language modeling and action capability.</li>
  <li>Contributed to <a href="https://arxiv.org/abs/2607.06655">Pelican-VLA 0.5</a>, studying bottleneck representations for task-relevant perception and manipulation across scenes and embodiments.</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/ubiquant-logo.png" alt="Ubiquant logo" width="144" loading="lazy"/>
  <div>
    <p class="company-name"><a href="https://www.ubiquant.com/">Ubiquant (九坤投资)</a></p>
    <p class="position-info">Research Intern, Quantitative Research and Foundation Models</p>
    <p class="location">📍 Beijing · May 2026 - Oct 2026</p>
  </div>
</div>
<ul class="exp-details">
  <li>Worked on quantitative research and language models for factor mining and data-driven decisions, with experience in thousand-GPU-scale training.</li>
  <li>Contributor and co-author of <a href="https://arxiv.org/abs/2610.30949" title="Q1: Advancing Foundation Capabilities for Agentic CLI Systems">Q1</a>, an agentic foundation model for CLI interaction, coding, and multi-step tool use (October 2026 technical report).</li>
  <li>Core contributor to <a href="https://arxiv.org/abs/2610.11451" title="SAIL: Scientific Agentic Intelligence via a Science-Aware Loop">SAIL</a>, a scientific-agent model for literature research, scientific coding, and multi-step research workflows (October 2026).</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/tencent.png" alt="Tencent logo" width="144" loading="lazy"/>
  <div>
    <p class="company-name"><a href="https://ieg.tencent.com/">Tencent Interactive Entertainment Group (IEG)</a></p>
    <p class="position-info">Qingyun Program Intern</p>
    <p class="location">📍 Shanghai · Aug 2025 - Dec 2025</p>
  </div>
</div>
<ul class="exp-details">
  <li>Developed multimodal scene understanding and game world models for gameplay analysis and content generation.</li>
  <li>Worked on <em>Honor of Kings – Lingbao</em>, including text-to-speech and live match commentary, with <a href="https://scholar.google.com/citations?user=oxNIbCUAAAAJ&hl=en&oi=ao">Dr. Liang Du</a> and <a href="https://scholar.google.com/citations?hl=en&user=ibNed18AAAAJ">Dr. Wentao Yao</a>.</li>
  <li>Contributed to <a href="https://main-vla.github.io/">MAIN-VLA</a>, a world model for <em>Game for Peace (和平精英)</em> that connects intentions, game states, and actions.</li>
  <li>Researched router-free MoE-LoRA adaptation through linear aggregation and merging of low-rank expert updates.</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/301.png" alt="PLA General Hospital logo" width="60" loading="lazy"/>
  <div>
    <p class="company-name"><a href="/docs/301医院.png">PLA General Hospital (301 Hospital)</a></p>
    <p class="position-info">Research Intern, Data Compression Group</p>
    <p class="location">📍 Beijing · Sept 2023 - Feb 2024</p>
  </div>
</div>
<ul class="exp-details">
  <li>Collaborated with <a href="https://scholar.google.com/citations?user=CHAajY4AAAAJ&hl=en&oi=ao">Prof. Qionghai Dai</a>'s team on medical image compression, designing methods adapted to different imaging modalities.</li>
</ul>
</div>

</details>

<details open>
<summary>🎓 Academic Experience <span class="badge-count">3</span></summary>

<div class="exp-item">
<div class="company-header">
  <img src="/images/IC.png" alt="Imperial College London logo" width="60" loading="lazy"/>
  <div>
    <p class="company-name"><a href="/docs/IC_letter_Yinda.png">Imperial College London</a></p>
    <p class="position-info">Research Intern, Data Science Institute</p>
    <p class="location">📍 London (remote) · Nov 2022 - Aug 2023</p>
  </div>
</div>
<ul class="exp-details">
  <li>Worked with <a href="https://scholar.google.com/citations?user=oxy2ZQoAAAAJ&hl=en">Dr. Rossella Arcucci</a> and <a href="https://scholar.google.com/citations?user=HED_458AAAAJ&hl=en&oi=sra">Dr. Che Liu</a> on multimodal pretraining and image-text contrastive learning for medical images.</li>
  <li>This collaboration led to work including GTGM and BIMCV-R; see <a href="#-publications">selected publications</a>.</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/xmu_logo.jpeg" alt="Xiamen University logo" width="60" loading="lazy"/>
  <div>
    <p class="company-name"><a href="/docs/wiserclub.png">Xiamen University WISER Club</a></p>
    <p class="position-info">Academic Community Member, Data Mining Group</p>
    <p class="location">📍 Xiamen · Aug 2021 - July 2022</p>
  </div>
</div>
<ul class="exp-details">
  <li>Designed and delivered data mining courses on clustering and Transformers, and mentored undergraduate machine learning projects. <a href="https://mp.weixin.qq.com/s/sqF3p69kdTF8KmdRhfEEMw">Campus feature</a>.</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/xmu_logo.jpeg" alt="Xiamen University logo" width="60" loading="lazy"/>
  <div>
    <p class="company-name"><a href="/docs/wise研助.png">Wang Yanan Institute for Studies in Economics, Xiamen University</a></p>
    <p class="position-info">Research Assistant, Econometrics</p>
    <p class="location">📍 Xiamen · Aug 2020 - Dec 2021</p>
  </div>
</div>
<ul class="exp-details">
  <li>Assisted Jiong Zhu with land economic statistics research, using satellite imagery and visual features to study homesteads and land-use change.</li>
</ul>
</div>

</details>

</div>

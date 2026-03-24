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
<summary>🏢 Industry Experience <span class="badge-count">3</span></summary>

<div class="exp-item">
<div class="company-header">
  <img src="/images/X-humanoid.png" alt="Beijing Humanoid Robot Innovation Center Logo" width="144"/>
  <div>
    <p class="company-name"><a href="https://www.x-humanoid.com/">Beijing Humanoid Robot Innovation Center (UBTECH Robotics)</a></p>
    <p class="position-info">Core Member, Embodied Intelligence World Model Algorithm Team</p>
    <p class="location">📍 Beijing · Dec 2025 - Present</p>
  </div>
</div>
<ul class="exp-details">
  <li>Conducting research on embodied intelligence world models</li>
  <li>Developing advanced algorithms for humanoid robot perception and decision-making</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/tencent.png" alt="Tencent Logo" width="144"/>
  <div>
    <p class="company-name"><a href="https://ieg.tencent.com/">Tencent Interactive Entertainment Group (IEG)</a></p>
    <p class="position-info">Qingyun Program Intern</p>
    <p class="location">📍 Shanghai · Aug 2025 - Dec 2025</p>
  </div>
</div>
<ul class="exp-details">
  <li>Developing TTS (Text-to-Speech) systems and multimodal scene understanding for <em>Honor of Kings – Lingbao</em> and <em>League of Legends</em> highlight commentary</li>
  <li>Supervised by <a href="https://scholar.google.com/citations?user=oxNIbCUAAAAJ&hl=en&oi=ao">Dr. Liang Du</a> and <a href="https://scholar.google.com/citations?hl=en&user=ibNed18AAAAJ">Dr. Wentao Yao</a></li>
  <li>Designed TTS models for generating game commentary and character voiceovers, exploring generation-understanding synergy</li>
  <li>Developed multimodal algorithms to analyze game video content and automatically generate contextual commentary scripts</li>
  <li>Co-developed <a href="https://main-vla.github.io/">MAIN-VLA</a>: A game world model for <em>Game for Peace (和平精英)</em>, modeling abstraction of intention and environment for Visual-Language-Action in complex gaming scenarios</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/301.png" alt="301 Hospital Logo" width="60"/>
  <div>
    <p class="company-name"><a href="/docs/301医院.png">Chinese PLA General Hospital (301 Hospital)</a></p>
    <p class="position-info">Research Intern, Data Compression Group</p>
    <p class="location">📍 Beijing · Sept 2023 - Feb 2024</p>
  </div>
</div>
<ul class="exp-details">
  <li>Collaborated with <a href="https://scholar.google.com/citations?user=CHAajY4AAAAJ&hl=en&oi=ao">Prof. Qionghai Dai</a> (CAE Academician, IEEE Fellow)'s team on efficient data compression research</li>
  <li>Designed image-specific compression algorithms for various data modalities</li>
  <li>Achieved 35% improvement in compression efficiency</li>
</ul>
</div>

</details>

<details open>
<summary>🎓 Academic Experience <span class="badge-count">3</span></summary>

<div class="exp-item">
<div class="company-header">
  <img src="/images/IC.png" alt="Imperial College Logo" width="60"/>
  <div>
    <p class="company-name"><a href="/docs/IC_letter_Yinda.png">Imperial College London</a></p>
    <p class="position-info">Research Intern, Data Science Institute</p>
    <p class="location">📍 London (Remote) · Nov 2022 - Aug 2023</p>
  </div>
</div>
<ul class="exp-details">
  <li>Collaborated with <a href="https://scholar.google.com/citations?user=oxy2ZQoAAAAJ&hl=en">Dr. Rossella Arcucci</a> and <a href="https://scholar.google.com/citations?user=HED_458AAAAJ&hl=en&oi=sra">Dr. Che Liu</a> on multimodal pretraining research</li>
  <li>Developed image-text contrastive learning framework achieving 93.5% accuracy on classification tasks</li>
  <li>Submitted one journal paper</li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/xmu_logo.jpeg" alt="XMU Logo" width="60"/>
  <div>
    <p class="company-name"><a href="/docs/wiserclub.png">Xiamen University WISER Club</a></p>
    <p class="position-info">Insider, Data Mining Group</p>
    <p class="location">📍 Xiamen · Aug 2021 - July 2022</p>
  </div>
</div>
<ul class="exp-details">
  <li>Designed and led data mining courses, delivering lectures on clustering and Transformer architectures</li>
  <li>Mentored 20 undergraduate students in machine learning projects and organized 2 campus-wide competitions</li>
  <li><a href="https://mp.weixin.qq.com/s/sqF3p69kdTF8KmdRhfEEMw">Media coverage</a></li>
</ul>
</div>

<div class="exp-item">
<div class="company-header">
  <img src="/images/xmu_logo.jpeg" alt="XMU Logo" width="60"/>
  <div>
    <p class="company-name"><a href="/docs/wise研助.png">Wang Yanan Institute for Studies in Economics, Xiamen University</a></p>
    <p class="position-info">Research Assistant, Econometrics</p>
    <p class="location">📍 Xiamen · Aug 2020 - Dec 2021</p>
  </div>
</div>
<ul class="exp-details">
  <li>Assisted Associate Prof. Jiong Zhu in national land economic statistics research</li>
  <li>Conducted visual feature extraction for homestead information and land use analysis</li>
  <li>Developed satellite imagery analysis tools achieving 85% accuracy in identifying land use changes</li>
</ul>
</div>

</details>

</div>

# 💬 Talks, Skills & Service

<style>
#others-section details {
  margin-bottom: 1em;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8e8e8;
  transition: box-shadow 0.3s;
}
#others-section details:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#others-section details[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#others-section summary {
  padding: 0.9em 1.2em;
  cursor: pointer;
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  background: linear-gradient(135deg, #f0f7ff 0%, #e8f0fe 100%);
  user-select: none;
  display: flex;
  align-items: center;
  gap: 0.5em;
  list-style: none;
  transition: background 0.2s;
}
#others-section summary::-webkit-details-marker { display: none; }
#others-section summary::before {
  content: "▶";
  font-size: 0.7em;
  color: #1976D2;
  transition: transform 0.25s;
  display: inline-block;
}
#others-section details[open] > summary::before {
  transform: rotate(90deg);
}
#others-section summary:hover {
  background: linear-gradient(135deg, #e8f0fe 0%, #d6e4f0 100%);
}

#others-section .badge-count {
  font-size: 0.75em;
  font-weight: 500;
  color: #fff;
  background: #1976D2;
  padding: 2px 9px;
  border-radius: 12px;
  margin-left: auto;
}

#others-section .section-content {
  padding: 1.2em 1.5em;
}

/* Talks timeline */
#others-section .talk-item {
  display: flex;
  gap: 1em;
  padding: 0.8em 0;
  border-bottom: 1px solid #f0f0f0;
}
#others-section .talk-item:last-child { border-bottom: none; }
#others-section .talk-date {
  flex-shrink: 0;
  font-size: 0.82em;
  font-weight: 600;
  color: #fff;
  background: #1976D2;
  padding: 3px 10px;
  border-radius: 4px;
  height: fit-content;
  margin-top: 2px;
}
#others-section .talk-text {
  color: #333;
  line-height: 1.6;
}
#others-section .talk-text strong {
  color: #1a1a1a;
}
#others-section .talk-venue {
  display: block;
  font-size: 0.88em;
  color: #666;
  margin-top: 2px;
}

/* Skill pills */
#others-section .skill-group {
  margin-bottom: 1em;
}
#others-section .skill-group-title {
  font-weight: 600;
  font-size: 0.92em;
  color: #555;
  margin-bottom: 0.5em;
  display: flex;
  align-items: center;
  gap: 0.4em;
}
#others-section .skill-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4em;
}
#others-section .skill-pill {
  display: inline-block;
  padding: 4px 12px;
  font-size: 0.82em;
  font-weight: 500;
  border-radius: 20px;
  transition: all 0.2s;
  cursor: default;
}
#others-section .skill-pill:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
#others-section .pill-lang { background: #E3F2FD; color: #1565C0; }
#others-section .pill-ml { background: #F3E5F5; color: #7B1FA2; }
#others-section .pill-data { background: #E8F5E9; color: #2E7D32; }
#others-section .pill-web { background: #FFF3E0; color: #E65100; }
#others-section .pill-tool { background: #ECEFF1; color: #37474F; }
#others-section .pill-nlang { background: #FCE4EC; color: #C62828; }

/* Reviewer badges */
#others-section .reviewer-category {
  margin-bottom: 0.8em;
}
#others-section .reviewer-label {
  font-weight: 600;
  font-size: 0.9em;
  color: #555;
  margin-bottom: 0.4em;
}
#others-section .venue-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4em;
}
#others-section .venue-badge {
  display: inline-block;
  padding: 3px 10px;
  font-size: 0.8em;
  font-weight: 600;
  border-radius: 4px;
  background: #1976D2;
  color: #fff;
  transition: all 0.15s;
  cursor: default;
}
#others-section .venue-badge:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(25, 118, 210, 0.3);
}
#others-section .venue-badge.journal {
  background: #7B1FA2;
}
</style>

<div id="others-section">

<details open>
<summary>🎤 Invited Talks <span class="badge-count">2</span></summary>
<div class="section-content">

<div class="talk-item">
  <span class="talk-date">2023.03</span>
  <div class="talk-text">
    <strong>Vision-Language Pretraining Using Generative Methods</strong>
    <span class="talk-venue">JD AI Team — Talk on leveraging generative techniques in VLMs for pretraining</span>
  </div>
</div>

<div class="talk-item">
  <span class="talk-date">2021.08</span>
  <div class="talk-text">
    <strong>Data Mining Course — Clustering and Feature Extraction</strong>
    <span class="talk-venue">Xiamen University, WISER Club — Designed and delivered data mining lectures</span>
  </div>
</div>

</div>
</details>

<details open>
<summary>💻 Technical Skills</summary>
<div class="section-content">

<div class="skill-group">
  <div class="skill-group-title">💻 Programming</div>
  <div class="skill-pills">
    <span class="skill-pill pill-lang">Python</span>
    <span class="skill-pill pill-lang">C</span>
    <span class="skill-pill pill-lang">C++</span>
    <span class="skill-pill pill-lang">Java</span>
    <span class="skill-pill pill-lang">MATLAB</span>
    <span class="skill-pill pill-lang">LaTeX</span>
    <span class="skill-pill pill-lang">Mathematica</span>
  </div>
</div>

<div class="skill-group">
  <div class="skill-group-title">🧠 Deep Learning</div>
  <div class="skill-pills">
    <span class="skill-pill pill-ml">PyTorch</span>
    <span class="skill-pill pill-ml">TensorFlow</span>
    <span class="skill-pill pill-ml">DeepSpeed</span>
    <span class="skill-pill pill-ml">DDP</span>
  </div>
</div>

<div class="skill-group">
  <div class="skill-group-title">📊 Data & Analysis</div>
  <div class="skill-pills">
    <span class="skill-pill pill-data">Pandas</span>
    <span class="skill-pill pill-data">NumPy</span>
  </div>
</div>

<div class="skill-group">
  <div class="skill-group-title">🌐 Web Development</div>
  <div class="skill-pills">
    <span class="skill-pill pill-web">HTML</span>
    <span class="skill-pill pill-web">CSS</span>
    <span class="skill-pill pill-web">JavaScript</span>
    <span class="skill-pill pill-web">Vue</span>
  </div>
</div>

<div class="skill-group">
  <div class="skill-group-title">🛠️ Tools & Infrastructure</div>
  <div class="skill-pills">
    <span class="skill-pill pill-tool">Git</span>
    <span class="skill-pill pill-tool">Docker</span>
    <span class="skill-pill pill-tool">CUDA</span>
    <span class="skill-pill pill-tool">HPC</span>
  </div>
</div>

<div class="skill-group">
  <div class="skill-group-title">🌍 Languages</div>
  <div class="skill-pills">
    <span class="skill-pill pill-nlang">English (TOEFL 110, GRE 328)</span>
    <span class="skill-pill pill-nlang">Chinese (Native)</span>
  </div>
</div>

</div>
</details>

<details open>
<summary>🎓 Professional Service</summary>
<div class="section-content">

<div class="reviewer-category">
  <div class="reviewer-label">Computer Vision & Multimedia</div>
  <div class="venue-badges">
    <span class="venue-badge">CVPR 2025</span>
    <span class="venue-badge">ICCV 2025</span>
    <span class="venue-badge">WACV 2026</span>
    <span class="venue-badge">MICCAI 2025</span>
    <span class="venue-badge">ACM MM 2024</span>
  </div>
</div>

<div class="reviewer-category">
  <div class="reviewer-label">Machine Learning & AI</div>
  <div class="venue-badges">
    <span class="venue-badge">NeurIPS 2024</span>
    <span class="venue-badge">ICML 2025</span>
    <span class="venue-badge">ICLR 2024</span>
    <span class="venue-badge">AAAI</span>
    <span class="venue-badge">AISTATS 2024</span>
  </div>
</div>

<div class="reviewer-category">
  <div class="reviewer-label">Journals</div>
  <div class="venue-badges">
    <span class="venue-badge journal">IJCV</span>
    <span class="venue-badge journal">TIP</span>
  </div>
</div>

</div>
</details>

</div>

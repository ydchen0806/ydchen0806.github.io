# 📝 Selected Research

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=hCvlj5cAAAAJ&hl=en&oi=ao) [![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=hCvlj5cAAAAJ&hl=en&oi=ao)

<details>
<summary>📈 <strong>View Citation Trend</strong></summary>
<div align="center" style="padding: 1em;">
  <img src="https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/citation_trend.svg" alt="Citation Trend" style="max-width: 100%; height: auto;">
</div>
</details>

**Note:** * denotes equal contribution. Journal and conference papers shown here are first- or co-first-authored; technical-report roles are stated individually.

<style>
#pub-section details {
  margin-bottom: 1em;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid #e8e8e8;
  transition: box-shadow 0.3s;
}
#pub-section details:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
#pub-section details[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}

#pub-section summary {
  padding: 0.9em 1.2em;
  cursor: pointer;
  font-size: 1.1em;
  font-weight: 600;
  color: #1a1a1a;
  background: linear-gradient(135deg, #fef5ff 0%, #f5eef8 100%);
  user-select: none;
  display: flex;
  align-items: center;
  gap: 0.5em;
  list-style: none;
  transition: background 0.2s;
}
#pub-section summary::-webkit-details-marker { display: none; }
#pub-section summary::before {
  content: "▶";
  font-size: 0.7em;
  color: #9C27B0;
  transition: transform 0.25s;
  display: inline-block;
}
#pub-section details[open] > summary::before {
  transform: rotate(90deg);
}
#pub-section summary:hover {
  background: linear-gradient(135deg, #f5eef8 0%, #ece0f0 100%);
}

#pub-section .badge-count {
  font-size: 0.75em;
  font-weight: 500;
  color: #fff;
  background: #9C27B0;
  padding: 2px 9px;
  border-radius: 12px;
  margin-left: auto;
}

.paper-box {
  list-style-type: none;
  margin-bottom: 0;
  padding: 1.5em;
  border-bottom: 1px solid #f0f0f0;
  transition: background 0.15s;
}
.paper-box:last-child { border-bottom: none; }
.paper-box:hover { background: #fdfaff; }

.paper-box-image img {
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

#pub-section .paper-box-image > div { width: 100%; }
#pub-section .paper-box-image .image-popup { display: block; cursor: zoom-in; }
#pub-section .paper-box-image .badge-journal,
#pub-section .paper-box-image .badge-conference,
#pub-section .paper-box-image .badge-ccf {
  position: static;
  margin-bottom: 8px;
}

.paper-box-text a {
  color: #1a1a1a;
  font-weight: 600;
  font-size: 1.05em;
  text-decoration: none;
  transition: all 0.2s;
}
.paper-box-text a:hover {
  color: #9C27B0;
  text-decoration: underline;
}

.badge-journal, .badge-conference {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85em;
  font-weight: 600;
  margin-right: 6px;
  margin-bottom: 8px;
}
.badge-journal {
  background: #9C27B0;
  color: white;
}
.badge-conference {
  background: #673AB7;
  color: white;
}

.badge-impact, .badge-ccf {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  font-size: 0.75em;
  font-weight: 500;
}
.badge-q1 {
  background: #FFD700;
  color: #333;
}
.badge-ccf-a {
  background: #E91E63;
  color: white;
}
.badge-ccf-b {
  background: #FF9800;
  color: white;
}

.paper-box-text strong {
  color: #9C27B0;
}
.paper-box-text img[src*="shields.io"] {
  vertical-align: middle;
  margin-left: 4px;
}

.research-tags {
  display: inline-flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-left: 8px;
  max-width: 100%;
  vertical-align: middle;
}
.research-tag {
  display: inline-block;
  padding: 2px 6px;
  font-size: 0.7em;
  font-weight: 500;
  border-radius: 3px;
  background: rgba(118, 75, 162, 0.1);
  color: #764ba2;
  border: 1px solid rgba(118, 75, 162, 0.2);
  white-space: nowrap;
}
@media (max-width: 600px) {
  #pub-section .research-tags {
    display: flex;
    width: 100%;
    margin: 0.4em 0 0;
  }
}

.citation-badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 2px 6px;
  font-size: 0.7em;
  font-weight: 500;
  border-radius: 4px;
  background: #4285f4;
  color: white;
  margin-left: 6px;
  vertical-align: middle;
}
.citation-badge::before {
  content: '📊';
  font-size: 0.85em;
}
#pub-section .paper-citation[hidden] { display: none; }
</style>

<script>
window.addEventListener('load', function () {
  // Exact normalized titles prevent citation totals being assigned to a different paper.
  function normalize(title) { return title.toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); }
  fetch('https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/first_author_papers.json')
    .then(function (response) { return response.ok ? response.json() : []; })
    .then(function (papers) {
      if (!Array.isArray(papers)) return;
      document.querySelectorAll('#pub-section .paper-citation').forEach(function (badge) {
        var paper = papers.find(function (item) { return normalize(item.title || '') === normalize(badge.dataset.title); });
        if (!paper || !Number.isFinite(paper.citations) || paper.citations < 10) return;
        var count = Math.floor(paper.citations);
        var img = badge.querySelector('img');
        img.src = 'https://img.shields.io/badge/citations-' + count + '-blue?logo=google-scholar&logoColor=white&style=flat-square';
        img.alt = count + ' Google Scholar citations';
        badge.hidden = false;
      });
    }).catch(function () {});
});
</script>

<div id="pub-section">

<details open>
<summary>🧠 Representation and Predictive Learning <span class="badge-count">3</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICCV 2025</div><div class="badge-ccf badge-ccf-a">CCF A</div><a href="/images/ICCV25.png" class="image-popup" title="TokenUnify: autoregressive pretraining objectives"><img src="/images/ICCV25.png" alt="TokenUnify: autoregressive pretraining objectives" width="1269" height="360" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[TokenUnify: Scaling Up Autoregressive Pretraining for Neuron Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_TokenUnify_Scaling_Up_Autoregressive_Pretraining_for_Neuron_Segmentation_ICCV_2025_paper.html) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:blknAaTinKkC" data-title="TokenUnify: Scaling Up Autoregressive Pretraining for Neuron Segmentation"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Self-Supervised Learning</span></span> \\
ICCV · 2025 \\
**Yinda Chen**\*; Haoyuan Shi\*; Xiaoyu Liu; Te Shi; Ruobing Zhang; Dong Liu; Zhiwei Xiong; Feng Wu

[**Code**](https://github.com/ydchen0806/TokenUnify) [![](https://img.shields.io/github/stars/ydchen0806/TokenUnify?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/TokenUnify) | [**Dataset**](https://huggingface.co/datasets/cyd0806/wafer_EM) | [**Weights**](https://huggingface.co/cyd0806/TokenUnify/tree/main/Pretrained_weights)

Autoregressive pretraining for volumetric neuron segmentation, combining three complementary prediction objectives with long-sequence modeling and an analysis of prediction-error accumulation.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">IJCAI 2023</div><div class="badge-ccf badge-ccf-a">CCF A</div><a href="/images/ijcai2023.png" class="image-popup" title="dbMiM: pretraining and finetuning framework"><img src="/images/ijcai2023.png" alt="dbMiM: pretraining and finetuning framework" width="743" height="362" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Self-Supervised Neuron Segmentation with Multi-Agent Reinforcement Learning](https://www.ijcai.org/proceedings/2023/68) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:QIV2ME_5wuYC" data-title="Self-Supervised Neuron Segmentation with Multi-Agent Reinforcement Learning"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Self-Supervised Learning</span></span> \\
IJCAI · 2023 \\
**Yinda Chen**; Wei Huang; Shenglong Zhou; Qi Chen; Zhiwei Xiong

[**Code**](https://github.com/ydchen0806/dbMiM) [![](https://img.shields.io/github/stars/ydchen0806/dbMiM?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/dbMiM) | [**Pretraining data**](https://huggingface.co/datasets/cyd0806/EM_pretrain_data)

Decision-based masked image modeling that learns masking policies through multi-agent reinforcement learning for neuron segmentation.

</div>
</div>

<!-- Original paper figure: https://arxiv.org/pdf/2308.09917, Figure 1 (page 2) -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICASSP 2024</div><div class="badge-ccf badge-ccf-b">CCF B</div><a href="/images/ICASSP24.png" class="image-popup" title="MS-Con, Figure 1: multiscale pretraining and segmentation framework"><img src="/images/ICASSP24.png" alt="MS-Con, Figure 1: multiscale pretraining and segmentation framework" width="1401" height="1002" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Learning Multiscale Consistency for Self-Supervised Electron Microscopy Instance Segmentation](https://arxiv.org/abs/2308.09917) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:9ZlFYXVOiuMC" data-title="Learning Multiscale Consistency for Self-Supervised Electron Microscopy Instance Segmentation"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Pretraining Methods</span></span> \\
ICASSP · 2024 \\
**Yinda Chen**; Wei Huang; Xiaoyu Liu; Shiyu Deng; Qi Chen; Zhiwei Xiong

[**Code**](https://github.com/ydchen0806/MS-Con-EM-Seg) [![](https://img.shields.io/github/stars/ydchen0806/MS-Con-EM-Seg?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/MS-Con-EM-Seg)

Self-supervised pretraining that encourages multiscale consistency in volumetric electron microscopy representations for neuron instance segmentation.

</div>
</div>

</details>

<details>
<summary>✨ Foundation Models, Multimodal Learning &amp; Agents <span class="badge-count">8</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-journal">IEEE TPAMI</div><a href="/images/TPAMI25.png" class="image-popup" title="GRCL: generative reference and conditional latent coding framework"><img src="/images/TPAMI25.png" alt="GRCL: generative reference and conditional latent coding framework" width="1740" height="501" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Learned Image Coding with Generative Reference of Conditional Latents](https://doi.org/10.1109/TPAMI.2026.3744812)  <span class="research-tags"><span class="research-tag">Image Compression</span><span class="research-tag">Generative Models</span></span> \\
IEEE TPAMI · Accepted October 2026 \\
Siqi Wu\*; **Yinda Chen**\*; Weiming Chen; Dong Liu; K. C. Ho; Zhihai He

[**PDF**](/docs/Learned_Image_Coding_with_Generative_Reference_of_Conditional_Latents.pdf) | [**Code**](https://github.com/ydchen0806/CLC) [![](https://img.shields.io/github/stars/ydchen0806/CLC?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/CLC)

GRCL uses retrieved or generated images as references for conditional latent coding. The framework combines reference generation, latent matching and synthesis, and theoretical analysis of robustness to reference perturbations.

</div>
</div>

<!-- Original paper figure: /docs/Condition_generation_Latent_Coding_with_an_External_Dictionary_for_Deep_Image_Compression.pdf, Figure 1 (page 2) -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">AAAI 2025</div><div class="badge-ccf badge-ccf-a">CCF A</div><a href="/images/AAAI25.png" class="image-popup" title="CLC, Figure 1: conditional latent coding framework"><img src="/images/AAAI25.png" alt="CLC, Figure 1: conditional latent coding framework" width="1401" height="955" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Conditional Latent Coding with Learnable Synthesized Reference for Deep Image Compression](https://doi.org/10.1609/aaai.v39i12.33403) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:4DMP91E08xMC" data-title="Conditional Latent Coding with Learnable Synthesized Reference for Deep Image Compression"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Image Compression</span></span> \\
AAAI · 2025 \\
Siqi Wu\*; **Yinda Chen**\*; Dong Liu; Zhihai He

[**PDF**](/docs/Condition_generation_Latent_Coding_with_an_External_Dictionary_for_Deep_Image_Compression.pdf) | [**Code**](https://github.com/ydchen0806/CLC) [![](https://img.shields.io/github/stars/ydchen0806/CLC?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/CLC) | [**Weights**](https://huggingface.co/cyd0806/CLC)

Learnable reference synthesis from an external image dictionary improves conditional latent coding for learned image compression.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICCV Workshop 2025</div><a href="/images/GTGM.png" class="image-popup" title="GTGM: generative text-guided pretraining framework"><img src="/images/GTGM.png" alt="GTGM: generative text-guided pretraining framework" width="1497" height="744" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[GTGM: Generative Text-Guided 3D Vision-Language Pretraining for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025W/VLM3D/html/Chen_GTGM_Generative_Text-Guided_3D_Vision-Language_Pretraining_for_Medical_Image_Segmentation_ICCVW_2025_paper.html) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:NMxIlDl6LWMC" data-title="GTGM: Generative Text-Guided 3D Vision-Language Pretraining for Medical Image Segmentation"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Vision-Language</span><span class="research-tag">Medical Imaging</span></span> \\
ICCV Workshop on VLM3D · 2025 \\
**Yinda Chen**\*; Che Liu\*; Wei Huang; Xiaoyu Liu; Haoyuan Shi; Sibo Cheng; Rossella Arcucci; Zhiwei Xiong

[**Code**](https://github.com/ydchen0806/gtgm) [![](https://img.shields.io/github/stars/ydchen0806/gtgm?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/gtgm)

Uses generated textual descriptions and negative-free contrastive learning to pretrain 3D medical image representations without paired medical text; evaluated through downstream segmentation on 10 CT/MRI datasets.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">MICCAI 2024</div><div class="badge-ccf badge-ccf-b">CCF B</div><a href="/images/MICCAI24.png" class="image-popup" title="BIMCV-R: MedFinder image-text retrieval framework"><img src="/images/MICCAI24.png" alt="BIMCV-R: MedFinder image-text retrieval framework" width="782" height="362" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[BIMCV-R: A Landmark Dataset for 3D CT Text-Image Retrieval](https://papers.miccai.org/miccai-2024/100-Paper1194.html) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:mVmsd5A6BfQC" data-title="BIMCV-R: A Landmark Dataset for 3D CT Text-Image Retrieval"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Vision-Language</span><span class="research-tag">Multimodal Learning</span></span> \\
MICCAI · 2024 \\
**Yinda Chen**; Che Liu; Xiaoyu Liu; Rossella Arcucci; Zhiwei Xiong

[**Dataset**](https://huggingface.co/datasets/cyd0806/BIMCV-R) | [**Code**](https://github.com/ydchen0806/MedFinder) [![](https://img.shields.io/github/stars/ydchen0806/MedFinder?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/MedFinder)

A dataset of 8,069 3D CT volumes with paired radiology reports, together with the MedFinder framework for bidirectional medical image–text retrieval.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">NeurIPS 2024</div><div class="badge-ccf badge-ccf-a">CCF A</div><a href="/images/NeurIPS24.png" class="image-popup" title="MaskFactory: mask editing and image generation framework"><img src="/images/NeurIPS24.png" alt="MaskFactory: mask editing and image generation framework" width="806" height="602" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[MaskFactory: Towards High-quality Synthetic Data Generation for Dichotomous Image Segmentation](https://arxiv.org/abs/2412.19080) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:aqlVkmm33-oC" data-title="MaskFactory: Towards High-quality Synthetic Data Generation for Dichotomous Image Segmentation"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Multimodal Learning</span></span> \\
NeurIPS · 2024 \\
Haotian Qian\*; **Yinda Chen**\*; Shengtao Lou; Fahad Shahbaz Khan; Xiaogang Jin; Deng-Ping Fan

[**Project**](https://qian-hao-tian.github.io/MaskFactory/) | [**Code**](https://github.com/ydchen0806/MaskFactory) [![](https://img.shields.io/github/stars/ydchen0806/MaskFactory?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/MaskFactory)

A two-stage framework for generating paired images and masks for dichotomous image segmentation, expanding training data while preserving image–mask consistency.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-journal">IEEE JBHI</div><a href="/images/JBHI25.png" class="image-popup" title="EMPOWER: evolutionary medical prompt optimization framework"><img src="/images/JBHI25.png" alt="EMPOWER: evolutionary medical prompt optimization framework" width="1335" height="774" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[EMPOWER: Evolutionary Medical Prompt Optimization With Reinforcement Learning](https://doi.org/10.1109/JBHI.2025.3621907) <a class="paper-citation" hidden href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=hCvlj5cAAAAJ&amp;pagesize=100&amp;citation_for_view=hCvlj5cAAAAJ:J_g5lzvAfSwC" data-title="EMPOWER: Evolutionary Medical Prompt Optimization With Reinforcement Learning"><img alt="Google Scholar citations" /></a> <span class="research-tags"><span class="research-tag">Vision-Language</span><span class="research-tag">Multimodal Learning</span></span> \\
IEEE JBHI · 2025 \\
**Yinda Chen**\*; Yangfan He\*; Jing Yang; Dapeng Zhang; Zhenlong Yuan; Muhammad Attique Khan; Jamel Baili; Por Lip Yee

[**Paper**](https://ieeexplore.ieee.org/document/11205280/)

Combines evolutionary prompt optimization with reinforcement learning and multi-dimensional evaluation for medical language tasks.

</div>
</div>


<!-- Original report figure: https://arxiv.org/html/2610.30949v1/M1-ARCH-V3.svg -->
<div class='paper-box' id='iquest-q1-report' style="scroll-margin-top: 90px;">
<div class='paper-box-image'><div>
<div class="badge-conference" style="position: static;">Technical Report 2026</div>
<a href="/images/IQuestQ1.png" class="image-popup" title="IQuest-Q1 technical report, Figure 3: overall model architecture"><img src="/images/IQuestQ1.png" alt="IQuest-Q1 technical report, Figure 3: overall model architecture" width="1400" height="1241" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a>
</div></div>
<div class='paper-box-text' markdown="1">

[IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems](https://arxiv.org/abs/2610.30949)  <span class="research-tags"><span class="research-tag">Agentic Models</span><span class="research-tag">Tool Use</span></span> \\
Ubiquant (九坤投资) · October 2026 \\
**Yinda Chen**, co-author

[**Report**](https://arxiv.org/abs/2610.30949) | [**Project**](https://iquestlab.github.io/) | [**Code**](https://github.com/IQuestLab/IQuest-Q1) [![](https://img.shields.io/github/stars/IQuestLab/IQuest-Q1?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/IQuestLab/IQuest-Q1) | [**Models**](https://huggingface.co/IQuestLab/IQuest-Q1)

A foundation model for command-line interaction, coding, and multi-step tool use. Contributed during my research internship at Ubiquant (九坤投资).

</div>
</div>

<!-- Original report figure: https://arxiv.org/html/2610.11451v1/improvement-loop.svg -->
<div class='paper-box' id='sail-report' style="scroll-margin-top: 90px;">
<div class='paper-box-image'><div>
<div class="badge-conference" style="position: static;">Technical Report 2026</div>
<a href="/images/SAIL.png" class="image-popup" title="SAIL report, Figure 4: science-aware improvement loop"><img src="/images/SAIL.png" alt="SAIL report, Figure 4: science-aware improvement loop" width="1400" height="875" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a>
</div></div>
<div class='paper-box-text' markdown="1">

[SAIL: Scientific Agentic Intelligence via a Science-Aware Loop](https://arxiv.org/abs/2610.11451)  <span class="research-tags"><span class="research-tag">Scientific Agents</span><span class="research-tag">Agentic Models</span></span> \\
Ubiquant (九坤投资) · October 2026 \\
SAIL Model Team · **Yinda Chen**, core contributor

[**Report**](https://arxiv.org/abs/2610.11451)

A scientific-agent research project for literature research, scientific coding, and multi-step investigations, developed through a science-aware improvement loop.

</div>
</div>

</details>

<details open>
<summary>🤖 World Models and Embodied Intelligence <span class="badge-count">2</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">Technical Report 2026</div><a href="/images/PelicanUnified.png" class="image-popup" title="Pelican-Unified 1.0: unified embodied model overview"><img src="/images/PelicanUnified.png" alt="Pelican-Unified 1.0: unified embodied model overview" width="1300" height="1119" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Pelican-Unified 1.0: A Unified Embodied Intelligence Model (UEI) for Understanding, Reasoning, Imagination and Action](https://arxiv.org/abs/2605.15153)  <span class="research-tags"><span class="research-tag">Embodied Intelligence</span><span class="research-tag">World Models</span><span class="research-tag">Unified Models</span></span> \\
X-Humanoid, WFM System Group · May 2026 \\
Pelican-Unified Team · **Yinda Chen**, core contributor

[**Report**](https://arxiv.org/abs/2605.15153) | [**Organization**](https://www.x-humanoid.com/)

My contribution: unified vision-language modeling and action capability.

A unified embodied model that combines scene and instruction understanding, task reasoning, and joint prediction of future video and robot actions.

</div>
</div>

<!-- Original paper figure: https://arxiv.org/html/2607.06655v2/structure.png, Figure 2 (PDF page 4) -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">Technical Report 2026</div><a href="/images/PelicanVLA05.png" class="image-popup" title="Pelican-VLA 0.5, Figure 2: model overview"><img src="/images/PelicanVLA05.png" alt="Pelican-VLA 0.5, Figure 2: model overview" width="1520" height="597" loading="lazy" decoding="async" style="width: 100%; height: auto;"></a></div></div>
<div class='paper-box-text' markdown="1">

[Pelican-VLA 0.5: Attending Before Acting Benefits Generalization](https://arxiv.org/abs/2607.06655)  <span class="research-tags"><span class="research-tag">Vision-Language-Action</span><span class="research-tag">Embodied Intelligence</span><span class="research-tag">World Models</span></span> \\
X-Humanoid, WFM System Group · July 2026 \\
Pelican-VLA Team · **Yinda Chen**, contributor

[**Report**](https://arxiv.org/abs/2607.06655) | [**Code**](https://github.com/Open-X-Humanoid/Pelican-VLA05) [![](https://img.shields.io/github/stars/Open-X-Humanoid/Pelican-VLA05?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/Open-X-Humanoid/Pelican-VLA05) | [**Models**](https://huggingface.co/X-Humanoid/Pelican-VLA05)

The VLA component of Pelican-Unified connects vision-language understanding, future-frame generation, and action prediction through learnable bottleneck tokens. The work studies task-relevant attention and manipulation generalization.

</div>
</div>

</details>

</div>

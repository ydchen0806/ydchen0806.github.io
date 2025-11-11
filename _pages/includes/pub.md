# 📝 Selected Publications  

For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=hCvlj5cAAAAJ&hl=en&oi=ao) [![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=hCvlj5cAAAAJ&hl=en&oi=ao)
<!-- 动态引用徽章（已注释）
[![](https://img.shields.io/badge/dynamic/json?logo=google-scholar&logoColor=white&label=citations&query=citedby&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fydchen0806%2Fydchen0806.github.io@google-scholar-stats%2Fgs_data.json)](https://scholar.google.com/citations?user=hCvlj5cAAAAJ&hl=en&oi=ao)
-->

**Note:** * denotes equal contribution

<style>
/* Publications section styles */
#journal-articles, #conference-papers {
  counter-reset: paper-counter;
}

/* Paper box enhanced styling */
.paper-box {
  list-style-type: none;
  margin-bottom: 2.5em;
  padding: 1.5em;
  background: linear-gradient(to right, #fef5ff 0%, #ffffff 100%);
  border-radius: 10px;
  border-left: 5px solid #9C27B0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
}

.paper-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Journal Articles自动编号 */
#journal-articles .paper-box-text::before {
  counter-increment: paper-counter;
  content: "[J" counter(paper-counter) "] ";
  font-weight: bold;
  color: #9C27B0;
  margin-right: 0.5em;
  display: inline;
  font-size: 1.1em;
}

/* Conference Papers自动编号 */
#conference-papers {
  counter-reset: paper-counter;
}

#conference-papers .paper-box-text::before {
  counter-increment: paper-counter;
  content: "[C" counter(paper-counter) "] ";
  font-weight: bold;
  color: #9C27B0;
  margin-right: 0.5em;
  display: inline;
  font-size: 1.1em;
}

/* Paper title styling */
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

/* Badge styling */
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

/* Paper image styling */
.paper-box-image img {
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

/* Code and resource links */
.paper-box-text strong {
  color: #9C27B0;
}

.paper-box-text img[src*="shields.io"] {
  vertical-align: middle;
  margin-left: 4px;
}

/* Research area tags */
.research-tags {
  display: inline-flex;
  gap: 4px;
  margin-left: 8px;
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
</style>

<div id="journal-articles" markdown="1">

## 📰 Journal Articles

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-journal">IEEE JBHI</div><div class="badge-impact badge-q1">SCI Q1 | IF: 6.7</div><img src='images/JBHI25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

> [EMPOWER: Evolutionary Medical Prompt Optimization With Reinforcement Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11205280) <span class="research-tags"><span class="research-tag">Vision-Language</span><span class="research-tag">Multimodal Learning</span></span> \\
  IEEE Journal of Biomedical and Health Informatics | October 16, 2025 \\
  **Yinda Chen\***; Yangfan He\*; Jing Yang; Dapeng Zhang; Zhenlong Yuan; Muhammad Attique Khan; Jamel Baili; Por Lip Yee

> EMPOWER proposes an evolutionary framework for prompt optimization through specialized representation learning and multi-dimensional evaluation. It achieves 24.7% reduction in factual errors and 15.3% higher preference scores.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-journal">IEEE TMI</div><div class="badge-impact badge-q1">SCI Q1 | IF: 10.6</div><img src='images/TMI24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Unsupervised Domain Adaptation for EM Image Denoising with Invertible Networks](/docs/Unsupervised_Domain_Adaptation_for_EM_Image_Denoising_With_Invertible_Networks.pdf) <span class="research-tags"><span class="research-tag">Domain Adaptation</span><span class="research-tag">Image Denoising</span></span> \\
IEEE Transactions on Medical Imaging | July 29, 2024 \\
Shiyu Deng; **Yinda Chen**; Wei Huang; Ruobing Zhang; Zhiwei Xiong

[**Code**](https://github.com/sydeng99/DADn) [![](https://img.shields.io/github/stars/sydeng99/DADn?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/sydeng99/DADn)

The paper proposes an unsupervised domain adaptation method for EM image denoising with invertible networks, outperforming existing methods.

</div>
</div>

</div>

<div id="conference-papers" markdown="1">

## 🎓 Conference Papers

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICCV 2025</div><div class="badge-ccf badge-ccf-a">CCF A</div><img src='images/ICCV25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TokenUnify: Scaling Up Autoregressive Pretraining for Computer Vision](https://openaccess.thecvf.com/content/ICCV2025/papers/Chen_TokenUnify_Scaling_Up_Autoregressive_Pretraining_for_Neuron_Segmentation_ICCV_2025_paper.pdf) <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Self-Supervised Learning</span></span> \\
ICCV | October 25, 2025 \\
**Yinda Chen\***; Haoyuan Shi\*; Xiaoyu Liu; Te Shi; Ruobing Zhang; Dong Liu; Zhiwei Xiong; Feng Wu

[**Code**](https://github.com/ydchen0806/TokenUnify) [![](https://img.shields.io/github/stars/ydchen0806/TokenUnify?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/TokenUnify) | [**Dataset**](https://huggingface.co/datasets/cyd0806/wafer_EM) [![](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/cyd0806/wafer_EM) | [**Weights**](https://huggingface.co/cyd0806/TokenUnify/tree/main/Pretrained_weights) [![](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Weights-yellow)](https://huggingface.co/cyd0806/TokenUnify/tree/main/Pretrained_weights)

TokenUnify proposes a hierarchical predictive coding framework for computer vision, reducing autoregressive error from O(K) to O(√K). It introduces a dataset with 1.2 billion annotated voxels and achieves 44% improvement over training from scratch.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICML 2025</div><div class="badge-ccf badge-ccf-a">CCF A</div><img src='images/ICML25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MaskTwins: Dual-form Complementary Masking for Domain-Adaptive Image Segmentation](https://openreview.net/pdf?id=9CpeZ8BzPO) <span class="research-tags"><span class="research-tag">Domain Adaptation</span><span class="research-tag">Pretraining Methods</span></span> \\
ICML | July 13, 2025 \\
Jiawen Wang; **Yinda Chen\*** (Theory Contribution & Project Leader); Xiaoyu Liu; Che Liu; Dong Liu; Jianqing Gao; Zhiwei Xiong

[**Code**](https://github.com/jwwang0421/masktwins) [![](https://img.shields.io/github/stars/jwwang0421/masktwins?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/jwwang0421/masktwins) | [**Poster**](https://icml.cc/media/PosterPDFs/ICML%202025/46243.png?t=1750997391.8351207)

MaskTwins introduces a dual-form complementary masking strategy for domain-adaptive image segmentation, effectively bridging the domain gap through coordinated spatial and feature-level masking mechanisms.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">AAAI 2025</div><div class="badge-ccf badge-ccf-a">CCF A</div><img src='images/AAAI25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

> [Condition-generation Latent Coding with an External Dictionary for Deep Image Compression](/docs/Condition_generation_Latent_Coding_with_an_External_Dictionary_for_Deep_Image_Compression.pdf) <span class="research-tags"><span class="research-tag">Image Compression</span></span> \\
  AAAI <span style="color:red">**(<font color="red">oral</font>)**</span> | March 06, 2025 \\
  Siqi Wu; **Yinda Chen\***; Dong Liu; Zhihai He

  [**Code**](https://github.com/ydchen0806/CLC) [![](https://img.shields.io/github/stars/ydchen0806/CLC?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/CLC) | [**Weights**](https://huggingface.co/cyd0806/CLC/tree/main) [![](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Weights-yellow)](https://huggingface.co/cyd0806/CLC/tree/main)

The paper proposes CLC for deep image compression. It uses a dictionary to generate references, shows good performance, and has theoretical analysis.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">NeurIPS 2024</div><div class="badge-ccf badge-ccf-a">CCF A</div><img src='images/NeurIPS24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MaskFactory: Towards High-quality Synthetic Data Generation for Dichotomous Image Segmentation](https://arxiv.org/pdf/2412.19080) <span class="research-tags"><span class="research-tag">Multimodal Learning</span></span> \\
NeurIPS | October 17, 2024 \\
Haotian Qian; **Yinda Chen\***; Shengtao Lou; Fahad Shahbaz Khan; Xiaogang Jin; Deng-Ping Fan

[**Project**](https://qian-hao-tian.github.io/MaskFactory/) | [**Code**](https://github.com/ydchen0806/MaskFactory) [![](https://img.shields.io/github/stars/ydchen0806/MaskFactory?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/MaskFactory)

MaskFactory proposes a two-stage method to generate high-quality synthetic datasets for DIS, outperforming existing methods in quality and efficiency.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">MICCAI 2024</div><div class="badge-ccf badge-ccf-b">CCF B</div><img src='images/MICCAI24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[BIMCV-R: A Landmark Dataset for 3D CT Text-Image Retrieval](https://arxiv.org/pdf/2403.15992) <span class="research-tags"><span class="research-tag">Vision-Language</span><span class="research-tag">Multimodal Learning</span></span> \\
MICCAI | October 06, 2024 \\
**Yinda Chen**; Che Liu; Xiaoyu Liu; Rossella Arcucci; Zhiwei Xiong

[**Dataset**](https://huggingface.co/datasets/cyd0806/BIMCV-R) [![](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/cyd0806/BIMCV-R)

This paper presents BIMCV-R, a 3D CT text-image retrieval dataset, and MedFinder. Tests show MedFinder outperforms baselines in related tasks.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">ICASSP 2024</div><div class="badge-ccf badge-ccf-b">CCF B</div><img src='images/ICASSP24.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

> [Learning multiscale consistency for self-supervised computer vision instance segmentation](https://arxiv.org/pdf/2308.09917) <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Pretraining Methods</span></span> \\
  ICASSP | April 13, 2024 \\
  **Yinda Chen**; Wei Huang; Xiaoyu Liu; Shiyu Deng; Qi Chen; Zhiwei Xiong

  [**Code**](https://github.com/ydchen0806/MS-Con-EM-Seg) [![](https://img.shields.io/github/stars/ydchen0806/MS-Con-EM-Seg?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/MS-Con-EM-Seg)

> A pretraining framework for volume instance segmentation is proposed. It enforces multiscale consistency and shows good performance in instance segmentation tasks.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge-conference">IJCAI 2023</div><div class="badge-ccf badge-ccf-a">CCF A</div><img src='images/ijcai2023.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

> [Self-Supervised Computer Vision with Multi-Agent Reinforcement Learning](https://www.ijcai.org/proceedings/2023/0068.pdf) <span class="research-tags"><span class="research-tag">Computer Vision</span><span class="research-tag">Self-Supervised Learning</span></span> \\
  IJCAI <span style="color:red">**(<font color="red">oral</font>)**</span> | August 17, 2023 \\
  **Yinda Chen**; Wei Huang; Shenglong Zhou; Qi Chen; Zhiwei Xiong

  [**Code**](https://github.com/ydchen0806/dbMiM) [![](https://img.shields.io/github/stars/ydchen0806/dbMiM?style=social&label=Code+Stars&cacheSeconds=3600)](https://github.com/ydchen0806/dbMiM) | [**Pretrain Data**](https://huggingface.co/datasets/cyd0806/EM_pretrain_data/tree/main) [![](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/cyd0806/EM_pretrain_data/tree/main) | [**CREMI**](https://cremi.org/) | [**VNC**](https://drive.google.com/drive/folders/1JAdoKchlWrHnbTXvnFn6pWWwx6VIiMH3?usp=sharing)

> This paper proposes a decision-based MIM for computer vision segmentation. It uses MARL to optimize masking, outperforming alternatives.

</div>
</div>

</div>
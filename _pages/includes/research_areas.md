# 🎯 Research Areas

<div class="research-visualization">
  <div class="research-intro">
    <p>My research spans across multiple domains in AI and computer vision, with a focus on bridging <strong>understanding</strong> and <strong>generation</strong> in multimodal scenarios.</p>
  </div>

  <div class="chart-container">
    <div class="chart-wrapper radar-wrapper">
      <h3>📊 Research Focus Distribution</h3>
      <canvas id="researchRadarChart"></canvas>
    </div>
    <div class="chart-wrapper pie-wrapper">
      <h3>📈 Publication Topics</h3>
      <canvas id="researchPieChart"></canvas>
    </div>
  </div>

  <div class="research-keywords">
    <h3>🔑 Key Research Keywords</h3>
    <div class="keyword-cloud" id="keywordCloud">
      <!-- Keywords will be auto-generated from publications -->
    </div>
  </div>
</div>

<style>
.research-visualization {
  margin: 2em 0;
  padding: 2em;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.research-intro {
  text-align: center;
  margin-bottom: 2em;
  color: white;
  font-size: 1.1em;
}

.research-intro strong {
  color: #FFD700;
}

.chart-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2em;
  margin-bottom: 2em;
}

@media (max-width: 768px) {
  .chart-container {
    grid-template-columns: 1fr;
  }
}

.chart-wrapper {
  background: rgba(255, 255, 255, 0.95);
  padding: 1.5em;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.chart-wrapper:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}

.chart-wrapper h3 {
  margin-top: 0;
  margin-bottom: 1em;
  color: #764ba2;
  text-align: center;
  font-size: 1.2em;
}

.chart-wrapper canvas {
  max-height: 350px;
}

.research-keywords {
  background: rgba(255, 255, 255, 0.95);
  padding: 1.5em;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.research-keywords h3 {
  margin-top: 0;
  margin-bottom: 1em;
  color: #764ba2;
  text-align: center;
}

.keyword-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8em;
  justify-content: center;
  align-items: center;
  min-height: 120px;
}

.keyword {
  display: inline-block;
  padding: 0.5em 1em;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border-radius: 25px;
  font-weight: 500;
  transition: all 0.3s ease;
  cursor: default;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  animation: fadeInUp 0.6s ease-out backwards;
}

.keyword[data-weight="5"] {
  font-size: 1.2em;
  padding: 0.6em 1.2em;
}

.keyword[data-weight="4"] {
  font-size: 1.1em;
}

.keyword[data-weight="3"] {
  font-size: 1em;
}

.keyword[data-weight="2"] {
  font-size: 0.9em;
}

.keyword:hover {
  transform: scale(1.1) rotate(2deg);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
  background: linear-gradient(135deg, #764ba2, #667eea);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 为关键词添加不同的延迟 */
.keyword:nth-child(1) { animation-delay: 0.1s; }
.keyword:nth-child(2) { animation-delay: 0.2s; }
.keyword:nth-child(3) { animation-delay: 0.3s; }
.keyword:nth-child(4) { animation-delay: 0.4s; }
.keyword:nth-child(5) { animation-delay: 0.5s; }
.keyword:nth-child(6) { animation-delay: 0.6s; }
.keyword:nth-child(7) { animation-delay: 0.7s; }
.keyword:nth-child(8) { animation-delay: 0.8s; }
.keyword:nth-child(9) { animation-delay: 0.9s; }
.keyword:nth-child(10) { animation-delay: 1s; }
.keyword:nth-child(11) { animation-delay: 1.1s; }
.keyword:nth-child(12) { animation-delay: 1.2s; }
.keyword:nth-child(13) { animation-delay: 1.3s; }
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  // 自动从页面内容提取研究主题
  function extractResearchTopics() {
    const topics = {
      'Neuron Segmentation': 0,
      'Image Compression': 0,
      'Domain Adaptation': 0,
      'Medical Imaging': 0,
      'Multimodal Learning': 0,
      'Synthetic Data': 0,
      'Pretraining': 0
    };

    const keywords = {
      'Neuron Segmentation': ['neuron', 'segmentation', 'em image', 'electron microscopy'],
      'Image Compression': ['compression', 'coding', 'latent'],
      'Domain Adaptation': ['domain adaptation', 'unsupervised', 'transfer'],
      'Medical Imaging': ['medical', 'biomedical', 'ct', 'bimcv', 'clinical'],
      'Multimodal Learning': ['multimodal', 'vision-language', 'text-image', 'retrieval'],
      'Synthetic Data': ['synthetic', 'generation', 'maskfactory'],
      'Pretraining': ['pretraining', 'pretrain', 'self-supervised', 'tokenunify', 'reinforcement']
    };

    // 获取所有论文标题和描述
    const pubSection = document.querySelector('#-publications');
    if (pubSection) {
      const paperTexts = Array.from(pubSection.querySelectorAll('.paper-box-text'))
        .map(box => box.textContent.toLowerCase());

      paperTexts.forEach(text => {
        Object.entries(keywords).forEach(([topic, words]) => {
          if (words.some(word => text.includes(word))) {
            topics[topic]++;
          }
        });
      });
    }

    // 转换为百分比
    const total = Object.values(topics).reduce((a, b) => a + b, 0) || 1;
    const percentages = Object.entries(topics)
      .filter(([_, count]) => count > 0)
      .map(([topic, count]) => ({
        topic,
        percentage: Math.round((count / total) * 100)
      }))
      .sort((a, b) => b.percentage - a.percentage);

    return percentages;
  }

  // 提取关键词
  function extractKeywords() {
    const keywordScores = {
      'Multimodal Learning': 0,
      'Self-Supervised Pretraining': 0,
      'Biomedical Image Analysis': 0,
      'Image Compression': 0,
      'Neuron Segmentation': 0,
      'Domain Adaptation': 0,
      'Representation Learning': 0,
      'Vision-Language Models': 0,
      'Reinforcement Learning': 0,
      '3D Medical Imaging': 0,
      'Electron Microscopy': 0,
      'Synthetic Data Generation': 0
    };

    const keywordPatterns = {
      'Multimodal Learning': ['multimodal', 'multi-modal'],
      'Self-Supervised Pretraining': ['self-supervised', 'pretraining', 'pretrain'],
      'Biomedical Image Analysis': ['biomedical', 'medical image', 'clinical'],
      'Image Compression': ['compression', 'coding', 'latent'],
      'Neuron Segmentation': ['neuron', 'segmentation'],
      'Domain Adaptation': ['domain adaptation', 'unsupervised domain'],
      'Representation Learning': ['representation', 'feature learning'],
      'Vision-Language Models': ['vision-language', 'text-image', 'retrieval'],
      'Reinforcement Learning': ['reinforcement', 'marl', 'multi-agent'],
      '3D Medical Imaging': ['3d', 'ct', 'volumetric'],
      'Electron Microscopy': ['electron microscopy', 'em image'],
      'Synthetic Data Generation': ['synthetic', 'generation', 'maskfactory']
    };

    const pubSection = document.querySelector('#-publications');
    if (pubSection) {
      const allText = pubSection.textContent.toLowerCase();
      
      Object.entries(keywordPatterns).forEach(([keyword, patterns]) => {
        patterns.forEach(pattern => {
          const regex = new RegExp(pattern, 'gi');
          const matches = allText.match(regex);
          if (matches) {
            keywordScores[keyword] += matches.length;
          }
        });
      });
    }

    // 按分数排序并分配权重
    const sortedKeywords = Object.entries(keywordScores)
      .filter(([_, score]) => score > 0)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 13);

    const maxScore = sortedKeywords[0]?.[1] || 1;
    
    return sortedKeywords.map(([keyword, score]) => {
      let weight = Math.ceil((score / maxScore) * 5);
      weight = Math.max(2, Math.min(5, weight)); // 限制在2-5之间
      return { keyword, weight };
    });
  }

  // 生成关键词云
  function generateKeywordCloud() {
    const keywordCloud = document.getElementById('keywordCloud');
    if (!keywordCloud) return;

    const keywords = extractKeywords();
    keywordCloud.innerHTML = keywords.map((item, index) => 
      `<span class="keyword" data-weight="${item.weight}" style="animation-delay: ${index * 0.1}s">${item.keyword}</span>`
    ).join('');
  }

  // 雷达图配置（基于intro中提到的研究方向）
  const radarCtx = document.getElementById('researchRadarChart');
  if (radarCtx) {
    new Chart(radarCtx, {
      type: 'radar',
      data: {
        labels: [
          'Multimodal\nUnderstanding',
          'Multimodal\nGeneration',
          'Self-Supervised\nLearning',
          'Biomedical\nImaging',
          'Image\nCompression',
          'Domain\nAdaptation'
        ],
        datasets: [{
          label: 'Research Focus',
          data: [95, 85, 90, 88, 75, 80],
          backgroundColor: 'rgba(118, 75, 162, 0.2)',
          borderColor: 'rgba(118, 75, 162, 1)',
          borderWidth: 3,
          pointBackgroundColor: 'rgba(118, 75, 162, 1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(118, 75, 162, 1)',
          pointRadius: 5,
          pointHoverRadius: 7
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
          r: {
            beginAtZero: true,
            max: 100,
            ticks: {
              stepSize: 20,
              backdropColor: 'transparent',
              color: '#666',
              font: {
                size: 11
              }
            },
            grid: {
              color: 'rgba(118, 75, 162, 0.2)'
            },
            pointLabels: {
              font: {
                size: 12,
                weight: '600'
              },
              color: '#764ba2'
            }
          }
        },
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            backgroundColor: 'rgba(118, 75, 162, 0.9)',
            titleFont: {
              size: 14,
              weight: 'bold'
            },
            bodyFont: {
              size: 13
            },
            padding: 12,
            cornerRadius: 8
          }
        },
        animation: {
          duration: 2000,
          easing: 'easeInOutQuart'
        }
      }
    });
  }

  // 饼图配置（自动从publications提取）
  setTimeout(() => {
    const pieCtx = document.getElementById('researchPieChart');
    if (pieCtx) {
      const topicsData = extractResearchTopics();
      
      const colors = [
        { bg: 'rgba(156, 39, 176, 0.8)', border: 'rgba(156, 39, 176, 1)' },
        { bg: 'rgba(103, 58, 183, 0.8)', border: 'rgba(103, 58, 183, 1)' },
        { bg: 'rgba(63, 81, 181, 0.8)', border: 'rgba(63, 81, 181, 1)' },
        { bg: 'rgba(33, 150, 243, 0.8)', border: 'rgba(33, 150, 243, 1)' },
        { bg: 'rgba(0, 188, 212, 0.8)', border: 'rgba(0, 188, 212, 1)' },
        { bg: 'rgba(255, 152, 0, 0.8)', border: 'rgba(255, 152, 0, 1)' },
        { bg: 'rgba(76, 175, 80, 0.8)', border: 'rgba(76, 175, 80, 1)' }
      ];

      new Chart(pieCtx, {
        type: 'doughnut',
        data: {
          labels: topicsData.map(d => d.topic),
          datasets: [{
            data: topicsData.map(d => d.percentage),
            backgroundColor: colors.slice(0, topicsData.length).map(c => c.bg),
            borderColor: colors.slice(0, topicsData.length).map(c => c.border),
            borderWidth: 2,
            hoverOffset: 15
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          plugins: {
            legend: {
              position: 'bottom',
              labels: {
                padding: 15,
                font: {
                  size: 12,
                  weight: '500'
                },
                color: '#333',
                usePointStyle: true,
                pointStyle: 'circle'
              }
            },
            tooltip: {
              backgroundColor: 'rgba(118, 75, 162, 0.95)',
              titleFont: {
                size: 14,
                weight: 'bold'
              },
              bodyFont: {
                size: 13
              },
              padding: 12,
              cornerRadius: 8,
              callbacks: {
                label: function(context) {
                  let label = context.label || '';
                  if (label) {
                    label += ': ';
                  }
                  label += context.parsed + '%';
                  return label;
                }
              }
            }
          },
          animation: {
            animateRotate: true,
            animateScale: true,
            duration: 2000,
            easing: 'easeInOutQuart'
          }
        }
      });
    }

    // 生成关键词云
    generateKeywordCloud();
  }, 500); // 等待Publications部分加载完成
});
</script>

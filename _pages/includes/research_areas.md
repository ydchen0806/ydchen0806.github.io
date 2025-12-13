# 🎯 Research Areas

<div class="research-visualization">
  <div class="chart-container">
    <div class="chart-wrapper">
      <canvas id="researchRadarChart"></canvas>
    </div>
    <div class="chart-wrapper">
      <canvas id="researchPieChart"></canvas>
    </div>
  </div>

  <div class="keyword-cloud" id="keywordCloud">
    <!-- Keywords will be auto-generated from publications -->
  </div>
</div>

<style>
.research-visualization {
  margin: 1.5em 0;
}

.chart-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5em;
  margin-bottom: 1.5em;
}

@media (max-width: 768px) {
  .chart-container {
    grid-template-columns: 1fr;
  }
}

.chart-wrapper {
  background: #fafafa;
  padding: 1em;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  transition: box-shadow 0.3s ease;
}

.chart-wrapper:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.chart-wrapper canvas {
  max-height: 280px;
}

.keyword-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6em;
  justify-content: center;
  margin-top: 1em;
}

.keyword {
  display: inline-block;
  padding: 0.4em 0.9em;
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
  border-radius: 20px;
  font-weight: 500;
  font-size: 0.85em;
  transition: all 0.2s ease;
  cursor: default;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.keyword[data-weight="5"] {
  font-size: 1em;
  padding: 0.5em 1em;
}

.keyword[data-weight="4"] {
  font-size: 0.95em;
}

.keyword[data-weight="3"] {
  font-size: 0.85em;
}

.keyword[data-weight="2"] {
  font-size: 0.8em;
}

.keyword:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
// 确保在页面完全加载后执行
window.addEventListener('load', function() {
  // 默认关键词（作为备选，当 API 数据不可用时使用）
  const defaultKeywords = [
    { keyword: 'Multimodal Learning', weight: 5 },
    { keyword: 'Self-Supervised Learning', weight: 5 },
    { keyword: 'Computer Vision', weight: 4 },
    { keyword: 'Image Compression', weight: 4 },
    { keyword: 'Domain Adaptation', weight: 4 },
    { keyword: 'Medical Imaging', weight: 3 },
    { keyword: 'Generative Models', weight: 3 },
    { keyword: 'Embodied AI', weight: 3 }
  ];
  
  // 尝试从 GitHub 加载自动生成的关键词
  let autoKeywords = null;
  fetch('https://raw.githubusercontent.com/ydchen0806/ydchen0806.github.io/google-scholar-stats/research_keywords.json')
    .then(response => response.ok ? response.json() : null)
    .then(data => {
      if (data && data.length > 0) {
        autoKeywords = data;
        generateKeywordCloud();  // 重新生成词云
        console.log('[Research Areas] 已加载自动生成的研究方向关键词');
      }
    })
    .catch(err => console.log('[Research Areas] 使用默认关键词'));

  // 提取关键词
  function extractKeywords() {
    const keywordScores = {};
    const keywordPatterns = {
      'Multimodal Learning': ['multimodal', 'multi-modal', 'vision-language'],
      'Self-Supervised Learning': ['self-supervised', 'pretraining', 'pretrain'],
      'Computer Vision': ['vision', 'segmentation', 'image'],
      'Image Compression': ['compression', 'coding', 'latent'],
      'Domain Adaptation': ['domain adaptation', 'unsupervised domain'],
      'Deep Learning': ['deep learning', 'neural network', 'transformer'],
      'Representation Learning': ['representation', 'feature learning'],
      'Reinforcement Learning': ['reinforcement', 'marl'],
      'Synthetic Data': ['synthetic', 'generation', 'maskfactory'],
      'Data-Centric AI': ['data', 'dataset', 'annotation']
    };

    const pubSection = document.querySelector('#journal-articles, #conference-papers');
    if (pubSection) {
      const allText = pubSection.textContent.toLowerCase();
      
      Object.entries(keywordPatterns).forEach(([keyword, patterns]) => {
        let score = 0;
        patterns.forEach(pattern => {
          const matches = allText.match(new RegExp(pattern, 'gi'));
          if (matches) score += matches.length;
        });
        if (score > 0) keywordScores[keyword] = score;
      });
    }

    if (Object.keys(keywordScores).length === 0) return defaultKeywords;

    const sortedKeywords = Object.entries(keywordScores)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10);

    const maxScore = sortedKeywords[0]?.[1] || 1;
    
    return sortedKeywords.map(([keyword, score]) => ({
      keyword,
      weight: Math.max(2, Math.min(5, Math.ceil((score / maxScore) * 5)))
    }));
  }

  // 生成关键词云
  function generateKeywordCloud() {
    const keywordCloud = document.getElementById('keywordCloud');
    if (!keywordCloud) return;

    // 优先使用自动生成的关键词
    const keywords = autoKeywords || extractKeywords();
    keywordCloud.innerHTML = keywords.map(item => 
      `<span class="keyword" data-weight="${item.weight}">${item.keyword}</span>`
    ).join('');
  }

  // 提取研究主题
  function extractResearchTopics() {
    const topics = {
      'Computer Vision': 0,
      'Image Compression': 0,
      'Domain Adaptation': 0,
      'Multimodal Learning': 0,
      'Pretraining Methods': 0,
      'Data-Centric AI': 0
    };

    const keywords = {
      'Computer Vision': ['vision', 'segmentation', 'image'],
      'Image Compression': ['compression', 'coding'],
      'Domain Adaptation': ['domain adaptation', 'unsupervised'],
      'Multimodal Learning': ['multimodal', 'vision-language', 'text-image'],
      'Pretraining Methods': ['pretraining', 'self-supervised', 'tokenunify'],
      'Data-Centric AI': ['dataset', 'synthetic', 'data generation']
    };

    const paperBoxes = document.querySelectorAll('.paper-box-text');
    paperBoxes.forEach(box => {
      const text = box.textContent.toLowerCase();
      Object.entries(keywords).forEach(([topic, words]) => {
        if (words.some(word => text.includes(word))) {
          topics[topic]++;
        }
      });
    });

    const validTopics = Object.entries(topics)
      .filter(([_, count]) => count > 0);
    
    if (validTopics.length === 0) {
      return [
        { topic: 'Computer Vision', percentage: 28 },
        { topic: 'Image Compression', percentage: 18 },
        { topic: 'Multimodal Learning', percentage: 22 },
        { topic: 'Pretraining Methods', percentage: 18 },
        { topic: 'Data-Centric AI', percentage: 14 }
      ];
    }

    const total = validTopics.reduce((sum, [_, count]) => sum + count, 0);
    return validTopics.map(([topic, count]) => ({
      topic,
      percentage: Math.round((count / total) * 100)
    }));
  }

  // 雷达图
  const radarCtx = document.getElementById('researchRadarChart');
  if (radarCtx) {
    new Chart(radarCtx, {
      type: 'radar',
      data: {
        labels: ['Multimodal\nUnderstanding', 'Multimodal\nGeneration', 'Self-Supervised\nLearning', 'Computer\nVision', 'Image\nCompression', 'Domain\nAdaptation'],
        datasets: [{
          label: 'Research Focus',
          data: [95, 85, 90, 88, 75, 80],
          backgroundColor: 'rgba(118, 75, 162, 0.15)',
          borderColor: 'rgba(118, 75, 162, 0.8)',
          borderWidth: 2,
          pointBackgroundColor: 'rgba(118, 75, 162, 0.8)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(118, 75, 162, 1)',
          pointRadius: 4,
          pointHoverRadius: 6
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
              stepSize: 25,
              backdropColor: 'transparent',
              color: '#999',
              font: { size: 10 }
            },
            grid: { color: 'rgba(118, 75, 162, 0.1)' },
            pointLabels: {
              font: { size: 11, weight: '600' },
              color: '#764ba2'
            }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(118, 75, 162, 0.9)',
            padding: 10,
            cornerRadius: 6
          }
        }
      }
    });
  }

  // 饼图
  const pieCtx = document.getElementById('researchPieChart');
  if (pieCtx) {
    const topicsData = extractResearchTopics();
    
    const colors = [
      { bg: 'rgba(156, 39, 176, 0.7)', border: 'rgba(156, 39, 176, 1)' },
      { bg: 'rgba(103, 58, 183, 0.7)', border: 'rgba(103, 58, 183, 1)' },
      { bg: 'rgba(63, 81, 181, 0.7)', border: 'rgba(63, 81, 181, 1)' },
      { bg: 'rgba(33, 150, 243, 0.7)', border: 'rgba(33, 150, 243, 1)' },
      { bg: 'rgba(0, 188, 212, 0.7)', border: 'rgba(0, 188, 212, 1)' },
      { bg: 'rgba(255, 152, 0, 0.7)', border: 'rgba(255, 152, 0, 1)' }
    ];

    new Chart(pieCtx, {
      type: 'doughnut',
      data: {
        labels: topicsData.map(d => d.topic),
        datasets: [{
          data: topicsData.map(d => d.percentage),
          backgroundColor: colors.slice(0, topicsData.length).map(c => c.bg),
          borderColor: colors.slice(0, topicsData.length).map(c => c.border),
          borderWidth: 1,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              padding: 10,
              font: { size: 11, weight: '500' },
              color: '#555',
              usePointStyle: true,
              pointStyle: 'circle'
            }
          },
          tooltip: {
            backgroundColor: 'rgba(118, 75, 162, 0.9)',
            padding: 10,
            cornerRadius: 6,
            callbacks: {
              label: function(context) {
                return context.label + ': ' + context.parsed + '%';
              }
            }
          }
        }
      }
    });
  }

  // 生成关键词云
  generateKeywordCloud();
});
</script>

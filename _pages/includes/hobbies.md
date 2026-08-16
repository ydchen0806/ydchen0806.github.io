# 🎯 Hobbies & Interests

<style>
#hobbies-section .hobby-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1em;
  margin-bottom: 1.5em;
}
#hobbies-section .hobby-card {
  padding: 1em 1.2em;
  border-radius: 10px;
  background: linear-gradient(135deg, #f8f9fa 0%, #fff 100%);
  border: 1px solid #e8e8e8;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  transition: all 0.25s;
}
#hobbies-section .hobby-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(0,0,0,0.1);
  border-color: #ddd;
}
#hobbies-section .hobby-title {
  font-weight: 600;
  font-size: 1em;
  margin-bottom: 0.4em;
  color: #1a1a1a;
}
#hobbies-section .hobby-desc {
  font-size: 0.9em;
  color: #555;
  line-height: 1.6;
}
#hobbies-section .hobby-desc a {
  color: #2196F3;
  text-decoration: none;
}
#hobbies-section .hobby-desc a:hover {
  text-decoration: underline;
}

#hobbies-section .connect-box {
  padding: 1.2em 1.5em;
  border-radius: 10px;
  background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
  border: 1px solid #e0d6f0;
  margin-bottom: 1.5em;
}
#hobbies-section .connect-box h3 {
  margin: 0 0 0.6em 0;
  font-size: 1.05em;
  color: #1a1a1a;
}
#hobbies-section .connect-box p {
  margin: 0.3em 0;
  font-size: 0.92em;
  color: #444;
  line-height: 1.7;
}
#hobbies-section .connect-box a {
  color: #1976D2;
  text-decoration: none;
}
#hobbies-section .connect-box a:hover {
  text-decoration: underline;
}

#hobbies-section .cta-text {
  text-align: center;
  font-size: 0.95em;
  color: #666;
  margin: 1em 0;
  font-style: italic;
}

#hobbies-section .visitor-shell {
  max-width: 760px;
  margin: 1.1em auto 0;
  padding: 1px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(59,130,246,.35), rgba(139,92,246,.25), rgba(16,185,129,.24));
  box-shadow: 0 10px 32px rgba(15, 23, 42, 0.08);
}
#hobbies-section .visitor-panel {
  border-radius: 15px;
  background: linear-gradient(180deg, #ffffff 0%, #fbfcff 100%);
  padding: 18px 18px 14px;
}
#hobbies-section .visitor-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}
#hobbies-section .visitor-title-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}
#hobbies-section .visitor-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 11px;
  background: linear-gradient(135deg, #eff6ff, #f5f3ff);
  font-size: 21px;
  flex: 0 0 auto;
}
#hobbies-section .visitor-heading {
  font-weight: 700;
  color: #172033;
  font-size: 1.02em;
  line-height: 1.25;
}
#hobbies-section .visitor-subtitle {
  margin-top: 2px;
  color: #7a8498;
  font-size: 0.78em;
}
#hobbies-section .visitor-live {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 9px;
  border-radius: 999px;
  background: #ecfdf3;
  color: #247a4a;
  font-size: 0.74em;
  font-weight: 600;
  white-space: nowrap;
}
#hobbies-section .visitor-live::before {
  content: "";
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 0 3px rgba(34,197,94,.12);
}
#hobbies-section .visitor-map-frame {
  overflow: hidden;
  border: 1px solid #eef0f4;
  border-radius: 12px;
  background: #fff;
}
#hobbies-section .visitor-map-frame a {
  display: block;
  text-decoration: none;
}
#hobbies-section .visitor-map-frame img {
  display: block;
  width: 100%;
  height: auto;
  min-height: 180px;
  object-fit: contain;
  background: #fff;
}
#hobbies-section .visitor-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 11px;
  color: #778195;
  font-size: 0.76em;
  line-height: 1.5;
}
#hobbies-section .visitor-meta a {
  color: #4f63b8;
  text-decoration: none;
  font-weight: 600;
}
#hobbies-section .visitor-meta a:hover {
  text-decoration: underline;
}
#hobbies-section .visitor-chips {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
#hobbies-section .visitor-chip {
  padding: 3px 8px;
  border-radius: 999px;
  background: #f4f6fa;
  color: #687386;
  border: 1px solid #edf0f5;
}
@media (max-width: 560px) {
  #hobbies-section .visitor-panel {
    padding: 14px 12px 12px;
  }
  #hobbies-section .visitor-head {
    align-items: flex-start;
  }
  #hobbies-section .visitor-live {
    padding: 4px 7px;
  }
  #hobbies-section .visitor-map-frame img {
    min-height: 130px;
  }
}
</style>

<div id="hobbies-section">

<div class="hobby-grid">

<div class="hobby-card">
  <div class="hobby-title">🎤 Singing</div>
  <div class="hobby-desc">Love belting out tunes and exploring different music styles. Certified in <a href="/docs/berklee_singing_popular_music_cert.png">Singing Popular Music</a> by Berklee College of Music.</div>
</div>

<div class="hobby-card">
  <div class="hobby-title">🍳 Cooking</div>
  <div class="hobby-desc">Always experimenting with new recipes — my kitchen is my lab!</div>
</div>

<div class="hobby-card">
  <div class="hobby-title">🏸 Sports</div>
  <div class="hobby-desc">Into badminton, basketball, and table tennis. Also hitting the gym as a total newbie!</div>
</div>

<div class="hobby-card">
  <div class="hobby-title">🎲 Board Games</div>
  <div class="hobby-desc">Obsessed with Splendor, Catan, Ticket to Ride, Azul, 7 Wonders, Carcassonne, and Wingspan. Game night anyone?</div>
</div>

<div class="hobby-card">
  <div class="hobby-title">⛰️ Hiking & Traveling</div>
  <div class="hobby-desc">Love chasing sunrises on mountain peaks. Explored Huangshan, Jiuhuashan, Zhuhai, Changsha, Istanbul, Morocco's Sahara, Seoul, and Singapore.</div>
</div>

<div class="hobby-card">
  <div class="hobby-title">🎮 <a href="/docs/王者荣耀.png">Gaming</a></div>
  <div class="hobby-desc">Not just building Honor of Kings (Lingbao developer!) but rocking National Server Nezha, Golden Badge Nakoruru, and ranked Top 50 Jungler in Hefei.</div>
</div>

</div>

<p class="cta-text">Feel free to hit me up for karaoke, board games, badminton, hiking, or just grabbing food and chatting about life!</p>

<h1>📬 Let's Connect</h1>

<div class="connect-box">
  <h3>Get in Touch</h3>
  <p>📫 Email: <a href="mailto:cyd0806@mail.ustc.edu.cn">cyd0806@mail.ustc.edu.cn</a></p>
  <p>💼 I'm eager to connect with fellow deep learning enthusiasts and researchers passionate about advancing AI.</p>
  <p>📍 USTC Gaoxin campus, Hefei, Anhui, China</p>
</div>

<h1>Visitor Map 🌍</h1>

<div class="visitor-shell">
  <div class="visitor-panel">
    <div class="visitor-head">
      <div class="visitor-title-wrap">
        <span class="visitor-icon">🌐</span>
        <div>
          <div class="visitor-heading">Visitors Worldwide</div>
          <div class="visitor-subtitle">Live geographic traffic from this homepage</div>
        </div>
      </div>
      <span class="visitor-live">LIVE</span>
    </div>

    <div class="visitor-map-frame">
      <a href="https://info.flagcounter.com/ydchen0806" target="_blank" rel="noopener noreferrer" aria-label="Open detailed visitor statistics">
        <img src="https://s11.flagcounter.com/map/ydchen0806/size_xl/txt_475467/border_F2F4F7/pageviews_1/viewers_Global+Visitors/flags_1/" alt="Worldwide visitor map with pageview and country statistics" decoding="async"/>
      </a>
    </div>

    <div class="visitor-meta">
      <div class="visitor-chips">
        <span class="visitor-chip">Page views</span>
        <span class="visitor-chip">Countries</span>
        <span class="visitor-chip">Geo statistics</span>
      </div>
      <a href="https://info.flagcounter.com/ydchen0806" target="_blank" rel="noopener noreferrer">Recent visitors & detailed stats →</a>
    </div>
  </div>
</div>

<!-- Legacy ClustrMaps widget kept for reference only.
<div class="visitor-map clustrmaps-globe">
  <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=-6dpgBBQ6VS019wttjE8HshiwnZUQM6hxMNnvZM-u6c"></script>
</div>
-->

</div>

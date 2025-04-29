import React, { useState, useEffect } from "react";
import NewsList from "./components/NewsList";
import NewsDetail from "./components/NewsDetail";
import "./components/ResponsiveLayout.css";

export interface NewsItem {
  category: string;
  code: string;
  title: string;
  caption: string;
  link: string;
  pubdate: string;
  tags: string[];
  thumbnail: string | null;
  content: string;
}

const App: React.FC = () => {
  const [menuOpen, setMenuOpen] = useState(true);
  const [newsList, setNewsList] = useState<NewsItem[]>([]);
  const [selectedNews, setSelectedNews] = useState<NewsItem | null>(null);

  const groupMap: { [key: string]: string } = {
    N: "Nogizaka46",
    K: "Keyakizaka46",
    S: "Sakurazaka46",
    H: "Hinatazaka46",
  };
  const kanji: { [key: string]: string } = {
    Nogizaka46: "乃木坂46",
    Keyakizaka46: "欅坂46",
    Sakurazaka46: "櫻坂46",
    Hinatazaka46: "日向坂46",
  };

  let init_year = 0
  let init_month = 0
  let init_group = "Nogizaka46";
  const init_hash = window.location.hash.substring(1); // 获取 URL 的 hash 部分
  if (init_hash) {
    const init_parts = init_hash.split("-");
    init_group = init_parts[0];
    const init_yearMonth = init_parts[1];
    init_year = parseInt(init_yearMonth.slice(0, 4));
    init_month = parseInt(init_yearMonth.slice(4, 6));
  }
  const [group, setGroup] = useState<string>(init_group || "Nogizaka46");
  const [year, setYear] = useState<number>(init_year || new Date().getFullYear());
  const [month, setMonth] = useState<number>(init_month || new Date().getMonth() + 1);

  // 监听 hash 改变，加载对应的数据
  useEffect(() => {
    const hash = window.location.hash.substring(1); // 获取 URL 的 hash 部分
    if (hash) {
      const parts = hash.split("-");
      if (parts.length === 2) {
        // 格式: group-yearmonth
        const groupFromUrl = parts[0];
        const yearMonth = parts[1];
        const year = parseInt(yearMonth.slice(0, 4));
        const month = parseInt(yearMonth.slice(4, 6));

        setGroup(groupFromUrl);
        setYear(year);
        setMonth(month);
      } else if (parts.length === 3) {
        // 格式: group-yearmonth-code
        const groupFromUrl = parts[0];
        const yearMonth = parts[1];
        const code = parts[2];

        const year = parseInt(yearMonth.slice(0, 4));
        const month = parseInt(yearMonth.slice(4, 6));

        setGroup(groupFromUrl); // 确保首字母大写
        setYear(year);
        setMonth(month);
        console.log(year, month)
        const url = `${groupFromUrl}-${year}${yearMonth.slice(4)}.json`;
        fetch(url)
          .then((response) => response.json())
          .then((data) => {
            setNewsList(data.news);
            const news = data.news.find((newsItem: NewsItem) => newsItem.code === code);
            setSelectedNews(news || null);
          })
          .catch((error) => console.error("Error fetching JSON:", error));
        setMenuOpen(!menuOpen)
      }
    }
  }, []); // 页面首次加载时

  // 监听 group, year, month 更新，更新 URL 和数据
  useEffect(() => {
    const url = `${group}-${year}${String(month).padStart(2, "0")}.json`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setNewsList(data.news);
      })
      .catch((error) => console.error("Error fetching JSON:", error));

    // 更新 URL 中的 hash
    const hash = window.location.hash.substring(1);
    const parts = hash.split("-");
    if (parts.length === 3) {
      window.location.hash = `${group}-${year}${String(month).padStart(2, "0")}-${parts[2]}`;
    }
    else {
      window.location.hash = `${group}-${year}${String(month).padStart(2, "0")}`;
    }

  }, [group, year, month]); // 当 group, year, month 改变时重新加载数据

  // 处理点击新闻
  const handleSelectNews = (news: NewsItem) => {
    setSelectedNews(news);
    setMenuOpen(!menuOpen)
    window.location.hash = `${group}-${year}${String(month).padStart(2, "0")}-${news.code}`; // 更新 URL 中的 hash
  };

  return (
    <div className="responsive-layout">
      <button className={`menu-toggle ${menuOpen ? "menu-open" : ""}`} onClick={() => setMenuOpen(!menuOpen)}>
        ☰
      </button>
      <div className={`mobile-title ${menuOpen ? "menu-open" : ""}`}>
        {kanji[group]}<br></br>{year}年{month}月
      </div>
      <div className={`sidebar ${menuOpen ? "menu-open" : ""}`}>
        <div className="sticky-filters-container">
          <div className="sticky-filters">
            <div className="group-selector">
              <select
                value={group}
                onChange={(e) => setGroup(e.target.value)}
                className="group-dropdown"
              >
                {Object.entries(groupMap).map(([letter, groupName]) => (
                  <option key={letter} value={groupName}>
                    {kanji[groupName]}
                  </option>
                ))}
              </select>
            </div>
            <div className="filters">
              <select value={year} onChange={(e) => setYear(parseInt(e.target.value))}>
                {Array.from({ length: new Date().getFullYear() - 2010 + 1 }, (_, i) => 2010 + i)
                  .map((yr) => (
                    <option key={yr} value={yr}>
                      {yr}年
                    </option>
                  ))}
              </select>
              <select value={month} onChange={(e) => setMonth(parseInt(e.target.value))}>
                {Array.from({ length: 12 }, (_, i) => i + 1).map((m) => (
                  <option key={m} value={m}>
                    {m}月
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>
        <div className="news-list">
          <NewsList newsList={newsList} onSelect={handleSelectNews} />
        </div>
      </div>
      <div className={`detail ${menuOpen ? "menu-open" : ""}`}>
        <NewsDetail news={selectedNews} />
      </div>
    </div>
  );
};

export default App;

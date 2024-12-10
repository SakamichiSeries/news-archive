import React, { useState, useEffect } from "react";
import NewsList from "./components/NewsList";
import NewsDetail from "./components/NewsDetail";
import "./components/ResponsiveLayout.css";

interface NewsItem {
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
  const [newsList, setNewsList] = useState<NewsItem[]>([]);
  const [selectedNews, setSelectedNews] = useState<NewsItem | null>(null);

  // 映射字母到对应组名
  const groupMap: { [key: string]: string } = {
    N: "nogizaka46",
    K: "keyakizaka46",
    S: "sakurazaka46",
    H: "hinatazaka46",
  };
  const [group, setGroup] = useState<string>("nogizaka46");
  const [year, setYear] = useState<number>(new Date().getFullYear());
  const [month, setMonth] = useState<number>(new Date().getMonth() + 1);

  useEffect(() => {
    const url = `${group}-${year}${String(month).padStart(2, "0")}.json`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setNewsList(data.news);
        setSelectedNews(data.news[0]);
      })
      .catch((error) => console.error("Error fetching JSON:", error));
  }, [group, year, month]);

  return (
    <div className="responsive-layout">
      <div className="sidebar">
        <div className="group-selector">
          {Object.entries(groupMap).map(([letter, groupName]) => (
            <button
              key={letter}
              className={`group-button ${group === groupName ? "active" : ""}`}
              onClick={() => setGroup(groupName)}
            >
              {letter}
            </button>
          ))}
        </div>
        <div className="filters">
          <select
            value={year}
            onChange={(e) => setYear(parseInt(e.target.value))}
          >
            {Array.from(
              { length: new Date().getFullYear() - 2010 + 1 },
              (_, i) => 2010 + i
            ).map((yr) => (
              <option key={yr} value={yr}>
                {yr}
              </option>
            ))}
          </select>
          <select
            value={month}
            onChange={(e) => setMonth(parseInt(e.target.value))}
          >
            {Array.from({ length: 12 }, (_, i) => i + 1).map((m) => (
              <option key={m} value={m}>
                {m}月
              </option>
            ))}
          </select>
        </div>
        <NewsList newsList={newsList} onSelect={setSelectedNews} />
      </div>
      <div className="detail">
        <NewsDetail news={selectedNews} />
      </div>
    </div>
  );
};

export default App;
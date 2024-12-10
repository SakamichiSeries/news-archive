import React, { useState, useEffect } from "react";
import NewsList from "./components/NewsList";
import NewsDetail from "./components/NewsDetail";
import "./components/ResponsiveLayout.css"; // Corrected the import path

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

  useEffect(() => {
    // Replace with your dynamic URL
    const group = "nogizaka46";
    const yyyy = "2023";
    const mm = "09";
    const url = `${group}-${yyyy}${mm}.json`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setNewsList(data.news);
        setSelectedNews(data.news[0]); // Select the first news item by default
      })
      .catch((error) => console.error("Error fetching JSON:", error));
  }, []);

  return (
    <div className="responsive-layout">
      <NewsList newsList={newsList} onSelect={setSelectedNews} />
      <NewsDetail news={selectedNews} />
    </div>
  );
};

export default App; // Corrected the export syntax

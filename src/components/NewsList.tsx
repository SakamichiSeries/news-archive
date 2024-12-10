import React from "react";
import { NewsItem } from "../App"; // 导入 NewsItem 类型

interface NewsListProps {
  newsList: NewsItem[];
  onSelect: (news: NewsItem) => void;
}

const NewsList: React.FC<NewsListProps> = ({ newsList, onSelect }) => {
  return (
    <div className="news-list">
      {newsList.map((news) => (
        <div
          key={news.code}
          className="news-item"
          onClick={() => onSelect(news)}
          id={news.code}
        >
          <div className="news-title">{news.title}</div>
          <div className="news-date">{new Date(news.pubdate).toLocaleDateString()}</div>
        </div>
      ))}
    </div>
  );
};

export default NewsList;

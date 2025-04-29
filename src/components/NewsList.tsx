import React from "react";
import { NewsItem } from "../App"; // Make sure the NewsItem type is imported from the App.tsx file

interface NewsListProps {
  newsList: NewsItem[];
  onSelect: (newsItem: NewsItem) => void; // Specify the type of the parameter here
}

const NewsList: React.FC<NewsListProps> = ({ newsList, onSelect }) => {
  return (
    <div>
      {newsList.map((news) => (
        <div
          key={news.code}
          className="news-item"
          onClick={() => onSelect(news)}
          id={news.code}

        >
          <div className="news-date">{new Date(news.pubdate).toLocaleDateString()}</div>
          <div className="news-title">{news.title}</div>
          
        </div>
      ))}
      <div className="mobile-extra-space"></div>
    </div>
  );
};

export default NewsList;

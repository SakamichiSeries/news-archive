import React from "react";

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

interface NewsListProps {
  newsList: NewsItem[];
  onSelect: (news: NewsItem) => void;
}

const NewsList: React.FC<NewsListProps> = ({ newsList, onSelect }) => {
  return (
    <div className="news-list">
      <h3>News List</h3>
      <ul>
        {newsList.map((news) => (
          <li key={news.code} onClick={() => onSelect(news)}>
            {news.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsList;

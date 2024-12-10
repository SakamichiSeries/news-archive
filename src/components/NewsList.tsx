import React from "react";
import { NewsItem } from "../App"; // Make sure the NewsItem type is imported from the App.tsx file

interface NewsListProps {
  newsList: NewsItem[];
  onSelect: (newsItem: NewsItem) => void; // Specify the type of the parameter here
}

const NewsList: React.FC<NewsListProps> = ({ newsList, onSelect }) => {
  return (
    <div>
      {newsList.map((newsItem) => (
        <div key={newsItem.code} onClick={() => onSelect(newsItem)}>
          {newsItem.title}
        </div>
      ))}
    </div>
  );
};

export default NewsList;

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

interface NewsDetailProps {
  news: NewsItem | null;
}

const NewsDetail: React.FC<NewsDetailProps> = ({ news }) => {
  if (!news) {
    return <div className="news-detail">Select a news item to view details</div>;
  }

  return (
    <div className="news-detail">
      <h3>{news.title}</h3>
      <p dangerouslySetInnerHTML={{ __html: news.content }}></p>
      <a href={news.link} target="_blank" rel="noopener noreferrer">
        Read more
      </a>
    </div>
  );
};

export default NewsDetail;

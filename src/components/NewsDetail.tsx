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
    return <div className="news-detail">ニュースを一つ選んで見てください。</div>;
  }

  return (
    <div className="news-detail">
      <h1>{news.title}</h1>
      <p className="news-date">{news.pubdate}</p> {/* 显示发布日期 */}
      <div className="news-caption">{news.caption}</div>
      {/* 使用 dangerouslySetInnerHTML 渲染 HTML 内容 */}
      <div className="news-content" dangerouslySetInnerHTML={{ __html: news.content }} />
      {news.thumbnail && <img src={news.thumbnail} alt={news.title} />}
      <br></br><br></br><br></br>
      <a href={news.link} target="_blank" rel="noopener noreferrer">公式サイトで開く</a>
      <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
    </div>
  );
};

export default NewsDetail;

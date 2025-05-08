// Display  paginated list of web scraped articles with search and filter options
import React, { useState, useEffect } from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import ArticleItem from '../components/ArticleItem'
import axios from 'axios'

export default function ArticlesList({ articles, setArticles }) {
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState('');

  // Fetch articles from DB
  const fetchArticles = async () => {
    setLoading(true);
    setMsg('');
    try {
      const response = await axios.get('/articles');
      setArticles(response.data.articles);
      setMsg('Articles loaded!');
    } catch (err) {
      setMsg('Failed to load articles.');
    }
    setLoading(false);
  };

  // Scrape and save articles, then fetch from DB
  const handleScrape = async () => {
    setLoading(true);
    setMsg('');
    try {
      await axios.post('/scrape_articles');
      setMsg('Articles scraped and saved!');
      await fetchArticles();
    } catch (err) {
      setMsg('Scraping failed.');
    }
    setLoading(false);
  };

  return (
    <>
      <NavBar />
      <div className='place-items-center'>
        <div className='grow text-2xl'>List of Articles</div>
        <button className="btn btn-primary mb-4" onClick={handleScrape} disabled={loading}>
          {loading ? 'Working...' : 'Scrape & Load Latest Articles'}
        </button>
        <button className="btn btn-secondary mb-4 ml-2" onClick={fetchArticles} disabled={loading}>
          {loading ? 'Loading...' : 'Load Articles Only'}
        </button>
        {msg && <div>{msg}</div>}
        <ul>
          {articles.map((article, idx) => (
            <li key={idx}>
              <a href={article.link} target="_blank" rel="noopener noreferrer">{article.title}</a>
              {article.author && <> by {article.author}</>}
              {article.category && <> [{article.category}]</>}
            </li>
          ))}
        </ul>
      </div>
      <Footer />
    </>
  )
}

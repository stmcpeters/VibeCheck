// Display  paginated list of web scraped articles with search and filter options
import React, { useState } from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import ArticleItem from '../components/ArticleItem'
import axios from 'axios'

export default function ArticlesList({ articles, setArticles }) {
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const articlesPerPage = 5;

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

  // Calculate the current articles to display
  const indexOfLastArticle = currentPage * articlesPerPage;
  const indexOfFirstArticle = indexOfLastArticle - articlesPerPage;
  const currentArticles = articles.slice(indexOfFirstArticle, indexOfLastArticle);

    // Calculate total pages
  const totalPages = Math.ceil(articles.length / articlesPerPage);

  const handlePageChange = (newPage) => {
    if (newPage > 0 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
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
        <ArticleItem articles={currentArticles} />
        {/* Pagination */}
        <div className="join">
          <button
            className="join-item btn"
            onClick={() => handlePageChange(currentPage - 1)}
            disabled={currentPage === 1}
          >
            «
          </button>
          <span className="join-item btn btn-disabled">
            Page {currentPage} of {totalPages}
          </span>
          <button
            className="join-item btn"
            onClick={() => handlePageChange(currentPage + 1)}
            disabled={currentPage === totalPages}
          >
            »
          </button>
        </div>
      </div>
      <Footer />
    </>
  )
}

import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import UserAuth from './pages/UserAuth'  
import ErrorPage from './pages/ErrorPage'
import ArticlesList from './pages/ArticlesList'
import MoodLogsList from './pages/MoodLogsList'
import LogOut from './pages/LogOut'

function App() {
  const [articles, setArticles] = useState([]);

    // function to fetch data using axios from server
    const fetchArticles = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8080/articles');
        const data = response.data.articles;

        // transform the data into an array of objects
        const articles = data.map((article) => ({
          id: article[0],
          title: article[1],
          category: article[2],
          link: article[3],
          author: article[4],
        }));
    
        setArticles(articles);
      } catch (error) {
        console.error('Error fetching articles from database:', error);
    }
  }

  // useEffect will fetch data from server on initial page load
  useEffect(() => {
    fetchArticles();
  }, []);

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard articles={articles} />} />
          <Route path="/auth" element={<UserAuth />} />
          <Route path="/*" element={<ErrorPage />} />
          <Route path='/articles' element={<ArticlesList articles={articles} />} />
          <Route path='/logs' element={<MoodLogsList />} />
          <Route path='/logout' element={<LogOut />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App

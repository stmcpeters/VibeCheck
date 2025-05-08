import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'  
import Register from './pages/Register'
import ErrorPage from './pages/ErrorPage'
import ArticlesList from './pages/ArticlesList'
import MoodLogsList from './pages/MoodLogsList'
import LogOut from './pages/LogOut'


export default function App() {
  const [response, setResponse] = useState();
  const [mood_logs, setMoodLogs] = useState([]);
  const [articles, setArticles] = useState([]);
  const [user, setUser] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(null);

    // axios config
    // sets the base URL for axios to the server URL
    axios.defaults.baseURL = process.env.REACT_APP_API_URL;
    axios.defaults.withCredentials = true;

    // function to check if user is logged in using axios from server
    const checkLoggedIn = async () => {
      try {
        const response = await axios.get('/current_user');
        console.log('User is logged in:', response.data.user);
        setIsLoggedIn(true);
        setUser(response.data.user); 
      } catch (error) {
        console.error('Error checking login status:', error);
        setIsLoggedIn(false);
        setUser(null);
      }
    };

    // function to fetch data using axios from server
    const fetchAPI = async () => {
      try {
        const response = await axios.get('/');
        setResponse(response.data.message);
      } catch (error) {
        console.error('Error fetching data:', error);
        setResponse('Error fetching data');
    }
  }

    // function to fetch articles data using axios from server
    const fetchArticles = async () => {
      try {
        const response = await axios.get('/articles');
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
    
    // function to fetch mood logs using axios from server
    const fetchMoodLogs = async () => {
      try {
        const response = await axios.get('/mood_logs');
        const data = response.data.mood_logs;

        // transform the data into an array of objects
        const mood_logs = data.map((mood_log) => ({
          id: mood_log.id,
          emoji: mood_log.emoji,
          journal_entry: mood_log.journal_entry,
          sentiment_score: mood_log.sentiment_score,
          created_at: mood_log.created_at,
        }));

        setMoodLogs(mood_logs);
      } catch (error) {
        console.error('Error fetching mood logs:', error);
      }
    }

    // function to handle logout using axios from server
    const handleLogout = async () => {
      try {
        await axios.post('/logout');
        setIsLoggedIn(false);
        setUser(null);
      } catch (error) {
        console.error('Error logging out:', error);
      }
    };

    // useEffect will fetch data from server on initial page load
    useEffect(() => {
      checkLoggedIn();
      fetchAPI();
      fetchArticles();
      fetchMoodLogs();
    }, []);

    // console.log('isLoggedIn:', isLoggedIn);
    // console.log('user:', user);

  return (
    <>
      <BrowserRouter>
        <Routes>
        <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard mood_logs={mood_logs} articles={articles} />} />
          <Route path="/login" element={<Login setUser={setUser} />} />
          <Route path="/register" element={<Register />} />
          <Route path="/*" element={<ErrorPage />} />
          <Route path='/articles' element={<ArticlesList articles={articles} />} />
          <Route path='/logs' element={<MoodLogsList mood_logs={mood_logs} />} />
          <Route path='/logout' element={<LogOut setIsLoggedIn={setIsLoggedIn} setUser={setUser}/>} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

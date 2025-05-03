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

export default function App() {
  const [response, setResponse] = useState();
  const [mood_logs, setMoodLogs] = useState([]);

    // creates a variable to hold the base URL for the server
    const baseURL = 'http://127.0.0.1:8080/';

    // function to fetch data using axios from server
    const fetchAPI = async () => {
      try {
        const response = await axios.get(baseURL);
        setResponse(response.data.message);
      } catch (error) {
        console.error('Error fetching data:', error);
        setResponse('Error fetching data');
    }
  }
    // function to fetch mood logs using axios from server
    const fetchMoodLogs = async () => {
      try {
        const response = await axios.get(baseURL + 'mood_logs');
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

    // useEffect will fetch data from server on initial page load
    useEffect(() => {
      fetchAPI();
      fetchMoodLogs();
    }, []);

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard mood_logs={mood_logs} />} />
          <Route path="/auth" element={<UserAuth />} />
          <Route path="/*" element={<ErrorPage />} />
          <Route path='/articles' element={<ArticlesList />} />
          <Route path='/logs' element={<MoodLogsList mood_logs={mood_logs} />} />
          <Route path='/logout' element={<LogOut />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

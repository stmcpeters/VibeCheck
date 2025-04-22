import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'
import UserAuth from './pages/UserAuth'  
import ErrorPage from './pages/ErrorPage'
import ArticlesList from './pages/ArticlesList'
import EntriesList from './pages/EntriesList'
import LogOut from './pages/LogOut'

function App() {
  const [response, setResponse] = useState();

    // function to fetch data using axios from server
    const fetchAPI = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8080/');
        setResponse(response.data.message);
      } catch (error) {
        console.error('Error fetching data:', error);
        setResponse('Error fetching data');
    }
  }

  // useEffect will fetch data from server on initial page load
  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/auth" element={<UserAuth />} />
          <Route path="/*" element={<ErrorPage />} />
          <Route path='/articles' element={<ArticlesList />} />
          <Route path='/logs' element={<EntriesList />} />
          <Route path='/logout' element={<LogOut />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App

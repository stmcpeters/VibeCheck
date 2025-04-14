import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [response, setResponse] = useState();

  // function to fetch data using axios from server
  const fetchAPI = async () => {
    const response = await axios.get('http://127.0.0.1:8080/');
    setResponse(response.data.message);
  }

  // useEffect will fetch data from server on initial page load
  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <h1>Welcome to VibeCheck!</h1>
      <span>{response}</span>
    </>
  )
}

export default App

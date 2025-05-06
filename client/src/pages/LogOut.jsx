// log out successful page
import axios from 'axios'
import React, { useEffect } from 'react'
import Footer from '../components/Footer'
import { useNavigate } from 'react-router-dom'

export default function LogOut({ setIsLoggedIn, setUser }) {

  // useNavigate hook to navigate to different routes
  const navigate = useNavigate();

  // useEffect to call handleLogout when the component mounts
  useEffect(() => {
      // function to handle logout
  const handleLogout = async (e) => {
    try {
      await axios.post('/logout'); 
      setIsLoggedIn(false);
      setUser(null);
      navigate('/'); // redirect to home page
    } catch (error) {
      console.error('Error logging out:', error);
    }
  }
  
    handleLogout();
  }, []);

  return (
    <>
      <div
          className="hero min-h-screen"
          style={{
            backgroundImage: "url(https://preview.redd.it/missouri-clouds-are-unique-and-so-beautiful-no-edits-needed-v0-t7qmi11cu3ua1.jpg?width=1080&crop=smart&auto=webp&s=df1cdcc1780868ce05cfdacf911bc1e7eeddab2e)",
          }}>
          <div className="hero-overlay"></div>
          <div className="hero-content text-neutral-content text-center">
            <div className="max-w-md">
              <h1 className="mb-5 text-2xl font-bold">Logging out...</h1>
            </div>
          </div>
        </div>
      <Footer />
    </>
  )
}

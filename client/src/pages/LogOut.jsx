// log out successful page
import axios from 'axios'
import React from 'react'
import Footer from '../components/Footer'
export default function LogOut() {

  // function to handle logout
  const handleLogout = async (e) => {
    try {
      const response = await axios.post('/logout'); 
      console.log(response.data);
    } catch (error) {
      console.error('Error logging out:', error);
    }
  }

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
              <h1 className="mb-5 text-2xl font-bold">You've succesfully logged out!</h1>
              <button className="btn btn-primary"><a href="/">Back to Home</a></button>
            </div>
          </div>
        </div>
      <Footer />
    </>
  )
}

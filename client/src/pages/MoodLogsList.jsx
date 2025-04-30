// Displays paginated list of previous mood entries with search and filter options
import React from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import MoodLogItem from '../components/MoodLogItem'

export default function MoodLogsList({ mood_logs }) {
  return (
    <>
      <NavBar />
      <div className='place-items-center'>
        <div className='grow text-2xl'>List of Mood Logs</div>
        <MoodLogItem mood_logs={mood_logs} />
        {/* pagination */}
        <div className="join">
          <button className="join-item btn btn-disabled">«</button>
          <button className="join-item btn">Page 1</button>
          <button className="join-item btn">»</button>
        </div>
        {/* end of pagination */}
      </div>
      <Footer />
    </>
  )
}

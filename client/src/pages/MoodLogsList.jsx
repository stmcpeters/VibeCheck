// Displays paginated list of previous mood entries with search and filter options
import React, { useState } from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import MoodLogItem from '../components/MoodLogItem'

export default function MoodLogsList({ mood_logs }) {
  const [currentPage, setCurrentPage] = useState(1);
  const logsPerPage = 5;

  // Calculate the current mood logs to display
  const indexOfLastLog = currentPage * logsPerPage;
  const indexOfFirstLog = indexOfLastLog - logsPerPage;
  const currentMoodLogs = mood_logs.slice(indexOfFirstLog, indexOfLastLog);

  // Calculate total pages
  const totalPages = Math.ceil(mood_logs.length / logsPerPage);

  const handlePageChange = (newPage) => {
    if (newPage > 0 && newPage <= totalPages) {
      setCurrentPage(newPage);
    }
  };

  return (
    <>
      <NavBar />
      <div className='place-items-center'>
        <div className='grow text-2xl'>List of Mood Logs</div>
        <MoodLogItem mood_logs={currentMoodLogs} />
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
        {/* End of Pagination */}
        </div>
      <Footer />
    </>
  )
}

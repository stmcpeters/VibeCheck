// Displays paginated list of previous mood entries with search and filter options
import React, { useState, useEffect } from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import MoodLogItem from '../components/MoodLogItem'

export default function MoodLogsList({ mood_logs: initialMoodLogs }) {
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [mood_logs, setMoodLogs] = useState(initialMoodLogs);

  // Reset currentPage to 1 when mood_logs changes
  useEffect(() => {
    setCurrentPage(1);
  }, [mood_logs]);

  const logsPerPage = 5;

    // useEffect to set loadingMoodLogs to false after mood logs are loaded
    useEffect(() => {
    if (mood_logs.length > 0) {
      setLoading(false);
    }
  }, [mood_logs]);

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

  const handleDelete = (id) => {
    setMoodLogs(mood_logs.filter((log) => log.id !== id)); 
  };

  const handleUpdate = (updatedLog) => {
    setMoodLogs(
      mood_logs.map((log) =>
        log.id === updatedLog.id ? updatedLog : log
      )
    );
  };

  return (
    <>
      <NavBar />
      <div className='place-items-center'>
        <div className='grow text-2xl'>List of Mood Logs</div>
        {loading ? (
          <p>Loading mood logs...</p>
        ) : (
          <MoodLogItem mood_logs={currentMoodLogs} onDelete={handleDelete} onUpdate={handleUpdate}/>
        )}
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

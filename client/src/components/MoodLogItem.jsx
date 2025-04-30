// Individual mood entry showing emoji, journal, sentiment score, and edit/delete buttons
import React from 'react'

export default function MoodLogItem({ mood_logs }) {
    // console.log(articles);
    if (!mood_logs || mood_logs.length === 0) {
      return <p>No mood logs available.</p>;
    }

    console.log(mood_logs[0].created_at);
  return (
    <>
      <div className="overflow-x-auto">
        <table className="table">
          {/* head */}
          <thead>
            <tr>
              <th>Created At</th>
              <th>Emoji</th>
              <th>Journal Entry</th>
              <th>Sentiment Score</th>
              <th colSpan={2}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {/* row 1 */}
            {mood_logs.map((mood_log, index) => (
                <tr key={mood_log.index} className="hover:bg-base-300">
                  <td>{new Date(mood_log.created_at).toLocaleDateString('en-US', { month: '2-digit', day: '2-digit', year: 'numeric' })}</td>
                  <td>{mood_log.emoji_id}</td>
                  <td>{mood_log.journal_entry}</td>
                  <td>{mood_log.sentiment_score}</td>
                  <td className='pr-5 pl-5'>
                    <button className="btn btn-square">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M20 14.66V20a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h5.34"></path><polygon points="18 2 22 6 12 16 8 16 8 12 18 2"></polygon></svg>
                    </button>
                    <button className="btn btn-square">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
                    </button>
                  </td>
                </tr>
              )
            )}
          </tbody>
        </table>
      </div>
  </>
  )
}

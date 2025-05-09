// Individual mood entry showing emoji, journal, sentiment score, and edit/delete buttons
import React, { useState } from 'react'
import axios from 'axios';

export default function MoodLogItem({ mood_logs, onDelete, onUpdate }) {
  console.log('onUpdate prop', onUpdate);
  console.log('onDelete prop', onDelete);

  
  const [editingLog, setEditingLog] = useState(null); // Track the log being edited
  const [updatedEmojiId, setUpdatedEmojiId] = useState(null);
  const [updatedJournalEntry, setUpdatedJournalEntry] = useState('');

    // console.log(articles);
    if (!mood_logs || mood_logs.length === 0) {
      return <p>No mood logs available.</p>;
    }

  // handle delete
  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this mood log?')) {
      try {
        await axios.delete(`/delete_mood_log/${id}`);
        onDelete(id); 
      } catch (error) {
        console.error('Error deleting mood log:', error);
        alert('Failed to delete mood log. Please try again.');
      }
    }
  };

  const handleUpdate = async (id) => {
    try {
      if (!updatedEmojiId || !updatedJournalEntry) {
        alert('Both emoji and journal entry are required.');
        return;
      }

      const response = await axios.put(`/update_mood_log/${id}`, {
        emoji_id: updatedEmojiId,
        journal_entry: updatedJournalEntry,
      });

      const updatedLog = response.data; // Assuming the backend returns the updated log
      onUpdate(updatedLog); // Pass the updated log to the parent component
      setEditingLog(null); // Exit edit mode
    } catch (error) {
      console.error('Error updating mood log:', error);
      alert('Failed to update mood log. Please try again.');
    }
  };

  return (
    <div className="overflow-x-auto">
      <table className="table">
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
          {mood_logs.map((mood_log) => (
            <tr key={mood_log.id} className="hover:bg-base-300">
              <td>
                {new Date(mood_log.created_at).toLocaleDateString('en-US', {
                  month: '2-digit',
                  day: '2-digit',
                  year: 'numeric',
                })}
              </td>
              <td>
                {editingLog === mood_log.id ? (
                  <input
                    type="text"
                    className="input input-bordered input-sm"
                    value={updatedEmojiId || ''}
                    onChange={(e) => setUpdatedEmojiId(e.target.value)}
                  />
                ) : (
                  mood_log.emoji
                )}
              </td>
              <td>
                {editingLog === mood_log.id ? (
                  <textarea
                    className="textarea textarea-bordered textarea-sm w-full"
                    value={updatedJournalEntry || ''}
                    onChange={(e) => setUpdatedJournalEntry(e.target.value)}
                  ></textarea>
                ) : (
                  mood_log.journal_entry
                )}
              </td>
              <td>
                {mood_log.sentiment_score !== null ? mood_log.sentiment_score : 'N/A'}
              </td>
              <td>
                {editingLog === mood_log.id ? (
                  <>
                    <button className="btn btn-outline btn-info" onClick={() => handleUpdate(mood_log.id)}>
                      Save
                    </button>
                    <button className="btn btn-outline btn-secondary" onClick={() => setEditingLog(null)}>
                      Cancel
                    </button>
                  </>
                ) : (
                  <>
                    <button
                      className="btn btn-square btn-sm mr-2"
                      onClick={(e) => {
                        e.stopPropagation();
                        handleDelete(mood_log.id);
                      }}
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <polyline points="3 6 5 6 21 6"></polyline>
                        <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                        <line x1="10" y1="11" x2="10" y2="17"></line>
                        <line x1="14" y1="11" x2="14" y2="17"></line>
                      </svg>
                    </button>
                    <button
                      className="btn btn-square btn-sm"
                      onClick={(e) => {
                        e.stopPropagation();
                        setEditingLog(mood_log.id);
                        setUpdatedEmojiId(mood_log.emoji);
                        setUpdatedJournalEntry(mood_log.journal_entry);
                      }}
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M12 20h9"></path>
                        <path d="M16.5 3.5a2.121 2.121 0 1 1 3 3L7 19l-4 1 1-4Z"></path>
                      </svg>
                    </button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
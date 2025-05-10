// Emoji selection, journal textarea, AI-generated prompt (uses OpenAI), and submit button
import React, { useState } from 'react'
import axios from 'axios'

export default function MoodForm({ userId, onSuccess }) {
  const [emojiId, setEmojiId] = useState(null); 
  const [journalEntry, setJournalEntry] = useState(''); 
  const [sentimentScore, setSentimentScore] = useState(null); 
  const [error, setError] = useState(null); 
  const [success, setSuccess] = useState(false); 

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);

    if (!emojiId) {
      setError('Please select an emoji to represent your mood.');
      return;
    }

    try {
      const response = await axios.post('/add_mood_log', {
        user_id: userId || null,
        emoji_id: emojiId,
        journal_entry: journalEntry,
        sentiment_score: sentimentScore,
      });

      if (response.status === 200) {
        setSuccess(true);
        setJournalEntry(''); // Clear the form
        setEmojiId(null);
        setSentimentScore(null);
        if (onSuccess) onSuccess(); // Trigger callback to refresh mood logs
      }
    } catch (err) {
      setError('Failed to save mood log. Please try again.');
    }
  };
  return (
    <>
      <div className="card bg-primary text-primary-content w-96">
        <div className="card-body">
          <h2 className="card-title">How are you feeling today?</h2>
          <form onSubmit={handleSubmit}>
            <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
              <div className="join heading">
                <button
                type="button"
                className={`btn join-item p-5 ${emojiId === 1 ? 'btn-success' : ''}`}
                onClick={() => setEmojiId(1)}
                >
                  😀
                </button>
                <button
                  type="button"
                  className={`btn join-item p-5 ${emojiId === 2 ? 'btn-info' : ''}`}
                  onClick={() => setEmojiId(2)}
                >
                  😐
                </button>
                <button
                  type="button"
                  className={`btn join-item p-5 ${emojiId === 3 ? 'btn-error' : ''}`}
                  onClick={() => setEmojiId(3)}
                >
                  ☹️
                </button>
              </div>
            </fieldset>
            <fieldset className="fieldset">
              <textarea 
                className="textarea h-24" 
                placeholder="Enter your entry here" 
                value={journalEntry}
                onChange={(e) => setJournalEntry(e.target.value)}
              ></textarea>
            </fieldset>
            <div className="heading">
              <button type="reset" className="btn btn-block m-2.5 btn-info" onClick={() => setJournalEntry('')}>
              Reset
              </button>
              <button type="submit" className="btn btn-block m-2.5 btn-success">
                Save
              </button>
            </div>
          </form>
          {error && <p className="text-error">{error}</p>}
          {success && <p className="text-success">Mood log saved successfully!</p>}
        </div>
      </div>
    </>
  )
}

// Emoji selection, journal textarea, AI-generated prompt (uses OpenAI), and submit button
import React from 'react'

export default function MoodForm() {
  return (
    <>
      <div className="card bg-primary text-primary-content w-96">
        <div className="card-body">
          <h2 className="card-title">Create a new mood log!</h2>
          <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
            {/* <legend className="fieldset-legend">How are you feeling today?</legend> */}
            <label className="label">Emoji mood</label>
            <div className="join heading">
              <button className="btn join-item p-5 btn-success">😀</button>
              <button className="btn join-item p-5 btn-info">😐</button>
              <button className="btn join-item p-5 btn-error">☹️</button>
            </div>
          </fieldset>
          <fieldset className="fieldset">
            <legend className="fieldset-legend">This is an AI generated journal prompt</legend>
            <textarea className="textarea h-24" placeholder="Enter your entry here"></textarea>
            <div className="label">Optional</div>
          </fieldset>
          <div className="heading">
              <button className="btn btn-block m-2.5 btn-info">Cancel</button>
              <button className="btn btn-block m-2.5 btn-success">Save</button>
              <button className="btn btn-block m-2.5 btn-error">Reset</button>
            </div>
        </div>
      </div>
    </>
  )
}

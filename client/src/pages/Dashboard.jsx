// Landing page after login. Displays current mood prompt, mood streaks, and Tableau chart
import React, { useState, useEffect } from "react"
import NavBar from "../components/NavBar"
import Footer from "../components/Footer"
import MoodForm from "../components/MoodForm"
import SearchBar from "../components/SearchBar"
import Chart from "../components/Chart"
import ArticleItem from "../components/ArticleItem"
import MoodLogItem from "../components/MoodLogItem"

export default function Dashboard({ userId, mood_logs, articles }) {
  const [loadingArticles, setLoadingArticles] = useState(true);
  const [loadingMoodLogs, setLoadingMoodLogs] = useState(true);

  // creates variable to hold the 2 most recent mood logs to be displayed on the dashboard
  const sortedMoodLogs = mood_logs.sort((a,b) => new Date(b.created_at) - new Date(a.created_at)).slice(0,2);

  // creates variable to hold the 2 articles to be displayed on the dashboard
  const featuredArticles = articles.slice(0,3);

  // useEffect to set loadingArticles to false after articles are loaded
  useEffect(() => {
  if (articles.length > 0) {
    setLoadingArticles(false);
  }
}, [articles]);

  // useEffect to set loadingMoodLogs to false after mood logs are loaded
  useEffect(() => {
  if (mood_logs.length > 0) {
    setLoadingMoodLogs(false);
  }
}, [mood_logs]);
  
  return (
    <>
      <NavBar />
      <SearchBar />
      <br />
      <hr />
      <br />
      <div className="flex w-full">
        <div className="card rounded-box grid h-100 grow place-items-center">
          <Chart />
        </div>
        <div className="divider divider-horizontal"></div>
        <div className="card rounded-box grid h-150 grow place-items-center">
          <MoodForm userId={userId} onSuccess={() => console.log('Mood log saved!')} />
        </div>
      </div>
      <hr />
      <div className="flex w-full">
        <div className="card rounded-box grid h-100 grow place-items-center">
          <h1>Most Recent Web Scraped Articles</h1>
          {loadingArticles ? (
            <p>Loading articles...</p>
          ):(
          <ArticleItem articles={featuredArticles} />)
          }
        </div>
        <div className="divider divider-horizontal"></div>
        <div className="card rounded-box grid h-100 grow place-items-center">
          <h1>Recent Mood Logs</h1>
          {loadingMoodLogs ? (
            <p>Loading mood logs...</p>
          ):(
          <MoodLogItem mood_logs={sortedMoodLogs} />)
          }
        </div>
      </div>
      <Footer />
    </>
  )
}
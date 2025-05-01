// Landing page after login. Displays current mood prompt, mood streaks, and Tableau chart
import NavBar from "../components/NavBar"
import Footer from "../components/Footer"
import MoodForm from "../components/MoodForm"
import SearchBar from "../components/SearchBar"
import Chart from "../components/Chart"
import ArticleItem from "../components/ArticleItem"
import MoodLogItem from "../components/MoodLogItem"

export default function Dashboard({ articles }) {
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
          <MoodForm />
        </div>
      </div>
      <hr />
      <div className="flex w-full">
        <div className="card rounded-box grid h-100 grow place-items-center">
          <h1>Most Recent Web Scraped Articles</h1>
          <ArticleItem articles={articles.slice(0,3)} />
        </div>
        <div className="divider divider-horizontal"></div>
        <div className="card rounded-box grid h-100 grow place-items-center">
          <h1>Recent Mood Logs</h1>
          <MoodLogItem />
        </div>
      </div>
      <Footer />
    </>
  )
}
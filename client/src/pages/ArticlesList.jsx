// Display  paginated list of web scraped articles with search and filter options
import React from 'react'
import NavBar from '../components/NavBar'
import Footer from '../components/Footer'
import ArticleItem from '../components/ArticleItem'

export default function ArticlesList({ articles }) {
  return (
    <>
      <NavBar />
      <div className='place-items-center'>
        <div className='grow text-2xl'>List of Articles</div>
        <ArticleItem articles={articles} />
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

// Display web scraped articles
import React from 'react'

export default function ArticleItem({articles}) {
  // console.log(articles);
  if (!articles || articles.length === 0) {
    return <p>No articles available.</p>;
  }
  return (
    <>
      <div className="overflow-x-auto">
        <table className="table">
          {/* head */}
          <thead>
            <tr>
              <th>Category</th>
              <th>Article Title</th>
              <th>Author</th>
              <th colSpan={2}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {/* row 1 */}
            {articles.map((article, index) => (
                <tr key={article.id} className="hover:bg-base-300">
                  <td>{article.category}</td>
                  <td><a href={article.link} target='_blank'>{article.title}</a></td>
                  <td>{article.author}</td>
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


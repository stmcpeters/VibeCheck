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
            </tr>
          </thead>
          <tbody>
            {/* row 1 */}
            {articles.map((article, index) => (
                <tr key={article.id} className="hover:bg-base-300">
                  <td>{article.category}</td>
                  <td><a href={article.link} target='_blank' rel="noopener noreferrer">{article.title}</a></td>
                  <td>{article.author}</td>
                </tr>
              )
            )}
          </tbody>
        </table>
      </div>
    </>
  )
}


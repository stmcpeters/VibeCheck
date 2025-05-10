// serves as the main page before a user signs in

export default function Home() {
  return (
    <>
      <div
          className="hero min-h-screen"
          style={{
            backgroundImage: "url(https://preview.redd.it/missouri-clouds-are-unique-and-so-beautiful-no-edits-needed-v0-t7qmi11cu3ua1.jpg?width=1080&crop=smart&auto=webp&s=df1cdcc1780868ce05cfdacf911bc1e7eeddab2e)",
          }}>
          <div className="hero-overlay"></div>
          <div className="hero-content text-neutral-content text-center">
            <div className="max-w-md">
              <h1 className="mb-5 text-5xl font-bold">Welcome to VibeCheck!</h1>
              <button className="btn btn-primary"><a href="/login">Login</a></button>
              <button className="btn btn-primary ml-5"><a href="/register">Register</a></button>
            </div>
          </div>
        </div>
    </>
  )
}
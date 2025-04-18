// Forms for email/password login and registration. Includes OAuth Google login button and CAPTCHA checkbox
import NavBar from "../components/NavBar"
import Footer from "../components/Footer"

export default function UserAuth() {
  return (
    <>
    <NavBar />
    <div className="flex w-full">
      <div className="card bg-base-300 rounded-box grid h-100 grow place-items-center">
        <fieldset className="fieldset w-xs bg-base-200 border border-base-300 p-4 rounded-box">
        <legend className="fieldset-legend">Login</legend>
        
        <label className="fieldset-label">Email</label>
        <input type="email" className="input" placeholder="Email" />
        
        <label className="fieldset-label">Password</label>
        <input type="password" className="input" placeholder="Password" />
        
        <button className="btn btn-neutral mt-4">Login</button>
        </fieldset>
      </div>
      <div className="divider divider-horizontal"></div>
      <div className="card bg-base-300 rounded-box grid h-100 grow place-items-center">
        <fieldset className="fieldset w-xs bg-base-200 border border-base-300 p-4 rounded-box">
          <legend className="fieldset-legend">Register</legend>
          
          <label className="fieldset-label">Email</label>
          <input type="email" className="input" placeholder="Email" />
          
          <label className="fieldset-label">Password</label>
          <input type="password" className="input" placeholder="Password" />
          
          <button className="btn btn-neutral mt-4">Register</button>
        </fieldset>
      </div>
    </div>
    <Footer />
    </>
  )
}
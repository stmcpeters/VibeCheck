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
        {/* Google */}
        <button className="btn bg-white text-black border-[#e5e5e5]">
          <svg aria-label="Google logo" width="16" height="16" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><g><path d="m0 0H512V512H0" fill="#fff"></path><path fill="#34a853" d="M153 292c30 82 118 95 171 60h62v48A192 192 0 0190 341"></path><path fill="#4285f4" d="m386 400a140 175 0 0053-179H260v74h102q-7 37-38 57"></path><path fill="#fbbc02" d="m90 341a208 200 0 010-171l63 49q-12 37 0 73"></path><path fill="#ea4335" d="m153 219c22-69 116-109 179-50l55-54c-78-75-230-72-297 55"></path></g></svg>
          Login with Google
        </button>
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
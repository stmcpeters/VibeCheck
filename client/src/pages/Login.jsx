// Forms for email/password login and registration. Includes OAuth Google login button and CAPTCHA checkbox
import React, { useState } from "react";
import NavBar from "../components/NavBar";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function UserAuth() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [user, setUser] = useState(null);
  
  const navigate = useNavigate();

  // function to handle login
  const handleLogin = async (e) => {
    // prevent default form submission
    e.preventDefault();
    try {
      const response = await axios.post('/login', {email, password});
      console.log('Login successful:', response.data);
      setUser(response.data.user);
      // redirect to dashboard after successful login
      navigate('/dashboard');
    } catch (error) {
      console.error('Error logging in:', error);
      setError('Invalid email or password');
    }
  }


  return (
    <>
      <NavBar />
      <div className="card bg-base-100">
        <div className="card-body">
          <h2 className="card-title grow heading">Login</h2>
          <div className="card bg-base-300 rounded-box grid h-100 grow place-items-center">
            <fieldset className="fieldset w-xs bg-base-200 border border-base-300 p-4 rounded-box">

              <label className="fieldset-label">Email</label>
              <input type="email" className="input" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)}/>

              <label className="fieldset-label">Password</label>
              <input type="password" className="input" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>

              <button type="submit" className="btn btn-primary mt-4" onClick={handleLogin}>Login</button>
              {error && <p className="text-red-500">{error}</p>}
            </fieldset>
            {/* Google
            <button className="btn bg-white text-black border-[#e5e5e5]">
              <svg
                aria-label="Google logo"
                width="16"
                height="16"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 512 512"
              >
                <g>
                  <path d="m0 0H512V512H0" fill="#fff"></path>
                  <path
                    fill="#34a853"
                    d="M153 292c30 82 118 95 171 60h62v48A192 192 0 0190 341"
                  ></path>
                  <path
                    fill="#4285f4"
                    d="m386 400a140 175 0 0053-179H260v74h102q-7 37-38 57"
                  ></path>
                  <path
                    fill="#fbbc02"
                    d="m90 341a208 200 0 010-171l63 49q-12 37 0 73"
                  ></path>
                  <path
                    fill="#ea4335"
                    d="m153 219c22-69 116-109 179-50l55-54c-78-75-230-72-297 55"
                  ></path>
                </g>
              </svg>
              Login with Google
            </button> */}
            <p>Don't have an account? <a href='/register' style={{ color: "blue"}}>Register</a></p>
          </div>
        </div>
      </div>
    </>
  );
}

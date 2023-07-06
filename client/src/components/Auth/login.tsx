import Link from "next/link";
import React, { FormEvent, useContext } from "react";
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { generateSessionToken } from "../../../utilities/sessionUtils";
import axios from "axios";
import { error, log } from "console";
import { UserInterface, Authentication } from "../../interfaces/user";
import { AllUsersContext } from "../../context/allusers";


const LoginComponent = () => {

  const router = useRouter()
  const baseUrl = "https://www.muganedev.tech/api/v1/";


  const [pass, setPassword] = useState('')
  const [username, setUserName] = useState('')
  const [loggedInUser, setLoggedInUser] = useState('')
  const [allUsers, setAllUsers] = useState<UserInterface[]>([])
  console.log(pass)

const  allUserContext = useContext(AllUsersContext)
  const handleLogin = (formSubmit: FormEvent<HTMLFormElement>) => {
    formSubmit.preventDefault();

    const fd = new FormData(formSubmit.currentTarget);
    var object: any = {};
    fd.forEach(function (value, key) {
      object[key] = value;
    });
    console.log('====================================');
    console.log(object);
    console.log('====================================');
    const savedUserDetailsString = localStorage.getItem('user');


    axios.get(`${baseUrl}users/`, {
      auth: object
    }).then(res => {
      console.log('allUsers', res.data);
      localStorage.setItem("allUsers", JSON.stringify(res.data as UserInterface[]))
      allUserContext.update(res.data as UserInterface[])
      let filterData = (res.data as UserInterface[]).filter((user) => user.email == object.username)
      console.log('====================================');
      console.log(filterData, object, object.username);
      console.log('====================================');
      alert('Login successful!');
      let authData: Authentication = {
        auth: object, id: filterData[0].id,
        userName:filterData[0].username
      }
      localStorage.setItem('user', JSON.stringify(authData));
      router.push("/");
    }).catch(error => {
      console.log('allUsersError', error)
    })
  }




  return <section className="ftco-section">
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-md-7 col-lg-5">
          <div className="wrap mt-4">
            <div className="login-wrap mt-4 p-4 p-md-5">
              <div className="d-flex">
                <div className="w-100">
                  <h3 className="mb-2 text-center">Welcome Back</h3>
                </div>
              </div>
              <form action="#" className="signin-form" onSubmit={handleLogin}>
                <div className="form-group mt-4">
                  <input type="text" className="form-control rounded-pill input-area" name="username" placeholder="Username"
                    value={username} onChange={(e) => setUserName(e.target.value)}
                    required />
                </div>
                <div className="form-group mt-4">
                  <input type="password" className="form-control rounded-pill input-area" name="password" placeholder="Password"
                    value={pass} onChange={(e) => setPassword(e.target.value)}
                    required />
                </div>
                <div className="form-group mt-4">
                  <button type="submit" className="form-control btn btn-primary btn-teal rounded-pill submit px-3">Sign In</button>
                </div>
                <div className="form-group d-md-flex mt-3">
                  <div className="text-end w-100">
                    <a href="#" className="fw-bold txt-link">Forgot Password?</a>
                  </div>
                </div>
              </form>
              <p className="text-center mt-4">Don&apos;t have an account? <Link data-toggle="tab" href="/signup" className="fw-bold txt-link">Sign Up</Link></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

}

export default LoginComponent
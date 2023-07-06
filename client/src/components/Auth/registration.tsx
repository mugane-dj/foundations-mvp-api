import React from "react";
import { useState, useEffect, FormEvent } from "react";
import axios from "axios"
import { RegisterInterface } from "../../interfaces/register";
import Link from "next/link";

const SignupComponent = () => {
    const [busy, setbusy] = useState('loading')
    const [password, setPassword] = useState('');
    const [cpassword, setConfirmPassword] = useState('');
    const [username, setUserName] = useState('')
    const [email, setEmail] = useState('')
    const [confirmPasswordError, setConfirmPasswordError] = useState('');
    const baseUrl = "https://www.muganedev.tech/api/v1/"

    const handleSubmit = (formSubmit: FormEvent<HTMLFormElement>) => {
       
        const formData = {
            username,
            email,
            password,
        };
        console.log(formData)
        formSubmit.preventDefault()
        setConfirmPasswordError('');

        if (password !== cpassword) {
            alert("not match")
            return;
        }

        axios.post(`${baseUrl}users/create`, formData, { auth: {
            username: "snzungula@gmail.com",
            password: "foundation25"
          }})
            .then(res => {
                setbusy('Loading')
                localStorage.setItem('user', JSON.stringify(formData));

                window.location.href = "/login"
                console.log(res.data);
            })
            .catch(err => {
                console.log(err)
                setbusy('')
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
                                    <h3 className="mb-2 text-center">Create an Account</h3>
                                </div>
                            </div>
                            <form action="#" className="signin-form" onSubmit={handleSubmit}>
                                <div className="form-group mt-4">
                                    <input type="text" className="form-control rounded-pill input-area" placeholder="Username" 
                                     onChange={(e) => setUserName(e.target.value)}required />
                                </div>
                                <div className="form-group mt-4">
                                    <input type="text" className="form-control rounded-pill input-area" placeholder="Email address"
                                     onChange={(e) => setEmail(e.target.value)} required />
                                </div>
                                <div className="form-group mt-4">
                                    <input id="password-field" type="password" value={password} className="form-control rounded-pill input-area" placeholder="Password"
                                        onChange={(e) => setPassword(e.target.value)}
                                        required />
                                </div>
                                <div className="form-group mt-4">
                                    <input id="password-field" type="password" value={cpassword} className="form-control rounded-pill input-area" placeholder="Confirm Password"
                                        onChange={(e) => setConfirmPassword(e.target.value)}
                                        required />
                                </div>
                                <div className="form-group mt-4">
                                    <button type="submit" className="form-control btn btn-primary btn-teal rounded-pill submit px-3">Sign Up</button>
                                </div>
                            </form>
                            <p className="text-center mt-4">Already have an account? <Link data-toggle="tab" href="/login" className="fw-bold txt-link">Sign In</Link></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

}

export default SignupComponent;
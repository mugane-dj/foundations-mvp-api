'use client'
import { NextPage } from "next";
import SignupComponent from "../src/components/Auth/registration";
import { useState, useEffect } from 'react'
import Head from 'next/head'

const SignUpPage: NextPage = () => {
    const [isloaded, setIsloaded] = useState(false)
    useEffect(() => {
      setIsloaded(true)
    }, [])
    return <SignupComponent />

}


export default SignUpPage;
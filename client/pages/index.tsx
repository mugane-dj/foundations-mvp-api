import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import { useState, useEffect } from 'react'
import HomeComponent from '../src/components/home'
import LoginPage from './login'
// import styles from '../styles/Home.module.css'

const Home: NextPage = () => {

  return (
   <>
   {
        localStorage.getItem('user') ==null? <LoginPage  />   :   <HomeComponent />
   }
   </>


  )
}

export default Home

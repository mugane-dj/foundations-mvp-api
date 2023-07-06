import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import { useState, useEffect } from 'react'
import HomeComponent from '../src/components/home'
import MyComplaintsComponent from '../src/components/myComplaints'

const MyComplaints: NextPage = () => {
  const [isloaded, setIsloaded] = useState(false)
  useEffect(() => {
    setIsloaded(true)
  }, [])
  return (
        <MyComplaintsComponent />
  )
}

export default MyComplaints;
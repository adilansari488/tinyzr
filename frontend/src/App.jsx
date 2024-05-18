import { useState, lazy, Suspense } from 'react'
import NavbarComp from './Components/Navbar'
import InputBox from './Components/InputBox'
import { onSubmit, SubmitBtn } from './Components/SubmitBtn'
import CopyBtn from './Components/CopyBtn';
import './index.css'
import Footer from './Components/Footer';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
const About = lazy(()=> import("./Components/About"))

function App() {
  return (
    <div>
      <BrowserRouter>
      <NavbarComp />
      <br />
      <Routes>
        <Route path='/about' element={<Suspense fallback={"Loading..."}><About /></ Suspense>} />
        <Route path='/' element={<Suspense fallback={"Loading..."}><AppBar /></ Suspense>} />

      </Routes>
      <Footer />
    </BrowserRouter>
    </div>
  )
}

function AppBar() {
  const [shorturl, setShorturl] = useState("")
  const [originalurl, setOriginalurl] = useState("")
  return <div>
    <div id="h1-title" className='text-center text-4xl font-bold text-gray-600'>URL Shortener</div>
    <br />
    <div className='flex justify-center'>

      <InputBox readOnly={false} placeHolder="Enter Long URL here" name="longurl" className="rounded-l-md border border-gray-300 p-2 focus:outline-none focus:border-blue-600 h-10" onChange={(e) => {
        setOriginalurl(e.target.value);
      }} onKeyDown={async (e) => {
        if (e.code == "Enter") {
          const res = await onSubmit(originalurl, setShorturl);
          setShorturl(res.message.short_url);
        }
      }} />

      <SubmitBtn originalurl={originalurl} setShorturl={setShorturl} />
    </div>
    <div className='flex justify-center pt-5'>
      <InputBox readOnly={true} placeHolder="Short URL will be shown here" name="shorturl" className="text-gray-500 rounded-md border border-gray-300 p-2 text-center w-80 focus:outline-none focus:border-blue-500" value={shorturl} />
      <CopyBtn data={shorturl} />
    </div>
    <div className='flex justify-center pt-4 text-gray-500'><p>
      Tinyzr is a free tool to generate short URLs for your lengthy URLs.
    </p>
    </div>
  </div>
}



export default App

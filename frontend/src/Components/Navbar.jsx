// import '../assets/styles.css'
import { memo } from 'react';
import '../index.css'
import { useNavigate } from 'react-router-dom';

const NavbarComp = memo(()=> {
    const navigate = useNavigate() ; 
    return <nav className=''>
        <div className="navbar flex justify-between p-4 bg-gradient-to-r from-blue-100 to-blue-500 text-white rounded-lg m-1">
            <div id="appName" className='text-xl cursor-pointer text-gray-600 font-bold' onClick={()=> {
                navigate('/')
            }}>Tinyzr URL Shortener</div>
            <div className="navbar-pages flex justify-between">
            <div className='px-2 cursor-pointer hover:text-blue-100' onClick={()=> {
                navigate('/')
            }}>Home</div>
            <div className='px-2 cursor-pointer hover:text-blue-100' onClick={()=> {
                navigate('/about')
            }}>About</div>
            <a className='px-2 cursor-pointer hover:text-blue-100' target='blank'
            href='https://forms.gle/FXGQC4qcW6YoWxo96'>Feedback</a>
            </div>
        </div>
    </nav>
}) 

export default NavbarComp ;
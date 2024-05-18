
import React from 'react';

const About = () => {
    return (
        <div className='text-center'>
            <div className='text-4xl font-bold text-gray-600'>About TinyZr</div> <br />
            <div className='flex justify-center'>
                <div className='text-l text-gray-500 max-w-xl bg-slate-50 rounded-lg overflow-hidden shadow-lg p-6 mr-5'>
                    <div className='text-2xl font-bold text-gray-600'>About TinyZr</div> <br />
                    <p>
                        TinyZR is a sleek and efficient URL shortener service created by <a className=' text-blue-500' href="https://linkedin.com/in/adilansari488" target="_blank">Adil Ansari</a>.
                    </p>
                    <p>
                        Simplify and enhance your online experience by transforming long and cumbersome URLs into concise links with TinyZR..
                    </p>
                </div>
                <br />
                <div className='text-l text-gray-500 max-w-xl bg-slate-50 rounded-lg overflow-hidden shadow-lg p-6 ml-5'>
                    <div className='text-2xl font-bold text-gray-600'>Motivation Behind TinyZr</div> <br />
                    <p>
                        Initial motivation behind TinyZr was building a serverless application.
                    </p>
                    <p>
                    If you are also a developer you can view the architecture diagram <a className='text-blue-500' href="https://drive.google.com/file/d/1QDI5i1ZYF7Q2hLa6j3g4mGP_HzJpBSRv/view" target='_blank'>here</a></p>
                </div>
            </div>
        </div>
    );
};

export default About;

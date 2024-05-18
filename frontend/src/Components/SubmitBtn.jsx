import axios from "axios"
import { memo, useState } from "react";
import apiURL from "../constants";

export const SubmitBtn = memo((props) => {
    const [generatingmsg, setGeneratingmsg] = useState("generating...") ;
    return <div>
        <button type="button" className='bg-blue-500 h-10 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r-md'
        onClick={async ()=> {
            const res = await onSubmit(props.originalurl, props.setShorturl) ;
            props.setShorturl(res.message.short_url) ;
            }}>Shorten URL</button>
    </div>
})

export async function onSubmit(url, setShorturl) {
  setShorturl("Generating Short URL...")
  const userLocation = await axios.get("https://ipinfo.io/json?token=ff6f472c2c9165")
  const userLocationData = userLocation.data ;
  const headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'API_KEY'
    }
  let req_body = {
  "user_id": "NA",
  "user_ip": userLocationData.ip,
  "user_city": userLocationData.city,
  "user_region": userLocationData.region,
  "user_country": userLocationData.country,
  "original_url": url,
  "is_custom_url": "false"
  }

  try {
    const response = await axios.post(apiURL, req_body, {headers}) ;

    return response.data ;
  }
  catch (error) {
    return {
      "message": {
        "short_url": "Error: Invalid URL or an issue occurred."
      }
    }
  }
}

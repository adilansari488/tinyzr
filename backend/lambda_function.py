import json
from utils import *
from env import *
from const import CORS_Headers

def lambda_handler(event, context=None):

    try:
        url_origin = event["headers"]["origin"]
        if url_origin in ALLOWED_DOMAINS:
            logger(f"url_origin is {url_origin} and it is in allowed origin list, so passing the request.")
            pass
        else :
            logger(f"url_origin is not in allowed origin list, instead it is from {url_origin}", 2)
            response = {
                        "statusCode": 403,
                        "headers": {
                            "Content-Type": 'application/json'
                                    },
                        "body": json.dumps({
                            "message": "you are not authorized to access the api."
                                })
                        }
            return response
    except Exception as e:
        logger(f"url_origin not detected. and error raised - {str(e)}", 3)
        response = {
                        "statusCode": 403,
                        "headers": {
                            "Content-Type": 'application/json'
                                    },
                        "body": json.dumps({
                            "message": "you are not authorized to access the api."
                                })
                        }
        return response
    
    logger(f"event : {event}")
    if event["httpMethod"] == "GET" :
        response = {
                    "statusCode": 200,
                    "headers": CORS_Headers,
                    "body": json.dumps({
                        "message": "you are not authorized to access the api."
                            })
                            }
        return response

    if event["httpMethod"] == "POST" :
        request_body = event["body"]
        json_body = json.loads(request_body)
        logger(f"json body : {json_body}")

    if "user_id" in json_body :
        user_id = json_body["user_id"]
    else:
        user_id = "NA"
        
    if "original_url" in json_body :
        originalURL = json_body["original_url"]
    else:
        originalURL = "https://www.example.com"
        
    if "user_ip" in json_body :
        ip = json_body["user_ip"]
    else:
        ip = "0.0.0.0"
        
    if "is_custom_url" in json_body:
        is_custom_url = True if json_body["is_custom_url"].lower() == "true" else False
    else:
        is_custom_url = False
        
    if is_valid_url(originalURL):
        try:
            logger(originalURL)
            url_id, iterations = url_id_generator(originalURL)
            shortURL = f"{DOMAIN}/{url_id}"
            data_to_insert = {
                "user_id": user_id,
                "user_ip": ip,
                "original_url": originalURL,
                "url_id": url_id,
                "short_url": shortURL,
                "is_custom_url": is_custom_url,
                "is_qrcode": False,
                "qrcode_img_url": "NA",
                "iterations": iterations,
                "total_clicks": 0, # Need to implement.
                "time_created": "",
                "last_accessed": "",
                "expiry_date": ""
            }
            
            is_data_inserted, data_insertion_msg = insert_to_db(data_to_insert, url_id)
            logger(f"is_data_insert response: >>>>> {is_data_inserted}")
            if is_data_inserted :
                response = {
                    "statusCode": 200,
                    "headers": CORS_Headers,
                    "body": json.dumps({
                        "message": {
                        "is_inserted": True,
                        "original_url": originalURL,
                        "short_url": shortURL
                        }
                            })
                            }
            else:
                response = {
                    "statusCode": 500,
                    "headers": CORS_Headers,
                    "body": {
                        "is_inserted": False, 
                        "message": data_insertion_msg
                            }
                        }
                logger(response)
                res2 = {
                    "statusCode": 500,
                    "headers": CORS_Headers,
                    "body": json.dumps({
                        "is_inserted": False, 
                        "message": "internal server error. Please try after sometime."
                            })
                        }
                return res2
    
        except Exception as e:
            response =  {
                    "statusCode": 500,
                    "headers": CORS_Headers,
                    "body": {
                        "is_inserted": False, 
                        "message": f"error in lambda function : {e}"
                            }
                        }
            logger(response)
            res2 = {
                    "statusCode": 500,
                    "headers": CORS_Headers,
                    "body": json.dumps({
                        "is_inserted": False, 
                        "message": "internal server error. Please try after sometime."
                            })
                        }
            return res2
    else :
        response = {
            "statusCode": 500,
            "headers": CORS_Headers,
            "body": json.dumps({
                "message": "Please enter a valid URL. (e.g. https://www.google.com)"
            })
        }
            
    return response


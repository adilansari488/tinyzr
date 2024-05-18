import hashlib
import datetime
import re
from pymongo import MongoClient
# import validators
import random
from const import *
from env import *
# import segno
import logging

def logger(message, log_level=1):
    """
    Logs a message with the specified log level.

    Parameters:
    - message (str): The message to be logged.
    - log_level (int): The log level (default is INFO).
    """
    if log_level == 1 :
        log_level = logging.INFO
    if log_level == 2 :
        log_level = logging.WARNING
    if log_level == 3 :
        log_level = logging.ERROR
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.log(log_level, message)

def generate_random_string(length):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random_string = ""
    for i in range(length):
        rand_int = random.randint(0,len(characters)-1)
        random_string += characters[rand_int]
    return random_string

def url_id_generator(originalURL, length=URL_LENGTH):
    if length <= MINIMUM_URL_LENGTH :
        return "Length is too short. Please choose greater than 3.", -1
    url_hash = hashlib.sha256(originalURL.encode()).hexdigest()
    url_id = url_hash[-length:]
    logger(f"url id generated at first time - {url_id}")
    client = MongoClient(MONGO_URI)
    db = client[URL_DB]
    collection = db[URL_COLLECTION]
    url_id_check = None
    try:
        url_id_check = collection.count_documents({'url_id': url_id})
        logger("mongo connected")
    except :
        logger("error in mongo connection", 3)
    # db = client[URL_DB]
    # collection = db[URL_COLLECTION]
    # url_id_check = collection.count_documents({'url_id': url_id})    
    iterations = 0
    if url_id_check:
        logger(f"{url_id} url id already available in DB.")
        logger("generating new url id...")
        while url_id_check:
            iterations += 1
            random_char = generate_random_string(1)
            random_index = random.randint(0, URL_LENGTH-1)
            temp_url_id = list(url_id)
            temp_url_id[random_index] = random_char
            url_id = "".join(temp_url_id)
            logger(f"url_id at iteration-{iterations} is {url_id}")
            url_id_check = collection.count_documents({'url_id': url_id})
            if not url_id_check:
                client.close()
                logger(f"final url id is - {url_id}")
                return url_id, iterations
            elif iterations >= 5 :
                client.close()
                logger(f"final url id is - {url_id}")
                return url_hash[-URL_LENGTH-1:], iterations
    else:
        logger(f"final url id is - {url_id}")
        client.close()
        return url_id, iterations

# old fucntion to validate URL
# def is_valid_url(url):
#     if not url.startswith('http://') and not url.startswith('https://'):
#         logger("url not starting with http:// or https:// so attaching https:// before the url")
#         url = 'https://' + url
#     validation = validators.url(url)
#     logger(validation)
#     if validation == True :
#         logger("valid")
#         return True
#     else:
#         logger("invalid")
#         return False
    
# New Function to validate url
def is_valid_url(url) :
    # Check if the URL contains http:// or https://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url  # Assume http:// if not provided
    # Use regular expression to check for a valid top-level domain
    tld_pattern = re.compile(r'^https?://([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,63})([a-zA-Z0-9/?=&%_#.-]*)?$')
    match = tld_pattern.match(url)
    if match:
        logger(f"URL validation passed for request url - {url}")
        return True
    else:
        logger(f"URL validation failed for request url - {url}", 3)
        return False

        
def insert_to_db(data, url_id):
    try:
        # data = json.loads(data)
        current_timestamp = datetime.datetime.now()
        current_timestamp_iso = current_timestamp.isoformat()
        expiry_timestamp = (current_timestamp + datetime.timedelta(days=180)).isoformat()
        data['time_created'] = current_timestamp_iso
        data['expiry_date'] = expiry_timestamp
        client = MongoClient(MONGO_URI)
        db = client[URL_DB]
        collection = db[URL_COLLECTION]
        url_id_check = collection.count_documents({'url_id': url_id})
        logger(f"url_id_check: >>>>> {url_id_check}")
        if not url_id_check:
            dict_data = dict(data)
            collection.insert_one(dict_data)
            logger(f"This is the data inserted into DB >>> {dict_data}")
            client.close()
            return True, "data inserted successfully"
        else :
            logger(f"{url_id} url_id is not unique hence unable to add data in DB", 3)
            client.close()
            return False, f"url_id: {url_id} is not unique"
    except Exception as e:
        logger(f"An error occurred while inserting data into DB: {e}", 3)
        client.close()
        return False, e
        
# def s3_upload(file,bucket,path_in_bucket):
#     pass

# def qr_generator(data):
#     qr = segno.make_qr(data)
#     data_hash = hashlib.sha256(data.encode()).hexdigest()
#     filename = data_hash[:5] + '.png'
#     if env != "lambda":
#         qr.save(filename, scale=5)

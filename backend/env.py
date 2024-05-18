from os import environ
import json
MONGO_URI = environ.get("MONGO_URI")
DOMAIN = environ.get("DOMAIN")
URL_DB = environ.get("URL_DB")
URL_COLLECTION = environ.get("URL_COLLECTION")
ALLOWED_DOMAINS = json.loads(environ.get("ALLOWED_DOMAINS"))

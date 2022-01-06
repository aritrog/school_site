import uuid
import json
import traceback
from PIL import Image
from flask import Response
from google.cloud import storage
from flask import make_response
from flask import request


def image_handler(img, name, folder='Post'):
    try:

        client = storage.Client.from_service_account_json(
            'qualified-city-334510-c3aec991befb.json')
        
        bucket = client.get_bucket('aps-img')

    except Exception as e:
        print("Bucket failed")
        traceback.print_exc()

        return None

    try:
        filename = name
        # folder = "Post"
        filename = "%s/%s" % (folder, filename)
        blob = bucket.blob(filename)
        blob.upload_from_file(img)
        url = blob.public_url
        return url
    except Exception as e:
        traceback.print_exc()
        return None
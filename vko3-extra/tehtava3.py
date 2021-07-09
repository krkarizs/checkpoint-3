#Grab the JSON file with .get() and save the picture URL to a variable
import requests

response = requests.get("https://thatcopy.pw/catapi/rest/")
data = response.json()
url = data["url"]

#Grab the picture from the URL
#The script runs on a linux VM in the cloud and the picture is downloaded to the VM
img_data = requests.get(url).content
with open('cat.jpg', 'wb') as image:
    image.write(img_data)

#Upload the .jpg file to a bucket in Cloud Storage
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

upload_blob("sevenke-checkpoint-bucket", "/home/sevenke/cat.jpg", "catpic.jpg")
#Creating a bucket
from google.cloud import storage

def create_bucket(bucket_name):
    
    storage_client = storage.Client()
    
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print( "Created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))

    return new_bucket

create_bucket("checkpoint-storage-bucket")

#Grabbing data and printing the txt file
import requests

response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")

data = response.json()
data_items = data["items"]

parameter_list = []

for i in data_items:
    parameter_list.append(i["parameter"])

with open("checkpoint.txt", "w") as x:
    for it in parameter_list:
        x.write(f"{it}\n")


#Uploading the file
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

upload_blob("checkpoint-storage-bucket", "C:/Users/KrisztinaKarizs/Desktop/Python exercises/checkpoint3/vko3-1/checkpoint.txt", "checkpoint.txt")
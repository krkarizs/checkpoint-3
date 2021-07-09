from google.cloud import storage

def create_bucket(bucket_name):
    #bucket_name = "sevenke-test-bucket3"

    storage_client = storage.Client()
    #The bucket name is the only ettribute that we need to add, everything else is optional
    bucket = storage_client.bucket(bucket_name)

    #optional stuff
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print( "Created bucket {} in {} with storage class {}".format(new_bucket.name, new_bucket.location, new_bucket.storage_class))

    return new_bucket

create_bucket("checkpoint-storage-bucket")

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


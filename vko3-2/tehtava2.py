#Downloading the file from the bucket
from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print("Blob {} downloaded to {}.".format(source_blob_name,destination_file_name))

download_blob("checkpoint-storage-bucket", "checkpoint.txt", "C:/Users/KrisztinaKarizs/Desktop/Python exercises/checkpoint3/vko3-2/checkpoint.txt")
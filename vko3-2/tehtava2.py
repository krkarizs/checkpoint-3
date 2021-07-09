#Downloading the file from the bucket
from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print("Blob {} downloaded to {}.".format(source_blob_name,destination_file_name))

download_blob("sevenke-checkpoint-bucket", "checkpoint.txt", "C:/Users/KrisztinaKarizs/Desktop/Python exercises/checkpoint3/vko3-2/checkpoint.txt")

#Printing the right number of lines from the command line
import argparse

def sort_func(item):
    return len(item)

parser = argparse.ArgumentParser()
parser.add_argument("lines", help="displays the requested number of lines", type=int)

args = parser.parse_args()

with open("checkpoint.txt") as reader:
    name_list = []

    for line in reader:
        name_list.append(line)

filtered_list = []
for name in range(args.lines):
    filtered_list.append(name_list[name])

sorted_list = sorted(filtered_list, key=sort_func)

for x in sorted_list:
    print(x)
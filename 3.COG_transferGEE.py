import os
import time
from google.cloud import storage

# know my buckets
#os.system('gsutil ls')

# define my bucket
bucket = 'my_bucket'

# define routes of image collections
COG_gee = 'my_cog_gee_path'
udm1_gee = 'my_udm1_gee_path'
udm2_gee = 'my_udm2_gee_path'
gee_cmd = 'earthengine upload image --asset_id='
time_cmd = '--time_start='

# create a list of images
COG_gcp = []
udm1_gcp = []
udm2_gcp = []

# loop to add each element to corresponding list
client = storage.Client()
for blob in client.list_blobs(bucket):
    if blob.name.endswith('COG.tif'):
        COG_gcp.append(blob.name)
    elif blob.name.endswith('udm1.tif'):
        udm1_gcp.append(blob.name)
    elif blob.name.endswith('udm2.tif'):
        udm2_gcp.append(blob.name)

# loop to transfer COG files from the GCP to GEE
for img in COG_gcp:

    year = img[7:11]
    month = img[11:13]
    day = img[13:15]

    if len(img) == 35:
        hour = img[21:23]
        minute = img[23:25]
        second = img[25:27]

    elif len(img) == 36:
        hour = img[22:24]
        minute = img[24:26]
        second = img[26:28]

    os.system(gee_cmd + COG_gee + img[0:len(img)-4] + ' ' + time_cmd + year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second + ' gs://' + bucket + '/' + img)
    print(img + ' requested to transfer from the GCP to GEE')
    time.sleep(5)

# loop to transfer udm1 files from the GCP to GEE
for img in udm1_gcp:

    year = img[7:11]
    month = img[11:13]
    day = img[13:15]

    if len(img) == 36:
        hour = img[21:23]
        minute = img[23:25]
        second = img[25:27]

    elif len(img) == 37:
        hour = img[22:24]
        minute = img[24:26]
        second = img[26:28]

    os.system(gee_cmd + udm1_gee + img[0:len(img)-4] + ' ' + time_cmd + year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second + ' gs://' + bucket + '/' + img)
    print(img + ' requested to transfer from the GCP to GEE')
    time.sleep(5)

# loop to transfer udm2 files from the GCP to GEE
for img in udm2_gcp:

    year = img[7:11]
    month = img[11:13]
    day = img[13:15]

    if len(img) == 36:
        hour = img[21:23]
        minute = img[23:25]
        second = img[25:27]

    elif len(img) == 37:
        hour = img[22:24]
        minute = img[24:26]
        second = img[26:28]

    os.system(gee_cmd + udm2_gee + img[0:len(img)-4] + ' ' + time_cmd + year + '-' + month + '-' + day + 'T' + hour + ':' + minute + ':' + second + ' gs://' + bucket + '/' + img)
    print(img + ' requested to transfer from the GCP to GEE')
    time.sleep(5)
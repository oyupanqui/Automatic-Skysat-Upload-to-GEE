import os

# create tiff lists

skysat_list = []
udm1_list = []
udm2_list = []

# loop to group tiffs

for file in os.listdir():
    if file.endswith('ed.tif'):
        skysat_list.append(file)
    elif file.endswith('udm.tif'):
        udm1_list.append(file)
    elif file.endswith('udm2.tif'):
        udm2_list.append(file)
    else:
        continue

# create a cog list

cog_list = []

# loop to create cog items

for img in skysat_list:
    ymd = img[0:8]
    hms = img[9:15]
    if len(img) == 43:
        ssc = img[16:20]
        udm = img[21:26]
    else: 
        ssc = img[16:21]
        udm = img[22:27]
    
    if udm[-1] != '1':
        hms = str(int(hms) + int(udm[-1]) - 1)

    cog = 'Skysat_' + ymd + '_' + ssc + '_' + hms + '_COG.tif'
    cog_list.append(cog)

# zip skysat image and cog lists

final_list = list(zip(skysat_list, cog_list))

# define bucket to upload de the images
bucket = 'your_bucket'

# define the path of the image collections
COG_path = 'your_COG_path'
udm1_path = 'your_udm1_path'
udm2_path = 'your_udm2_path'

# upload the udm1 files
for img in udm1_list:
    ymd = img[0:8]
    hms = img[9:15]
    if len(img) == 47:
        ssc = img[16:20]
        udm = img[21:26]
    else: 
        ssc = img[16:21]
        udm = img[22:27]
    
    if udm[-1] != '1':
        hms = str(int(hms) + int(udm[-1]) - 1)

    udm1 = 'Skysat_' + ymd + '_' + ssc + '_' + hms + '_udm1.tif'
    os.system('gsutil -m cp -r ' + img + ' gs://' + bucket + '/' + udm1)
    print(udm1 + ' has been uploaded to the GCP')

# upload the udm2 files
for img in udm2_list:
    ymd = img[0:8]
    hms = img[9:15]
    if len(img) == 48:
        ssc = img[16:20]
        udm = img[21:26]
    else: 
        ssc = img[16:21]
        udm = img[22:27]
    
    if udm[-1] != '1':
        hms = str(int(hms) + int(udm[-1]) - 1)

    udm2 = 'Skysat_' + ymd + '_' + ssc + '_' + hms + '_udm2.tif'
    os.system('gsutil -m cp -r ' + img + ' gs://' + bucket + '/' + udm2)
    print(udm2 + ' has been uploaded to the GCP')

# upload the COG files
for img in cog_list:
    os.system('gsutil -m cp -r ' + img + ' gs://' + bucket + '/')
    print(img + ' has been uploaded to the GCP')

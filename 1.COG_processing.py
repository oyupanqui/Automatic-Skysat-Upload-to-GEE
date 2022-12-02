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

# loop to create overviews COMMENT IF THE OVERVIEWS HAVE BEEN GENERATED
for sk in final_list:
    os.system('gdaladdo -r average ' + sk[0] + ' 2 4 8 16')
    print('Overview for '+ sk[0] + ' has been generated')

print('OVERVIEW GENERATION COMPLETED')

# loop to create final cog files
for sk in final_list:
    os.system('gdal_translate ' + sk[0] + ' ' + sk[1] + ' -co TILED=YES -co COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW -co BIGTIFF=IF_NEEDED')
    print(sk[1] + ' has been created')

print('COG CREATION COMPLETED')
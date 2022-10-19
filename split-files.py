#!/usr/bin/python3

from pathlib import Path
import glob
import re
import shutil

file_patt = list()
case_id = list()

# get pattern
with open('/path/to/file/count-by-slice.txt', 'r') as f:
    for line in f:
        line = line.split('\t')
        file_patt.append(line[0])
        case_id.append(line[2])

# get slice id
count = 1
slice_id_lst = list()

for i in file_patt:
    slice_id = i[-4:]
    if slice_id.startswith('A'):
        new_slice_id = re.sub(" ", "_", slice_id)
        slice_id_lst.append(new_slice_id)
    else:
        new_slice_id = "tonsil_{}".format(count)
        slice_id_lst.append(new_slice_id)
        count+=1

new_folder_name = list()

# create qupath project folder
for i, j in zip(case_id, slice_id_lst):
    new_name = i.split('\n')[0] + '_' + j
    folder_name = '/path/to/qupath-projects/' + new_name
    new_folder_name.append(folder_name)
    Path(folder_name).mkdir(parents=True, exist_ok=True)

# create text file listing path to input files
# for each slice == project
for i, j in zip(file_patt, new_folder_name):
    new_name = j.split('/')[5]
    filepath = '/path/to/component_data/' + i + '*'
    filenamelst = glob.glob(filepath)
    with open('/path/to/path-to-files-by-slice/' + new_name + '-tiflst.txt', 'w') as f:
        f.write('\n'.join(filenamelst))

    

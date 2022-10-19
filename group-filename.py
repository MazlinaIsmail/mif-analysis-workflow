#!/usr/bin/python3

# reads in a list of component_data filenames
# extract the unique prefix and count
# effectively counting number of tifs per slice

from collections import Counter

file_names = list()

with open('/path/to/file/component_data-namelst.txt', 'r') as f:
    for line in f:
        line = line.split('_[')
        file_names.append(line[0])

count_by_slice = Counter(file_names)

outfile = open('/path/to/file/count-by-slice.txt', 'w')

for k, v in count_by_slice.items():
    string = "%s\t%s\n" % (k, v)
    outfile.write(string)

outfile.close()



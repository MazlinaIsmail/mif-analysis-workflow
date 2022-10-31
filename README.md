# mif-analysis-workflow
Walk through of the steps taken for analysis of multiplex IF image data from Vectra

## Aim 1: check image quality using mean intensity of DAPI

1. Copy \*component_data\* tif files from source_dir to destination_dir = 4,561 files
2. Create a text file containing unique slice ID and count of images per slice -> group-filename.py
3. Create list of paths (.txt) and empty directory for each slice = 54 + 6 controls -> split-files.py
4. For each matched pair of empty_dir and path_list, create Qupath project and load images -> create-project-and-load-images.groovy
5. For each project, get mean intensity value of DAPI -> get-mean-intensity-value.groovy  
   Save as image metadata.

To be continued .....  

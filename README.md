# mif-analysis-workflow
Walk through of the steps taken for analysis of multiplex IF image data from Vectra

## Aim 1: check image quality using mean intensity of DAPI

1. Copy \*component_data\* tif files from source_dir to destination_dir = 4,561 files
2. Create a text file containing unique slice ID and count of images per slice -> group-filename.py
3. Create list of paths (.txt) and empty directory for each slice = 54 + 6 controls -> split-files.py
4. For each matched pair of empty_dir and path_list, create Qupath project and load images -> create-project-and-load-images.groovy

  \# list of path lists  
  path_lst=($(find /path/to/txt/files -maxdepth 1 -type f -name "*txt"))  

  \# list of empty dirs  
  empty_dir=($(find /path/to/empty/dirs/* -maxdepth 0 -type d))  
  
  \# loop over number of slices/projects  
  \# here I know we have n = 60  
  for i in {1..60}; do /Applications/QuPath.app/Contents/MacOS/QuPath script /path/to/groovy/script/create-project-and-load-images.groovy -a "$empty_dir[$i] $path_lst[$i]"; done  

To be continued .....  

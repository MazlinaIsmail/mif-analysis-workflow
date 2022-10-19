# mif-analysis-workflow
Walk through of the steps taken for analysis of multiplex IF image data from Vectra

1. Copy *component_data* tif files from <source> to <destination> = 4,561 files
2. Create list of paths (.txt) and empty directory for each slice = 54 + 6 controls -> split-files.py
3. For each matched pair of empty_dir and path_list, create Qupath project and load images -> create-project-and-load-images.groovy

  &#35 list of path lists
  path_lst=($(find /path/to/txt/files -maxdepth 1 -type f -name "*txt"))

  &#35 list of empty dirs
  empty_dir=($(find /path/to/empty/dirs/* -maxdepth 0 -type d))
  
  &#35 loop over number of slices/projects
  &#35 here I know we have n = 60
  for i in {1..60}; do /Applications/QuPath.app/Contents/MacOS/QuPath script /path/to/groovy/script/create-project-and-load-images.groovy -a "$empty_dir[$i] $path_lst[$i]"; done

To be continued .....

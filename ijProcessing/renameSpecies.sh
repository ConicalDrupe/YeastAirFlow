#!/bin/bash
#Read Species Folder One at a time
# But we want to ignore files we have 
# already renammed and transfered
#
# Transfer old pics somewhere else? and delete in current folder?
# how can we automate this script to run through all folders?
readFolder=$1
writeFolder=$2
speciesName=$(basename $readFolder)
echo $speciesName

exiftool -r -ImageDescription="$speciesName" $readFolder -overwrite_original

if [ "$speciesName" == "C.Albicans" ]; then
  exiftool -r -d 'Albicans_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder 
elif [ "$speciesName" == "C.Auris" ]; then
  exiftool -r -d 'Auris_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder
elif [ "$speciesName" == "S.Cerevisae" ]; then
  exiftool -r -d 'Cerevisae_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder
elif [ "$speciesName" == "C.Glabrata" ]; then
  exiftool -r -d 'Glabrata_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder
elif [ "$speciesName" == "C.Haemulonii" ]; then
  exiftool -r -d 'Haemulonii_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder
elif [ "$speciesName" == "C.Krusei" ]; then
  exiftool -r -d 'Krusei_%Y%m%d_%H%M%S%%-c.%%e' '-filename<datetimeoriginal' -ext jpg -o $writeFolder $readFolder
fi

#make copy of readFolder_dated_transfer_<datetime>, then delete contents of readFolder



#!/bin/bash
#Bash script to read Species Directory and relabel metadata and Images
#READ FOLDER MUST BE IN FORMAT of C.Albicans, C.Auris, S.Cerevisae, C.Glabrata, etc...
#
#
readFolder=$1
writeFolder=$2
backupPath=$3

allowed_basenames=("C.Albicans" "C.Auris" "S.Cerevisae" "C.Glabrata" "C.Haemulonii" "C.Krusei")

#Pulls Species name from readfolder
speciesName=$(basename $readFolder)
#Create backup folder with readFolder name, with date appended
backup_readFolderName="$(basename "$readFolder")_temp_$(date +"%m-%d-%Y")"

if [ -z "$(ls -A $readFolder)" ]; then
  echo "$readFolder is empty"
  exit 1
fi

#check if basename of read folder is in species list
if [[ " ${allowed_basenames[*]} " == *" $speciesName "* ]]; then

#writes speciesName into metadata of all photos
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

#creates backup folder if it does not exist. Note: backup path must have existant parent directories
if [ ! -d "$backupPath/$backup_readFolderName" ]; then
  mkdir "$backupPath/$backup_readFolderName"
fi
# copy read folder contents to backup folder
cp -r "$readFolder"/* "$backupPath/$backup_readFolderName"
echo "Copied $readFolder contents to $backupPath/$backup_readFolderName"

else
  echo "$readFolder basename is not a listed species in renameSpecies.sh script. Check directory spelling."
  exit 1
fi
echo "Rename of $speciesName images complete!"
exit 0

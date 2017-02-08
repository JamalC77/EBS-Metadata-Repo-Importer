import os
import subprocess
## Author: Jamal Carter
## This script imports xml files from a directory to
## the database metadata repository

## The root path equivalent to $JAVA_TOP
## (*****Change this to the directory above your application*****)
root_path = 'C:/homedir/jdevhome/jdev/myclasses/'

## Directory containing the import script
## (*****Change this to the directory with your import.bat*****)
java_import_dir = 'C:/homedir/jdevbin/oaext/bin/'

## The directories from which files will be imported
paths=[
    root_path + 'mycompany/oracle/apps/xx/application/webui/',
    root_path + 'mycompany/oracle/apps/xx/lov/webui/',
    root_path + 'mycompany/oracle/apps/xx/application/attributesets/'
]

# Changes active directory to directory with import script
os.chdir(java_import_dir)

## Specific import script to run
program = java_import_dir + "import.bat"

## Default value for the file name parameter
default_page_path = ""

## Parameters used for the import.bat program
params =[
    default_page_path,
    "-rootdir",
    root_path,
    "-username",
    "apps",
    "-password",
    "apps",
    "-dbconnection",
    """(description = (address_list = (address = (community = tcp.world)(protocol = tcp)(host =hostname)(port = 1521)))(connect_data = (sid = DBNAME)))"""
    ]

## Increments when script command returns successfully
success_count = 0
## Increments when script command returns an error code value other than 0
error_count = 0

## Iterate through the files of the given paths
for directory in paths:
    default_page_path = directory + "{0}"

    ## list of all files in the directory
    list_of_files = os.listdir(directory)
    
    for fn in list_of_files:
        file_name = str(fn)
        if '.xml' in file_name:
            ## Sets the file name in the full file path
            params[0] = default_page_path.format(file_name)
        
            ## Runs the actual import script
            cp  = subprocess.run([program] + params)
             
            if cp.returncode == 0:
                print(file_name + " Successfully uploaded")
                success_count += 1
            else:
                print(file_name + " Encountered an error")
                error_count += 1


print("\n\nUploaded Successfully: " + str(success_count) + "\nFailed to Import: " + str(error_count))

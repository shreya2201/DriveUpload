# -*- coding: utf-8 -*-
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Login to Google Drive and create drive object

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in file_list:       
#    print ('title: %s, id: %s' % (file1['title'], file1['id']))



fid = '1iqirhS_XUUsDQFq4z0Xc6KhBSfznhTCY'

#insert_permission(drive,fid,None,'user','owner')

import glob, os
os.chdir("/home/shreya/Documents")
for file in glob.glob("plot.png"):
    print(file)
    with open(file,"r") as f:
        fn = os.path.basename(f.name)
        file_drive = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
    file_drive.SetContentFile(fn) 
    
    file_drive.Upload()
    print ("The file: " + fn + " has been uploaded")
   
print ("All files have been uploaded")
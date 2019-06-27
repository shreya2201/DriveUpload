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

#fid is the id of the folder in drive where all the files will be backed up
fid = '1iqirhS_XUUsDQFq4z0Xc6KhBSfznhTCY'

#insert_permission(drive,fid,None,'user','owner')

fileobject = open('tracking.txt','r')    #tracking.txt keeps the track of the files that are being uploaded to the drive
file_list = fileobject.readlines()
print(file_list)
print(file_list[0])
present = False
import glob, os
os.chdir("/home/shreya/Documents")          #it is the directory that is being backed up on google drive
for file in glob.glob("emp.txt"):
    print(file)
    with open(file,"r") as f:
        fn = os.path.basename(f.name)
        for i in range(len(file_list)):
            print(i)
            # this removes the extra \n that is present after every file name
            file_list[i] = file_list[i].replace("\n","").strip()  
            if(file_list[i] == fn):
                present = True
                print("match found for ",fn)
                break
 #if the file name is not present tracking.txt, it will upload that file to drive alongside making an entry in tracking.txt                
        if(present == False):           
            file_drive = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
            file_drive.SetContentFile(fn) 
            file_drive.Upload()
            print ("The file: " + fn + " has been uploaded")
            fileWriteObject = open('tracking.txt','a')
            s = fn
            fileWriteObject.write(s+"\n")
            print("the file is appended to tracking.txt")

fileobject.close()
fileWriteObject.close()          
print ("All files have been uploaded")

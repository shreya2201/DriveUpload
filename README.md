# DriveUpload

DriveUpload is a python script to automatically upload all the content of the particular folder on the system to a folder in google drive. The script is made to prevent any kind of manual process of backup of important files.

## Before you run the script, here are some pre-requisites to be met.
1. Go to google developer console and create a new project.
2. After naming the project, navigate through the burger button on the top-left corner and click on Api and services.
3. In that click on button, enable apis and services.
4. Select google drive api and enable it.
5. After that you need to create the credentials for the client.
6. Under the OAuth consent screen, give a name to your application. Go back again to the main page of create credentials.
7. You will get an client id and a secret(that is to be kept secret).
8. Upon id creation, you will be able to see a download icon that will download your keys as json.
9. Copy this file to the location where your DriveUpload.py is located.
10. Rename the .json file to client_secrets.json

Thats it!!!

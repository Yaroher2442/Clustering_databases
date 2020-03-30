# Clustering databases on flask
This test application is designed to clustering databasesfor files uploaded by user.  
To work with the application API is used based on HTTP requests to the local server deployed on Flask.   
Downloading and calculation take place in the background. 
Communication with the user occurs through the browser in the form of simple html

## Setup 
---
**First we need:**
- python 3+  
- pip 

**The second step is to install the necessary packages using pip.**  
We can use 
>pip install -r requirements.txt  (you must be in the project directory)

Or install each package separately
>pip install (Flask,requests,scikit-learn,pandas,sklearn,matplotlib,Werkzeug ) 
---

## Start 
**To run all the necessary services supporting this application is necessary:**
- Start a Application (app.py)

#### app.py  
  
You need to go to the basic directory of project using new console  

Then enter the command:  
	
    $python app.py

After that you can see the Flask server in console


## Testing
**For tests I use browser with http://127.0.0.1:5000/**
- "/"  - is sample page for upload file by user
- "/way" - page after upload
- "/ret" - page with buttons for view results of clustering

NEEDED TO UPLOAD .CSV FILE

After upload file you can click the necessary button for the statistics that you want to see (on "/ret" page)










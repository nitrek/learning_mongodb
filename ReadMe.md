# Learning Mongodb  
https://docs.mongodb.com/

# Links
* Aggeration
  * https://docs.mongodb.com/manual/meta/aggregation-quick-reference/index.html

* Update Operators 
  * https://docs.mongodb.com/manual/reference/operator/update/


* Commands

` mongoimport --drop --type csv --headerline --db mflix --collection movies --host "<CLUSTER>/<SEED_LIST>" --authenticationDatabase admin --ssl --username analytics --password analytics-password --file movies_initial.csv `


#Mflix App Setup 

* ```pip install -r requirements.txt```
# Setting Up MFlix
  This file is a guide to getting started running mflix, an example video streaming application backed by MongoDB!

  It's important to note that you don't need to set up MFlix to complete the required work for this course. If you run into issues setting up MFlix that you can resolve you should move forward with the graded exercises.

  # Prerequisites
  Before install mflix, you'll first need to make sure you've followed the all the steps in Setting Up Your Course Environment. This means you should already have an Atlas cluster, MongoDB installed locally, and have Anaconda running with Python 3 to support your Jupyter notebooks.

  # MFlix Dependancies
  After ensuring you have all the necessary prerequisites, you'll need to install the necessary Python dependencies used by mflix.

  First, download the MFlix zip and extract it to your mongodb-analytics/intro-to-mongodb/mflix folder.

  Then, activate your Anaconda environment by running:

``` 
source activate intro-to-mongodb # on Linux and macOS
activate intro-to-mongodb # on Windows
```
Now, from within this environment you can install all your Python dependencies using the requirements.txt from the zip:

```
pip install -r requirements.txt
```

# Importing Data
After installing all the dependencies you can import the data required by mflix into your MongoDB Atlas cluster.

To import this data you'll first need to paste your connection URI (from the Atlas UI) into env.sh (or env.bat on Windows).

After you've update env.sh (or env.bat on Windows) with your Atlas connection URI you can run init.sh (or init.bat on Windows) to import all the required data:


Running the Application
Once your dependencies and data are taken care of you can finally start mflix!

Because Windows has issues with environmental variables being set from the command line, Windows users will need to make a small change to their db.py file. Replace "environ["MFLIX_DB_URI"]" with the same connection string you used in env.bat.


To do this run the following command:

``` 
./run.sh # on Linux and macOS
 run # on Windows
And then point your browser to http://localhost:5000/.

```
From here, you should go ahead and create yourself an account by clicking "sign up

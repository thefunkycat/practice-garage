# practice-garage

This project is assuming you are familiar with the app engine basics:<br>
if not please check [guestbook tutorial](https://gaedevs.com/blog/how-to-use-the-firestore-emulator-with-a-python-3-flask-app)
a simple example with FireStore<br>
_Optional: Try to use the DataStore instead_

Practice for google app engine python with Vue

download the project

## Setup _google app engine_

- install 
[google app engine sdk](https://cloud.google.com/sdk/docs/)<br>
-- _The app-engine-python package is required_
<br>In the commandline go to project and check the `glcoud components list`. If app-engine-python is not installed run: `gcloud components install app-engine-python`


see [GAE local run](https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app)


## Setup _npm and webpack_

- install [nodejs](https://nodejs.org/en/) -- _install recommended version_

use the commandline and go to the project.<br>
Within this project mulitple smaller projects are defined app, worker and web. Since we are running
the javascript we should got to the web folder.

Now type `npm install`<br>
this will install all java script dependencies for the project.

now webpack needs to watch the javascript files and place the generated files in the static/dist folder.<br>
type `npm run dev`
<br>since watcher is defined in dev modus the script will keep running and detect changes.

## Further initialization
To run this project you will need like in the FireStore example an emulator for the datastore.<br>
install the [datastore emulator](https://cloud.google.com/datastore/docs/tools/datastore-emulator)<br>

for now use a test environment:<br>
`gcloud beta emulators datastore start --project practice-garage --host-port localhost:8000`<br>

To run the application run the script `dev_appserver.py`
This will automatically start the server with all env variables set.

## Datastore viewer
Sadly google did not include a datastore viewer in gcloud, but luckily for us there is a package called [Datastore Emulator UI](https://github.com/streamrail/dsui) to get this functionality back.
To install run the following command `npm i -g @streamrail/dsui`
 

## Starting the server
In terminal run `gcloud beta emulators datastore start --project practice-garage --host-port localhost:8000` for the datastore emulator. <br>
In separate terminal run `dsui -r practice-garage -e localhost:8000` for the datastore viewer. <br>
Run python script `dev_appserver.py` for the actual application.

## List of things
[datastore](https://googleapis.dev/python/datastore/latest/index.html)<br>
[ndb](https://googleapis.dev/python/python-ndb/latest/index.html) (_ndb client library for use with Google Cloud Datastore_)<br>
[flask](http://flask.palletsprojects.com/en/1.1.x/)<br>
[datastore emulator](https://cloud.google.com/datastore/docs/tools/datastore-emulator)<br>

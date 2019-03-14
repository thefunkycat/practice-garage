# practice-garage

This project is assuming you are familiar with the app engine basics:<br>
if not please check [guestbook tutorial](https://cloud.google.com/appengine/docs/standard/python/getting-started/creating-guestbook)

Practice for google app engine python with jinja2 jquery and webpack

download the project

## Setup _google app engine_

- install 
[google app engine](https://cloud.google.com/appengine/docs/standard/python/download)
-- _The app-engine-python package is required_
<br>In the commandline go to project and check the `glcoud components list`. If app-engine-python is not installed run: `gcloud components install app-engine-python`


see [GAE local run](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server)


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


####----- to fix error there are to many files.<br>
go to :<br>
`/google-cloud-sdk/platform/google_appengine/google/appengine/tools/devappserver2/mtime_file_watcher.py`
    
below the
<br>`for dirpath, dirnames, filenames in os.walk(self._directory, followlinks=True):`

place at line ~167: _ofcourse this line number can be different_
```
if '/node_modules/' in dirpath:
    continue
```
It might even be possible to exclude the `web` folder completely.
# -*- coding: utf-8 -*-

"""
File to run all services on one ip + port. To access specif services use the prefix url

To run the database emulator type the following into the terminal
gcloud beta emulators datastore start --project=practice-garage --host-port=localhost:8000

Also run the the npm watcher by running the following command in de web directory in the terminal
npm run dev
"""

import os
import subprocess

# Set environment variables
os.environ["FLASK_ENV"] = "development"
os.environ["DATASTORE_DATASET"] = "practice-garage"
os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8000"
os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8000/datastore"
os.environ["DATASTORE_HOST"] = "http://localhost:8000"
os.environ["DATASTORE_PROJECT_ID"] = "practice-garage"

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from app.main import app as app

application = DispatcherMiddleware(
    app, {
    }
)


if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=8080,
        application=application,
        use_reloader=True,
        use_debugger=True,
        use_evalex=True
    )

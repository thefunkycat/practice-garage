from google.cloud import ndb
import os


debug = os.environ.get('FLASK_ENV', 'prod') == 'development'
_credentials = None
_project = None
if debug:
    _project = 'test'
    import mock
    from google.auth import credentials
    _credentials = mock.Mock(spec=credentials.Credentials)


client = ndb.Client(project=_project, credentials=_credentials)

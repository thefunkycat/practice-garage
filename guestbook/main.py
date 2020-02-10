import os
import mock
from flask import Flask, render_template, request
from google.cloud import firestore
from google.cloud import datastore
from google.cloud import ndb
import google.auth.credentials

app = Flask(__name__)
debug = os.environ.get('FLASK_ENV', 'prod') == 'development'

if debug:
    # localhost
    # os.environ["FIRESTORE_DATASET"] = "test"
    # os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8001"
    # os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:8001/firestore"
    # os.environ["FIRESTORE_HOST"] = "http://localhost:8001"
    # os.environ["FIRESTORE_PROJECT_ID"] = "test"

    os.environ["DATASTORE_DATASET"] = "test"
    os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"
    os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8001/datastore"
    os.environ["DATASTORE_HOST"] = "http://localhost:8001"
    os.environ["DATASTORE_PROJECT_ID"] = "test"

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    # db = firestore.Client(project="test", credentials=credentials)
    # client = datastore.Client(project="test", credentials=credentials)
    client = ndb.Client(project="test", credentials=credentials)
else: # prod
    db = firestore.Client()

#
# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/", methods=["GET", "POST"])
# def index():
#     # get all messages from the Firestore
#     messages_ref = db.collection(u'messages')  # a reference to the messages collection
#     messages_gen = messages_ref.stream()  # messages generator: holds all message documents (these documents need to be converted to dicts)
#
#     messages = []
#     for message in messages_gen:
#         message_dict = message.to_dict()  # converting DocumentSnapshot into a dictionary
#
#         message_dict["id"] = message.id  # adding message ID to the dict, because it's not there by default
#         messages.append(message_dict)  # appending the message dict to the messages list
#
#     if request.method == "POST":
#         # add message to Firestore
#         message_ref = messages_ref.document()  # create a message document reference
#         # now you can create or update the message document (set: if it exists, update it. If not, create a new one).
#         message_ref.set({
#             u'message': u'{}'.format(request.form.get("message")),
#         })
#
#     return render_template("index.html", messages=messages)


# @app.route('/', methods=['GET', 'POST'])
# def index_test():
#     print('yay starting query')
#     if request.method == "POST":
#         key = client.key('Message')
#         entity = datastore.Entity(key=key)
#         entity.update({
#             'message': u'{}'.format(request.form.get("message")),
#         })
#         client.put(entity)
#     messages = []
#     for message in client.query(kind='Message').fetch():
#         print('message: {0}'.format(message))
#
#         messages.append(message)  # appending the message dict to the messages list
#     return render_template("index.html", messages=messages)


class Message(ndb.Model):
    message = ndb.StringProperty()

    @property
    def id(self):
        if self.key:
            return self.key.id()
        return None


@app.route('/', methods=['GET', 'POST'])
def index_test():
    print('yay starting query')
    messages = []
    with client.context():
        if request.method == "POST":
            key = client.key('Message')
            entity = Message(message=request.form.get("message"))
            entity.put()

        for message in Message.query():
            print('message: {0}'.format(message))

            messages.append(message)  # appending the message dict to the messages list
    return render_template("index.html", messages=messages)


if __name__ == '__main__':
    if debug:
        app.run(port=8080, host="localhost")  # localhost
    else: # os.getenv('GAE_ENV', '').startswith('standard')
        app.run()  # production

"""
A Flask file server for demonstrating application updates with PyUpdater.
"""
import logging
from flask import Flask, request
from Task1 import get_prescription
LOCALHOST = '0.0.0.0'

logger = logging.getLogger(__name__)

"""
Run a Flask file server on the given port.

Explicitly specify instance_path, because Flask's
auto_find_instance_path can fail when run in a frozen app.
"""
app = Flask(__name__)

@app.route('/', methods=['GET'])
def ready():  # pylint: disable=unused-variable
    return "API server is ready"


@app.route('/get-prescription', methods=['GET'])
def getprescription():  # pylint: disable=unused-variable
    """
    Used to get the prescription for ML module.
    """
    text = request.args['text']
    data = get_prescription(text.strip())
    print(text)
    return data


app.run(host=LOCALHOST, port=5000)

from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.kubernetes_information_acquire import KubernetesInformationAcquire
import datetime


app = Flask(__name__)


@app.route('/api/get-all-resource')
def get_all_resource():
    resource_list = ["pod", "service", "deployment", "node", "namespace"]
    result = {}
    now = datetime.datetime.now()
    for resource in resource_list:
        result[resource] = KubernetesInformationAcquire.get_resource(resource, now)
    return jsonify(result)


app.route('/api/')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

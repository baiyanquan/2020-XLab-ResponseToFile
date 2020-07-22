# -*- coding: utf-8 -*

import requests
import json
import os

from utils.config import Config


class KubernetesInformationAcquire(object):

    def __init__(self):
        pass

    @staticmethod
    def get_resource(resource_type, now):
        now_time = now.strftime('%Y-%m-%d %H-%M-%S')
        base_dir = Config.save_path + "/kubernetes_information"
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        dirs = Config.save_path + "/kubernetes_information/" + now.strftime('%Y-%m-%d %H')
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        json_data = ""
        if resource_type in Config.resource_in_namespace:
            for namespace in Config.namespaces:
                dir_namespace = dirs + "/" + namespace
                if not os.path.exists(dir_namespace):
                    os.makedirs(dir_namespace)
                info = requests.get(Config.resource_api[resource_type] + namespace)
                json_data = json.loads(info.text)
                filename = now_time + "_" + namespace + "_" + resource_type + ".json"
                with open(dir_namespace + "/" + filename, 'w') as file_obj:
                    json.dump(json_data, file_obj)
        else:
            info = requests.get(Config.resource_api[resource_type])
            json_data = json.loads(info.text)
            filename = now_time + "_" + resource_type + ".json"
            with open(dirs + "/" + filename, 'w') as file_obj:
                json.dump(json_data, file_obj)
        return json_data


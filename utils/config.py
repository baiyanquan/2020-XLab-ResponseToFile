# -*- coding: utf-8 -*


class Config(object):
    def __init__(self):
        pass

    base_url = "http://10.60.38.173:329"
    namespaces = [
        "sock-shop",
        "monitoring"
    ]
    save_path = "./file"
    resource_api = {
        "pod": base_url + "/tool/api/v1.0/get_pods/",
        "deployment": base_url + "/tool/api/v1.0/get_deployment/",
        "service": base_url + "/tool/api/v1.0/get_svc/",
        "node": base_url + "/tool/api/v1.0/get_node",
        "namespace": base_url + "/tool/api/v1.0/get_namespace",
    }
    resource_in_namespace = [
        "pod",
        "deployment",
        "service"
    ]


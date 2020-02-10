from flask import Blueprint

class BaseBlueprint(Blueprint):
    def __init__(self, name, import_name, static_folder=None,
                 static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None,
                 root_path=None):
        super(BaseBlueprint, self).__init__(name, import_name, static_folder=static_folder,
                 static_url_path=static_url_path, template_folder=template_folder,
                 url_prefix=url_prefix, subdomain=subdomain, url_defaults=url_defaults,
                 root_path=root_path)
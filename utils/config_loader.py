import yaml

def config_loader():
    confs = yaml.safe_load(open("config/test.yaml"))
    return confs

# coding:utf-8
import yaml
import logging.config
import os
config_path = os.path.join(os.path.dirname(__file__), 'logging.yaml')
def setup_logging(default_path = "logging.yaml",default_level = logging.INFO,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            logging.config.dictConfig(yaml.load(f))
    else:
        logging.basicConfig(level = default_level)

setup_logging(default_path=config_path,default_level=logging.INFO)

logger = logging.getLogger(__name__)
import os


ROOT_DIR= os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/"

CONFIG_DIR= ROOT_DIR + "config/"
DATA_DIR= ROOT_DIR + "data/"
TEMPLATE_DIR= ROOT_DIR + "templates/"
STATIC_DIR= ROOT_DIR + "static/"

###


FEED_CONFIG= CONFIG_DIR + "feeds.yaml"
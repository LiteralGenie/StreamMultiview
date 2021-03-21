import json
from .global_utils import *
from ruamel.yaml import YAML

def load_yaml(path, as_dict=False):
	if as_dict:
		y= YAML(typ='safe', pure=True)
	else:
		y= YAML()
	return y.load(open(path, encoding='utf-8'))

def dump_yaml(data, path):
	return YAML().dump(data, open(path, "w", encoding='utf-8'))

def load_json(path, default=None):
	if default is None: default= {}

	# make parent dirs if not exists
	if not os.path.exists(os.path.dirname(path)):
		os.makedirs(os.path.dirname(path))

	# load json, using default if necessary
	if os.path.exists(path):
		return json.load(open(path, encoding='utf-8'))
	elif default is not False:
		json.dump(default, open(path, "w"), indent=2)
		return default
	else:
		raise Exception(f"No default supplied and file does not exist: {path}")


def dump_json(data, path):
	# make parent dirs if not exists
	if not os.path.exists(os.path.dirname(path)):
		os.makedirs(os.path.dirname(path))

	# dont use \u characters
	json.dump(data, open(path,"w",encoding='utf-8'), ensure_ascii=False, indent=2)

def render(path, **kwargs):
	from mako.template import Template
	return Template(open(path, encoding='utf-8').read()).render(**kwargs)
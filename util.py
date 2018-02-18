import json
import os


def get_secreat(key):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "key.json")) as f:
        secret_file = json.load(f.read())
        print('secret_file : ', secret_file)
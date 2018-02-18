import json
import os


def get_secret(key:str) -> str:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print('basedir : ', BASE_DIR)
    with open(os.path.join(BASE_DIR, "key.json")) as f:
        try:
            secret_file = json.loads(f.read())
        except Exception as e:
            print("error : ",e)

    return secret_file[key]
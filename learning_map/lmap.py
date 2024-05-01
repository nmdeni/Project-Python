import json

def view_lmap(ldata):
    with open(ldata) as f:
        print(type(json.load(f)))

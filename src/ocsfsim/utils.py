import requests
import json

def get_base_event(url='https://schema.ocsf.io/sample/base_event?profiles=security_control'):
    r = requests.get(url)
    event = r.json()

    return event
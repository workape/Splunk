import requests
import json
import urllib3

urllib3.disable_warnings() # Don't do this in production, but all our certs in lab are self signed...

data = json.dumps({"index": "test", "source": "hec_test.py", "sourcetype": "python_script", "event": {"field1": "data1", "field2": "data2"}})

SPLUNK_INSTANCE = "172.16.12.131"
HEC_TOKEN = '6a029228-e9a8-42e0-ac8d-ab8d48ab73c4'
HEC_PORT = '8088'

HEC_URL = 'https://' + SPLUNK_INSTANCE + ':' + HEC_PORT + '/services/collector/event'
headers = {'Authorization': 'Splunk %s' % HEC_TOKEN, 'Connection': 'close'}


foo = requests.post(HEC_URL, headers=headers, data=data, verify=False)

print foo.status_code, foo.json()

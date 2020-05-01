import requests
import urllib3

urllib3.disable_warnings()

blah=['{"event": {"src": "de:ad:be:ef:00:00", "dot11_subtype": "beacon", "bssid": "00:00:de:ad:be:ef", "privacy": "WPA2", "rssi": -49, "dst": "ff:ff:ff:ff:ff:ff", "channel": 6, "ssid": "funtimes"}, "sourcetype": "dot11_mgmt", "time": 1582785809.000000}','{"event": {"src": "de:ad:be:ef:00:00", "dot11_subtype": "beacon", "bssid": "00:00:de:ad:be:ef", "privacy": "WPA2", "rssi": -49, "dst": "ff:ff:ff:ff:ff:ff", "channel": 6, "ssid": "funtime"}, "sourcetype": "dot11_mgmt", "time": 1582785810.0000}']

SPLUNK_INSTANCE = "172.16.12.131"
HEC_TOKEN = 'bc3c577b-3015-4f91-b333-364d0ee75a57'
HEC_PORT = '8088'

HEC_URL = 'https://' + SPLUNK_INSTANCE + ':' + HEC_PORT + '/services/collector/event'
headers = {'Authorization': 'Splunk %s' % HEC_TOKEN, 'Connection': 'close'}

event_data = ' '.join(blah)

foo = requests.post(HEC_URL, headers=headers, data=event_data, verify=False)

print foo.status_code, foo.json()

# Babbys First HEC Call

Utilizing HEC from the cli (hopefully you are on something with cUrl installed!) is a fairly straight forward process.

## cURL Call
curl -k "https://splunkserver.local:8088/services/collector" \
    -H "Authorization: Splunk CF179AE4-3C99-45F5-A7CC-3284AA91CF67" \
    -d '{"event": "Hello, world!", "sourcetype": "manual"}'

### cURL options
#### -k tells the command to make a POST HTTP Method Call
#### -H tells cURL to use the following headers
#### -d tells cURL to use the following data as the POST payload

## cURL example from CLI

laptop:~ workape$ curl -k "https://splunkserver.local:8088/services/collector" -H "Authorization: Splunk 6a029228-e9a8-42e0-ac8d-ab8d48ab73c4" -d '{"sourcetype": "hec_test", "event": "first time"}'

{"text":"Success","code":0}

With the text response of Success, we have achieved data insertion based on HEC!  Now go search for it, and remember that 
the data will be in the default index associated with your HEC token.  If you didn't define one, you can find it in the 
system default index (main or default depending on Splunk version).

For the -d portion, you can additionally add options such as defining the source (which you could grab the hostname, or
the sending application) or the index (to define where the data will reside within Splunk.) to allow a more programmatic
approach to utilizing HEC.

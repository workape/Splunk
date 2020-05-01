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

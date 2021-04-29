import requests
import json

def test_get_headers_body_json():
    url = 'http://httpbin.org/uuid'
    
    headers = {
            'Host': "httpbin.org",
            'Connection': "keep-alive",
            'User-Agent': "VSCode/1.55.2",
            'Accept': "*/*",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "en-US,en;q=0.9"
            }
    
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body["url"] == url
    
    print (response.text)
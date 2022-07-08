import requests

def request(verb: str, url: str, json: dict = None):

    method = None
    match verb:
        case 'get': method = requests.get
        case 'put': method = requests.put
        case 'post': method = requests.post
        case 'delete': method = requests.delete

    http_rsp = method(url, json=json)

    match http_rsp.status_code:
        case 200:
            return http_rsp.text 
        case _:
            return None

print(request('get', 'http://barkhuizen.com'))
print(request('post', 'https://httpbin.org/post', {'dog':'fish'}))


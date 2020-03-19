from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import requests
import time
a=time.time()

#Use get_it if HTTP/HTTPS request type is GET
def get_it(url):
    try:
        r = requests.get(url,timeout=5)
        return r.text
    except:
        pass
 
 ##Use post_it HTTPS/HTTP request type is POST
 
def post_it(url,data):
    try:
        r=requests.post(url,data=data,timeout=5)
        return r.text
      
     
urls = ["https://www.google.com"] * 400

with PoolExecutor(max_workers=96) as executor:
    for _ in executor.map(get_it, urls):
        pass

print(time.time()-a)

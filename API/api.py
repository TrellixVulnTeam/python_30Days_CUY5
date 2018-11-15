import requests
from requests_oauthlib import OAuth1
url ='https://www.food2fork.com/api/search'
params = {
    "key":"972895f3f9c5f9d69c49a85773b326bb",
    "q":"beef",
    "page":2
}
r = requests.get(url, params= params)
print(r.text)

def search_recipe(query, page):
    url ='https://www.food2fork.com/api/search'
    params = {
        "key":"972895f3f9c5f9d69c49a85773b326bb",
        "q":query.replace(' ','%20'),
        "page":page
    }
    r = requests.get(url, params= params)
    return r.json()

a = search_recipe("chicken breast",2)
for i in range(0,30,1):
    print(a["recipes"][i]["title"])

src="https://www.food2fork.com/about/api"
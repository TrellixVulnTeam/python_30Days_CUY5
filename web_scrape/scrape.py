import requests
from bs4 import BeautifulSoup
base = "https://www.yelp.com/search?find_loc="
loc='Newport+Beach'
current_page = 0
url = base + loc + "&start=" + str(current_page)

while current_page < 51:
    print(current_page)
    url = base + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    restaurant = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    i=0
    for a in restaurant:
        i=i+1
        title = a.findAll('a', {'class': 'biz-name'})[0].text
        print(title)
        address = a.findAll('address')[0].text.replace(' ','')
        print(address)
        category = a.findAll('span', {'class': 'category-str-list'})[0].text.replace(' ', '')
        print(str(i) + category) 
    current_page = current_page + 10

    
yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
print(yelp_soup.prettify())
print(yelp_soup.findAll('a'))
# for a in yelp_soup.findAll('div'):
#     print(a)
# print(yelp_soup.findAll('div', {'class': "main-header_logo"}))
for link in yelp_soup.findAll('div'):
    print(link)
# for a in yelp_soup.findAll('a', {'class': 'biz-name'}):
#     print(a.text)
# print(yelp_soup.findAll('a', {'class': "btn-primary btn-full-width"}))
i=0
for a in yelp_soup.findAll('div', {'class': 'biz-listing-large'}):
    i=i+1
    title = a.findAll('a', {'class': 'biz-name'})[0].text
    print(title)
    address = a.findAll('address')[0].text.replace(' ','')
    print(address)
    category = a.findAll('span', {'class': 'category-str-list'})[0].text.replace(' ', '')
    print(str(i) + category) 

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
file_path = 'yabc-{loc}.txt'.format(loc=loc)
with open(file_path, "a") as textfile:
    restaurant = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    i=0
    for a in restaurant:
        # print(a)
        i=i+1
        title = a.findAll('a', {'class': 'biz-name'})[0].text.strip(" \t\n\r ")
        # print(title)
        address = a.findAll('address')[0].text.replace(' ','').strip(" \t\n\r ")
        # print(address)
        category = a.findAll('span', {'class': 'category-str-list'})[0].text.replace(' ', '').strip(" \t\n\r ")
        # print(str(i) + category)
        page_line = "{title}\n{address}\n{category}\n\n".format(
                title=title,
                address=address,
                category = category
            )
        textfile.write(page_line) 


    

url = base + loc + "&start=" + str(70)
yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
restaurant = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
for a in restaurant:
    title = a.findAll('a', {'class': 'biz-name'})[0].text
    print(title)




try:
    a = [1,2,3]
    print(a[5])
except:
    print("hello")

r="               kkkkhariskkk             "
print(r.strip('k'))
print(r.strip(" \t "))






import requests
from bs4 import BeautifulSoup
base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc = 'Newport+Beach,+CA,+United+States'
current_page = 0

while current_page < 11:
    # print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
        for biz in businesses:
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            print(title)
            second_line = ""
            first_line = ""
            try:
                address = biz.findAll('address')[0].contents
                for item in address:
                    if "br" in str(item):
                        #print(item.getText())
                        second_line += item.getText().strip(" \n\t\r")
                    else:
                        #print(item.strip(" \n\t\r"))
                        first_line = item.strip(" \n\t\r")
                # print(first_line)
                # print(second_line)
            except:
                pass
            print('\n')
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(" \n\t\r")
            except:
                phone = None
            # print(phone)
            page_line = "{title}\n{address_1}{address_2}\n{phone}\n\n".format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    phone = phone
                )
            textfile.write(page_line)
    current_page += 10
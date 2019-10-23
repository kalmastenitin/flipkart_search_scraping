from bs4 import BeautifulSoup
import requests
import html5lib

user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
page_url = "https://www.flipkart.com/search?q="

query = input("Enter You Search Query: ")
final_url = page_url + query

response = requests.get(final_url, headers=user_agent)

soup = BeautifulSoup(response.content,'html5lib')
containers = soup.find_all("div",{"class":"bhgxx2 col-12-12"})

product_list = []
for container in containers:
    product_name = container.find("div", {"class":"_3wU53n"})
    product_rating = container.find("div", {"class":"hGSR34"})
    product_price = container.find("div", {"class":"_1vC4OE _2rQ-NK"})
    if product_name:
        product_item = product_name.get_text()
        product_item_rating = product_rating.get_text()
        product_item_price = product_price.get_text()
        product = { 'product_name': product_item,
        'product_rating':product_item_rating, 'product_price':product_item_price}
        product_list.append(product)

print(product_list)

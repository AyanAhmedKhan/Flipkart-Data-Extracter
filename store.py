
from bs4 import BeautifulSoup
import os
import pandas as pd

check=input("If your product is laptop or mobile then type yes else type no\n")
if check=="yes":
    titleclass='KzDlHZ'
    priceclass='Nx9bqj _4b5DiR'
    discountclass='UkUFwK'
    linkclass='tUxRFH'
    titletype='div'
    linktype='div'
else:
    titleclass='wjcEIp'
    priceclass='Nx9bqj'
    discountclass="UkUFwK"
    linkclass='VJA3rP'
    titletype='a'
    linktype='a'
    
d = {"title": [], "Price": [], "Discount": [], "link": []}

for file in os.listdir("data"):
    with open(os.path.join("data", file), 'r', encoding='utf-8') as f:
        html_doc = f.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    title_elem = soup.find(titletype, {'class':titleclass })
    if title_elem:
        title = title_elem.get_text(strip=True)
    else:
        title = None
    
    
    '''link_div = soup.find('div', {'class': 'tUxRFH'})
    if link_div:
        a_tag = link_div.find('a', class_='CGtC98')
        if a_tag:
            link = "https://www.flipkart.com" + a_tag.get('href')'''
    # Extract link
    if check=="yes":
        link_div = soup.find('div', {'class': 'tUxRFH'})
        if link_div:
            a_tag = link_div.find('a', class_='CGtC98')
            if a_tag:
                link = "https://www.flipkart.com" + a_tag.get('href')
    else:
        link = None
        link_div = soup.find('a', {'class': 'VJA3rP'})
        if link_div:
            link = "https://www.flipkart.com" + link_div.get('href')
    
    price_elem = soup.find('div', {'class': priceclass})

    #prc=soup.find('div',{'class': 'Nx9bqj _4b5DiR'})
    #price='₹'+prc.get_text().replace('â‚¹'," ")
    if price_elem:
        price = price_elem.get_text().replace('â‚¹',"  ")

    else:
        price = None
        
    
    
    
    discount_elem = soup.find('div', {'class': discountclass})
    if discount_elem:
        discount = discount_elem.get_text(strip=True)
    else:
        discount = None
    
    d['title'].append(title)
    d['Price'].append(price)
    d['Discount'].append(discount)
    d['link'].append(link)
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)


'''
from bs4 import BeautifulSoup
import os
import pandas as pd

check=input("If your product is laptop or mobile then type yes else type no")
if check=="yes":
    titleclass=
    priceclass=
    discountclass=
    linkclass=

# Initialize empty dictionary
d = {"title": [], "Price": [], "Discount": [], "link": []}

# Loop through files in 'data' directory
for file in os.listdir("data"):
    with open(os.path.join("data", file), 'r', encoding='utf-8') as f:
        html_doc = f.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # Extract title
    title_elem = soup.find('div', {'class': 'KzDlHZ'})
    if title_elem:
        title = title_elem.get_text(strip=True)
    else:
        title = None
    
    # Extract link
    link = None
    link_div = soup.find('div', {'class': 'tUxRFH'})
    if link_div:
        a_tag = link_div.find('a', class_='CGtC98')
        if a_tag:
            link = "https://www.flipkart.com" + a_tag.get('href')
    
    # Extract price
    price_elem = soup.find('div', {'class': 'Nx9bqj _4b5DiR'})

    #prc=soup.find('div',{'class': 'Nx9bqj _4b5DiR'})
    #price='₹'+prc.get_text().replace('â‚¹'," ")
    if price_elem:
        price = price_elem.get_text().replace('â‚¹',"  ")

    else:
        price = None
    
    # Extract discount
    discount_elem = soup.find('div', {'class': 'UkUFwK'})
    if discount_elem:
        discount = discount_elem.get_text(strip=True)
    else:
        discount = None
    
    # Append data to dictionary
    d['title'].append(title)
    d['Price'].append(price)
    d['Discount'].append(discount)
    d['link'].append(link)
# Create DataFrame
df = pd.DataFrame(data=d)

# Export to CSV
df.to_csv("data.csv", index=False)

'''

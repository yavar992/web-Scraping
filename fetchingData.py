import requests as re
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.zigwheels.com/newcars/cars-under-50-lakhs'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

data = re.get(url, headers)
# print(data)
soup = BeautifulSoup(data.text , 'html.parser')
# print(soup)

rowD = soup.find('div', class_='resultParent')
# print(rowD)

CarName =[]
CarPrice =[]
CarRating =[]


names = rowD.find_all('strong', class_='lnk-hvr')
print(names)


for i in names:
    name = i.text.strip()
    CarName.append(name)

# print( " available cars  --> " , CarName)    

prices = rowD.find_all('div', class_= 'clr-bl')
# print(prices)
for i in prices:
    price = i.text.strip()
    CarPrice.append(price)

# print(CarPrice)    

ratings = rowD.find_all('div' , class_ = 'i-b fnt-12 clr-try')
print(ratings)
for i in ratings:
    rating = i.text.strip()
    CarRating.append(rating)

print(CarRating) 

print("carname length --")
print(len(CarName))
print("carprice length --")
print(len(CarPrice))
print("carrating length --")
print(len(CarRating))


df = pd.DataFrame({
    'car Name' : CarName,
    'car Price': CarPrice, 
    'carRating':CarRating
})


    # Save the DataFrame to CSV and Excel files
df.to_csv('cars_under_50_lakhs.csv', index=False)
df.to_excel('cars_under_50_lakhs.xlsx', index=False)




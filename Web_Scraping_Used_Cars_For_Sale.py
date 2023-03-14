#Import
from bs4 import BeautifulSoup
import requests
from csv import writer

#First URL page
url = "https://www.zigwheels.ph/used-cars/cebu-city?"
page = requests.get(url)
#print(page) -- Checks http response status
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

#Data Scraping
soup = BeautifulSoup(page.content,"html.parser")
lists = soup.find_all ('div',class_="car-short-detail")

# Export the data to a CSV file
with open('Used_Cars_Cebu.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header =['Car_Unit', 'Car_Price (PHP)', 'Existing_Milage / Engine_Type / Seller_Location']
    thewriter.writerow(header)

    #Requesting data from URL
    for list in lists:
        car_unit = list.find('span',class_="car-heading truncate").text.replace('\n', '')
        price = list.find('span',class_="car-price").text.replace('\n', '')
        specs_and_location = list.find('div',class_="spec truncate").text.replace('\n', '')
        info = [car_unit, price, specs_and_location]
        thewriter.writerow(info)

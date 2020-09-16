from bs4 import BeautifulSoup as bs 
import pandas as pd
import requests
url='https://forecast.weather.gov/MapClick.php?lat=40.6229&lon=-79.1501'
page=requests.get(url)
soup=bs(page.content,'html.parser')
# print(soup)
weak=soup.find(id="seven-day-forecast-body")
items=weak.find_all(class_="tombstone-container")
# print(weak)
# print(items[0])
# print(items[0].find(class_="period-name").get_text())
# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp temp-high").get_text())
# list comprehensive
period_names=[item.find(class_='period-name').get_text() for item in items]
short_desc=[item.find(class_='short-desc').get_text() for item in items]
temp=[item.find(class_='temp').get_text() for item in items]
print(period_names)
print(short_desc)
print(temp)
# import pandas to create as a dataFrame
weather_stuff=pd.DataFrame({
    'period':period_names,
    'short_description':short_desc,
    'temperature':temp
})
print(weather_stuff)
# weather_stuff.to_csv('weather.csv')







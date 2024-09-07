import requests
import urllib3
import lxml.html


headers = {
    "User-agent":  'User-Agent'  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36 Brave/1.69.162'
}

html = requests.get("https://www.scrapethissite.com/pages/simple/", headers=headers)#opening the website using requests


doc = lxml.html.fromstring(html.content)#pass the above response to lxml.html.fromstring method
#print(html.text)

countries = doc.xpath("//div[@class='col-md-4 country']")
print(f"Number of countries found: {len(countries)}")

with open("output.txt", 'w', newline='', encoding='utf-8') as file:

    for country in countries:
        name = country.xpath(".//h3[@class='country-name']/text()[normalize-space()]")
        capital = country.xpath(".//span[@class='country-capital']/text()")
        population = country.xpath(".//span[@class='country-population']/text()")
        area =country.xpath(".//span[@class='country-area']/text()")


        #Etract the text from the lists or provide a default value
        name_text = name[0].strip() if name else "N/A"
        capital_text = capital[0].strip() if capital else "N/A"
        population_text= population[0].strip() if population else "N/A"
        area_text = area[0].strip() if area else "N/A"
        print(f"name: {name_text}, capital: {capital_text}, population: {population_text} Area: {area_text}")
    
        #trying to write the information onto an external file; am on fire hahaha!
        file.write(f"Name: {name_text}\n") 
        file.write(f"Capital: {capital_text}\n") 
        file.write(f"Population: {population_text}\n") 
        file.write(f"Area: {area_text}\n") 

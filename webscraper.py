import requests
import lxml.html
import ssl
import urllib3

urllib3.disable_warnings()

html = requests.get("https://www.scrapethissite.com/pages/simple/")#opening the website using requests
doc = lxml.html.fromstring(html.content)#pass the above response to lxml.html.fromstring method

new_releases = doc.xpath('//div[@class=col-md-4 country"]')
#Things went bad bad mate; I tried the site given on the project and it gave me a mind fuck considering am running on a network with sophos plus when I tried another site other fucking errors until I stopped @0156hrs

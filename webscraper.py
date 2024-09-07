import requests
import urllib3
import lxml.html
import ssl

urllib3.disable_warnings()

html = requests.get("https://www.scrapethissite.com/pages/simple/")#opening the website using requests
doc = lxml.html.fromstring(html.content)#pass the above response to lxml.html.fromstring method
print(doc)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

# Check if the element exists
if new_releases:
    titles = new_releases[0].xpath('.//div[@class="tab_item_name"]/text()')
    print(titles)
else:
    print("Element with id 'tab_newreleases_content' not found.")

# titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')

# new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')
#Things went bad bad mate; I tried the site given on the project and it gave me a mind fuck considering am running on a network with sophos plus when I tried another site other fucking errors until I stopped @0156hrs

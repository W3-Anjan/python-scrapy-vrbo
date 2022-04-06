import json
import scrapy
from bs4 import BeautifulSoup

from ..items import VrbodataItem


class VrbospyderSpider(scrapy.Spider):
    name = 'vrbos'

    start_urls = ['https://www.vrbo.com/vacation-rentals/beach/usa/florida']

    def parse(self, response):
        # script = response.xpath('//script[2]').re_first('\((\[.*\])\)')
        property_items = VrbodataItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find_all('script')[25].text.strip()[29:-1] # remove 1st 29 char
        data = json.loads(script)

        #  data['abacus']['ha_gdpr_banner']['bucket']
        destinations = data['destination']['listings']
        for destination in destinations:

            name = destination['propertyName']
            price = str(destination['price']['value'])
            thumb = destination['thumbnailUrl']
            details = destination['toplineDescription']

            #print("Pipeline Details :" + details + "\nName:" + name +"\nThumb: "+ thumb)
            #print("\nPrice :" + price)

            property_items['property_name'] = name
            property_items['property_price'] = price
            property_items['property_thumb'] = thumb
            property_items['property_details'] = details

            yield property_items

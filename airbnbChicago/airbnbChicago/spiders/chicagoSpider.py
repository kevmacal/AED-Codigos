from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy import selector
from scrapy.http import Request
from airbnbChicago.items import AirbnbchicagoItem


class chicagoSpider(CrawlSpider):
    name = 'chicagoSpider'
    allowed_domains = ['airbnb.com','airbnb.com.ec']
    start_urls = ['https://www.airbnb.com.ec/s/Chicago--Illinois--Estados-Unidos']

    custom_settings = {

        'DOWNLOAD_HANDLERS': {

            's3': None,
            }
    }

    rules = (

      Rule(
        LinkExtractor(restrict_xpaths=('//div[@class="pagination pagination-responsive"]/ul/li[@class="next next_page"]/a')),
        follow=True), 

      Rule(
        LinkExtractor(allow=r'/rooms/\d{5,8}.+',
          deny=r'https://www.airbnb.com.ec/users/show/\d{4,9}',
          restrict_xpaths=(['/html/head','//*[div[@class="listings-container"]/div[@class="row"]]'])),
         callback='parse_item'),

    ) 

    def parse_item(self, response):
      #/html/head/meta[18]
      #/html/head/meta[17]
       l = ItemLoader(item=AirbnbchicagoItem(), response=response)
       l.add_xpath('latitud','//meta[@property="airbedandbreakfast:location:latitude"]/@content')
       l.add_xpath('longitud','//meta[@property="airbedandbreakfast:location:longitude"]/@content')
       l.add_xpath('host_name', "//div[@class='row']/div[@class='col-md-3 text-muted text-center hide-sm']/a/text()")
       l.add_xpath('room_description',"//div[@class='row']/div[@class='col-md-9']/h1/text()")
       l.add_xpath('price_room',"//div[@class='row']/div[@class='col-sm-8']/div[@class='book-it__price-amount h3 text-special pull-left']/span/text()")
       yield l.load_item()

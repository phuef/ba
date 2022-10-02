import scrapy, os
import pandas as pd

class IvSpider(scrapy.Spider):
    name = "iv"
     
    def start_requests(self):
        f=os.path.abspath(__file__ + "/../../../../server/data/urls/toAnalyze.csv")
        data = pd.read_csv (f)
        df = pd.DataFrame(data, columns= ['urls']) 
        urls=df['urls'].tolist()   
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # xpath selectors to extract the needed information to classify the website   
        content=''
        description=''
        keywords=''
        if response.xpath("//meta[@name='keywords']/@content")!=[]:
            content=response.xpath("//meta[@name='keywords']/@content")[0].extract() # string
        description=response.xpath("//meta[@name='description']/@content")[0].extract() # string
        keywords=response.xpath("//meta[@name='keywords']/@content")[0].extract() # string
        external_links=response.xpath("//link/@href").extract() # array 
        external_scripts=response.xpath("//script/@src").extract() # array
        div_ids=response.xpath("//div/@id").extract() # array
        div_classes=response.xpath("//div/@class").extract() # array
        
        yield{
            'url': response.url,
            'content': content,
            'description': description, 
            'keywords': keywords,
            'external_links': external_links, 
            'external_scripts': external_scripts, 
            'div_ids': div_ids, 
            'div_classes': div_classes,
        }
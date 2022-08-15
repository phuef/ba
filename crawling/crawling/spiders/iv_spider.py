import scrapy, os
import pandas as pd


class IvSpider(scrapy.Spider):
    name = "iv"

    #returns a list of urls from a given file
    def getUrls(urls):
        data = pd.read_csv ('\\..\\server\\data\\urls\\{urls}.csv')
        df = pd.DataFrame(data, columns= ['urls']) # add 
        #print (df)
        return df['urls'].tolist()
    
    def start_requests(self):
        f=os.path.abspath(__file__ + "/../../../../server/data/urls/toAnalyze.csv")
        data = pd.read_csv (f)
        df = pd.DataFrame(data, columns= ['urls']) # add 
        #print (df)
        #return df['urls'].tolist()
        urls=df['urls'].tolist() 
        #urls = self.getUrls('IV')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")
        self.log(page)
        filename = f'{page}.html'
        #with open(os.path.abspath(__file__ + f'/../../../../server/data/html/toAnalyze/{filename}'), 'wb') as f:
         #   f.write(response.body)
        self.log(f'Saved file {filename}')
from lxml import html
import requests
import json
import pandas as pd

def getUrls(urls):
    data = pd.read_csv (f'urls\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls']) 
    return df['urls'].tolist()

def getJsonInfosOfUrl(url):
    help={'url': url}
    page = requests.get(url)
    tree = html.fromstring(page.content)
    content=''
    description=''
    keywords=''
    if tree.xpath("//meta[@name='keywords']/@content")!=[]:
        content=tree.xpath("//meta[@name='keywords']/@content")[0] # string
    help['content']=content
    if tree.xpath("//meta[@name='description']/@content") !=[]:
        description=tree.xpath("//meta[@name='description']/@content")[0] # string
    help['description']=description
    if tree.xpath("//meta[@name='keywords']/@content")!=[]:
        keywords=tree.xpath("//meta[@name='keywords']/@content")[0] # string
    help['keywords']=keywords
    external_links=tree.xpath("//link/@href") # array 
    help['external_links']=external_links
    external_scripts=tree.xpath("//script/@src") # array
    help['external_scripts']=external_scripts
    div_ids=tree.xpath("//div/@id") # array
    help['div_ids']=div_ids
    div_classes=tree.xpath("//div/@class") # array
    help['div_classes']=div_classes
    return help

def write_json(new_data, filename):
    with open(filename,'r+') as file:
        # load existing data into a dict
        file_data = json.load(file)
        # join new_data with file_data
        file_data.append(new_data)
        # sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

urlsToAnalyze=getUrls('toAnalyze')

for u in urlsToAnalyze:
    print(u)
    write_json(getJsonInfosOfUrl(u), 'scraped_data_analysation.json')

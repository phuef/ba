import pandas as pd, json, requests
from slugify import slugify


# returns a list of urls from a given file
def getUrls(urls):
    data = pd.read_csv (f'urls\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls']) # add 
    #print (df)
    return df['urls'].tolist()

# creates a json object for each url and saves it in another file
def createsAndSavesJson(filename, urls):
    jsonData=[]
    for url in urls:
        # microlink is an api that returns html data as a json from an url
        microlink = 'https://api.microlink.io'
        params = {'url': url}
        response = requests.get(microlink, params)
        screenshot= slugify(url) +'.png'
        #classifiedType=classifyWebsite("url")
        if response.status_code == 200:
            print (response.json)
            jsonData.append( 
                {
                    "url":url,
                    "topics": [],
                    "previewImageLink":"",
                    "type":"",
                    "description":"",
                    "screenshot":screenshot,
                    #"classifiedType":classifiedType,
                    "microlink": response.json()
                    
                    
                }
            )
            print(jsonData)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(jsonData, f, ensure_ascii=False, indent=4)
        
    
 
  
#urlsToAnalyze=getUrls('toAnalyze')
#urlsToAnalyze=getUrls('toEvaluate')

#createsAndSavesJson('json/ToEvaluateWithScreenshot.json', urlsToAnalyze)

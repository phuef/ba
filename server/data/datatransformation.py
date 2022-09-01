import pandas as pd, json, requests
from slugify import slugify


#returns a list of urls from a given file
def getUrls(urls):
    data = pd.read_csv (f'urls\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls']) # add 
    #print (df)
    return df['urls'].tolist()

# returns whether an given url has an interactive visualization (IV) or not
def isIV(url):
    # if the website has an external IV framework --> return true
    return False
    
# returns whether an given url has an interactive geo visualization (IGV) or not
def isIGV(url):
    # if the website has an external IV framework --> return true
    return False

# classifies a given website according to the decision tree   
def classifyWebsite(url):
    if isIV(url):
        return 'IV'
    if isIGV(url):
        return 'IGV'            
    return 'noIV'
 
#creates a json object for each url and saves it in another file
def createsAndSavesJson(filename, urls):
    jsonData=[]
    for url in urls:
        # microlink is an api that returns html data as a json from an url
        microlink = 'https://api.microlink.io'
        params = {'url': url}
        response = requests.get(microlink, params)
        screenshot= slugify(url) +'.png'
        classifiedType=classifyWebsite()
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
                    "classifiedType":classifiedType,
                    "microlink": response.json()
                    
                    
                }
            )
            print(jsonData)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(jsonData, f, ensure_ascii=False, indent=4)
        
    
    
urlsToAnalyze=getUrls('toAnalyze')

#urlsToAnalyze=getUrls('toEvaluate')

createsAndSavesJson('json/ToEvaluateWithScreenshot.json', urlsToAnalyze)

#url="https://google.com/"
#screenshot= requests.get("https://screenshot.abstractapi.com/v1/?api_key=25f26f7dc1de480e86079777d057c066&url=" + url)
#print(screenshot.status_code)
#print(screenshot.content)

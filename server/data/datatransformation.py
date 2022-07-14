import pandas as pd, json

#returns a list of urls from a given file
def getUrls(urls):
    data = pd.read_csv (f'urls\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls'])
    #print (df)
    return df['urls'].tolist()
    
#creates a json object for each url and saves it in another file
def createsAndSavesJson(filename, urls):
    jsonData=[]
    for url in urls:
        print (url)
        jsonData.append(
            {
                "url":url,
                "topics": [],
                "previewImage":"",
                "type":"",
                "description":""
                
            }
        )
        print(jsonData)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(jsonData, f, ensure_ascii=False, indent=4)
    
    
    
urlsToAnalyze=getUrls('toAnalyze')

#createsAndSavesJson('json/ToAnalyze.json', urlsToAnalyze)



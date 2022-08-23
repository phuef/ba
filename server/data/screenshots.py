import requests
import cv2, json, os
from html2image import Html2Image
import pandas as pd
import time
import re
from slugify import slugify
print(os.path)
def getUrls(urls):
    data = pd.read_csv(f'C:\\Users\\Phil\\OneDrive - Universität Münster\\Dokumente\\coding\\ba\\ba\\server\\data\\urls\\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls'])
    return df['urls'].tolist()

def get_screenshot_of_website(url):
    response = requests.get(f"https://screenshot.abstractapi.com/v1/?api_key=25f26f7dc1de480e86079777d057c066&url={url}")
    print(response.status_code)
    print(response.content)
    return response.content
    
#response=get_screenshot_of_website('https://wiediversistmeingarten.org/view/')
#result=cv2.imwrite('\test.png', response)



# api -> https://pypi.org/project/html2image/
hti = Html2Image()
#ToDo: replace absolute path with relative
hti.output_path = 'C:\\Users\\Phil\\OneDrive - Universität Münster\\Dokumente\\coding\\ba\\ba\\server\\data\\previewImages'

def saveScreenshot(url):
    #print(slugify(url) +'.png')
    hti.screenshot(url=url,save_as=slugify(url) +'.png')

urlsToEvaluate=getUrls('toEvaluate')

#print(urlsToEvaluate)
for url in urlsToEvaluate: 
    #print(url)
    saveScreenshot(url)

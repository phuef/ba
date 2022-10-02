import requests
from html2image import Html2Image
import pandas as pd
from slugify import slugify

# returns the urls of a csv file as a list 
def getUrls(urls):
    data = pd.read_csv(f'C:\\Users\\Phil\\OneDrive - Universität Münster\\Dokumente\\coding\\ba\\ba\\server\\data\\urls\\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls'])
    return df['urls'].tolist()


# first try of getting screenshots with the abstract API - was not used in the end due to limitations
def get_screenshot_of_website(url):
    response = requests.get(f"https://screenshot.abstractapi.com/v1/?api_key=25f26f7dc1de480e86079777d057c066&url={url}")
    print(response.status_code)
    print(response.content)
    return response.content


# getting screenshots using the Html2Image package
# api link -> https://pypi.org/project/html2image/
hti = Html2Image(
    # customizing flags:
    # --virtual-time-budget -> waiting a certain amount of time to let the website finish loading
    # --hide-scrollbars -> hiding the scrollbars of the website
    custom_flags=['--virtual-time-budget=10000', '--hide-scrollbars']   
)

# the output path is the folder in which the screenshots will be saved
# ToDo: replace absolute path with relative
hti.output_path = 'C:\\Users\\Phil\\OneDrive - Universität Münster\\Dokumente\\coding\\ba\\ba\\server\\data\\previewImages'

# makes a screenshot of the website with the given url and saves the screenshot 
def saveScreenshot(url):
    hti.screenshot(url=url,save_as=slugify(url) +'.png')



urlsToEvaluate=getUrls('toEvaluate')

# saves a screenshot for each url with a slugified name
for url in urlsToEvaluate: 
    saveScreenshot(url)

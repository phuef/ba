import requests
def get_screenshot_of_website(url):
    response = requests.get(f"https://screenshot.abstractapi.com/v1/?api_key=25f26f7dc1de480e86079777d057c066&url={url}")
    print(response.status_code)
    print(response.content)
    return response
    
response=get_screenshot_of_website('https://wiediversistmeingarten.org/view/')
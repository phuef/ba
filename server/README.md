# HowTo
To start the server, run the server.py file:
```
python server.py 
```

You can now run search queries on the server according to the following syntax:
http://localhost:5000/search?search_query=*your search query*

As a result you will get an array with the found objects. 



# Example

http://localhost:5000/search?search_query=human

result:
```
[
  {
    "description": "", 
    "microlink": {
      "data": {
        "author": "Tim Taylor", 
        "date": "2022-08-15T14:59:44.000Z", 
        "description": "Explore the anatomy of the human cardiovascular system (also known as the circulatory system) with our detailed diagrams and information.", 
        "image": {
          "height": 60, 
          "size": 1097, 
          "size_pretty": "1.1 kB", 
          "type": "jpg", 
          "url": "https://innerbody.imgix.net/Tim-Taylor-BW.jpg?w=60&auto=format", 
          "width": 60
        }, 
        "lang": "en", 
        "logo": {
          "height": 180, 
          "size": 1836, 
          "size_pretty": "1.84 kB", 
          "type": "png", 
          "url": "https://www.innerbody.com/apple-touch-icon.png", 
          "width": 180
        }, 
        "publisher": "Innerbody", 
        "title": "Cardiovascular System - Human Veins, Arteries, Heart", 
        "url": "https://www.innerbody.com/image/cardov.html"
      }, 
      "headers": {
        "age": "46341", 
        "cf-cache-status": "HIT", 
        "cf-ray": "73b2cbbbcee019f3-EWR", 
        "content-encoding": "br", 
        "content-type": "text/html; charset=utf-8", 
        "date": "Mon, 15 Aug 2022 14:59:44 GMT", 
        "expect-ct": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\"", 
        "nel": "{\"success_fraction\":0,\"report_to\":\"cf-nel\",\"max_age\":604800}", 
        "report-to": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=6slIlHNBjLIkMojplenuUVBL2G%2F%2BPh8dhym6vGjf%2FsksddeV7MWQbsATqdlNIugFTtetw12aLs1roZeEZPe9CTbtQv1A8HAgCbI0hR6MKWkh5yhnvx4olDiEImnSK9w2T13%2F\"}],\"group\":\"cf-nel\",\"max_age\":604800}", 
        "server": "cloudflare", 
        "vary": "Accept-Encoding"
      }, 
      "status": "success", 
      "statusCode": 200
    }, 
    "previewImageLink": "", 
    "screenshot": "https-www-innerbody-com-image-cardov-html.png", 
    "topics": [
      "body", 
      "human", 
      "inner", 
      "cardiovascular", 
      "system", 
      "organ"
    ], 
    "type": "", 
    "url": "https://www.innerbody.com/image/cardov.html"
  }
]
```
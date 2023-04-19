
# About
This repository contains a prototypical implementation of a search engine for interactive (geo) visualizations. It consists of a server handling the search queries and a website providing the user interface. 

# Website
The User Interface enables the user to search for keywords, through the search bar.
![image](https://user-images.githubusercontent.com/46593824/232992149-62121c0d-9909-4564-bea2-df8394b2f586.png)
After a search, it retrieves a set of websites that fit the search and displays them to the user. This might look like the following:
![image](https://user-images.githubusercontent.com/46593824/232753562-1a2b7d58-d06d-4043-a38c-8fdec4a3a34e.png)
The user interface consists of a few additional features, which were thought of as useful when looking through search results of web-based interactive (geo) visualizations . For example a preview image, to see what the website is about and how the visualization looks like.
![image](https://user-images.githubusercontent.com/46593824/232756622-04d417b2-28f1-4311-bba0-f56fa1781cf9.png)
Tags to see what the website is about. These tags can be clicked and the search engine will show all websites containing the clicked tag. 

![image](https://user-images.githubusercontent.com/46593824/232756986-6e27db97-b6fd-4f73-8fe0-f578e0e6b449.png)

# Server 
The server handles the search queries from the website and returns websites, fitting the search. The search is performed on a fixed set of websites. 
## requests

### GET /search
**Parameters**:
search_query - a string which the websites must contain 

**Response**: 
An Array of Websites 

**Example**:
/search?search_query=3d

**Example Response**:
[
  {
    "description": "",
    "microlink": {
      "data": {
        "author": "pbpmaps",
        "date": "2022-08-15T14:58:54.000Z",
        "description": "Map created by pbpmaps in CARTO",
        "image": {
          "height": 630,
          "size": 122514,
          "size_pretty": "123 kB",
          "type": "png",
          "url": "https://a.gusc.cartocdn.com/pbpmaps/api/v1/map/static/named/tpl_45180c5a_29d4_11e7_8c77_0e05a8b3e3d7/1200/630.png",
          "width": 1200
        },
        "lang": "en",
        "logo": {
          "height": 16,
          "size": 637,
          "size_pretty": "637 B",
          "type": "ico",
          "url": "https://libs.cartocdn.com/cartodbui/assets/1.0.0-assets.290/favicons/favicon.ico",
          "width": 16
        },
        "publisher": "CARTO",
        "title": "Case Map for PBP Website",
        "url": "https://pbpmaps.carto.com/builder/45180c5a-29d4-11e7-8c77-0e05a8b3e3d7/embed"
      },
      "headers": {
        "age": "0",
        "cache-control": "no-cache,max-age=86400,must-revalidate,public",
        "content-encoding": "gzip",
        "content-type": "text/html; charset=utf-8",
        "date": "Mon, 15 Aug 2022 14:58:54 GMT",
        "status": "200 OK",
        "surrogate-key": "rp rv:44Je/t",
        "vary": "Accept-Encoding",
        "x-cache": "HIT",
        "x-cartodb-rev": "",
        "x-cdb-type": "embed",
        "x-content-type-options": "nosniff",
        "x-request-id": "3f7ff141-ed80-4c0b-cc6b-c05edf93c79f",
        "x-runtime": "0.217928",
        "x-varnish": "16552505 6363201",
        "x-xss-protection": "1; mode=block"
      },
      "status": "success",
      "statusCode": 200
    },
    "previewImageLink": "",
    "screenshot": "https-pbpmaps-carto-com-builder-45180c5a-29d4-11e7-8c77-0e05a8b3e3d7-embed.png",
    "topics": [
      "case",
      "map",
      "pb",
      "case",
      "dollar"
    ],
    "type": "",
    "url": "https://pbpmaps.carto.com/builder/45180c5a-29d4-11e7-8c77-0e05a8b3e3d7/embed"
  },
  {
    "description": "",
    "microlink": {
      "data": {
        "author": "MapTiler AG",
        "date": "2022-08-15T14:16:00.000Z",
        "description": "3D map of the entire world for your applications. Combine our 3D terrain with a street or satellite map to get a photorealistic bird\u00e2\u20ac\u2122s view.",
        "image": {
          "height": 512,
          "size": 173575,
          "size_pretty": "174 kB",
          "type": "png",
          "url": "https://www.maptiler.com/img/share/share-maps.png",
          "width": 1024
        },
        "lang": "en",
        "logo": {
          "height": 192,
          "size": 4192,
          "size_pretty": "4.19 kB",
          "type": "png",
          "url": "https://www.maptiler.com/img/favicon/android-chrome.png",
          "width": 192
        },
        "publisher": "maptiler.com",
        "title": "3D map of the entire world preview | MapTiler",
        "url": "https://www.maptiler.com/maps/3d/"
      },
      "headers": {
        "cf-cache-status": "DYNAMIC",
        "cf-ray": "73b2cb152df4198e-EWR",
        "content-encoding": "br",
        "content-type": "text/html",
        "date": "Mon, 15 Aug 2022 14:59:18 GMT",
        "etag": "W/\"7988-5e648456839e4-gzip\"",
        "expect-ct": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\"",
        "last-modified": "Mon, 15 Aug 2022 14:16:00 GMT",
        "server": "cloudflare",
        "vary": "Accept-Encoding"
      },
      "status": "success",
      "statusCode": 200
    },
    "previewImageLink": "",
    "screenshot": "https-www-maptiler-com-maps-3d-10-7466-46-7681-11992-270-20.png",
    "topics": [
      "3d",
      "satellite",
      "terrain",
      "map",
      "search"
    ],
    "type": "",
    "url": "https://www.maptiler.com/maps/3d/#10.7466/46.7681/11992/270/-20"
  }
]
### GET /img
**Parameters**:
url - a string of the path of the website. The path is composed of the slugified url & ".png" 

**Response**:
An image 

**Example**:
/img?img=https-www-google-com-maps.png

**Example Response**:
![image](https://user-images.githubusercontent.com/46593824/233049777-26c25cfb-5a34-4c55-9865-6fb288f2979e.png)

# start server

```
cd server 
python server.py 
```

# start website 

```
cd website
npm run serve
```

# Explanation of some other stuff
## gathering of preview images
The screenshots were gathered using the python package Html2image. The code can be found in the file screenshots.py under server/data.
## operating of the search
The server checks whether the input-string is equal to one of the “topics” for each website. If yes, the website gets added to the search results. Additionally, it is checked whether the input-string is part of the url. 
## webscraping
The retrieval of the data is done via web scraping. The code can be found in the file scrape_websites under server/data. It reads a csv of urls and creates a json file with some information about the websites.The JSON file contains the following fields:
* **url** - the url of the website as a string
* **content** - the content, provided in the metadata of the HTML 
* **description** - the description, provided in the metadata of the HTML 
* **keywords** - the keywords, provided in the metadata of the HTML, as a string. Keywords are seperated by commata.
* **external_links** - an array of all external links loaded in the HTML file
* **external_scripts** - an array of all external scripts loaded in the HTML file
* **div_ids** - an array of all ids of divs in the HTML document
* **div_classes** - an array of all classes of divs in the HTML document


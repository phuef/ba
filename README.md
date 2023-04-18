
# About
This repository contains a prototypical implementation of a search engine for interactive (geo) visualizations. It consists of a server handling the search queries and a website providing the user interface.

# Website
The User Interface, in form of a website, enables the user to search for keywords. After a search it retrieves a set of websites that fit the search. This might look like the following:
![image](https://user-images.githubusercontent.com/46593824/232753562-1a2b7d58-d06d-4043-a38c-8fdec4a3a34e.png)
The user interface consists of a few additional features, which were thought of as useful when looking through search results of web-based interactive visualizations . For example a preview image, to see directly what the website is about.
![image](https://user-images.githubusercontent.com/46593824/232756622-04d417b2-28f1-4311-bba0-f56fa1781cf9.png)
Tags to see what the website is about. 

![image](https://user-images.githubusercontent.com/46593824/232756986-6e27db97-b6fd-4f73-8fe0-f578e0e6b449.png)

These tags can be clicked and the search engine will show all websites containing this tag. 

# Server 
The server handles the input from the search of the website and returns websites, fitting the search. The search is performed on a fixed set of websites. 
## requests

### GET /search
**Parameters**:
search_query - string which the websites must contain 

**Response**: 
An Array of Websites 

### GET /img
**Parameters**:
url - string of the website url

**Response**:
An image 

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

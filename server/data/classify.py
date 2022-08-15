import os
# assign directory

        
        
# returns whether an given url has an interactive visualization (IV) or not
def isIV(url):
    # if the website has an external IV framework --> return true
    return False
    
# returns whether an given url has an interactive geo visualization (IGV) or not
def isIGV(url):
    # if the website has an external IV framework --> return true
    return False


# returns the classification of an url as an string. Possible outcomes are 'IV', 'IGV' or 'noIV' 
def getWebsiteType(url):
    if isIV(url):
        return 'IV'
    if isIGV(url):
        return 'IGV'            
    return 'noIV'

# classifies 
def classifyAllWebsites(directory): 
    for filename in os.listdir(directory): # iterate over files in a directory
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f)


directoryToAnalyze = 'html/toAnalyze'
b=classifyAllWebsites(directoryToAnalyze)
a=getWebsiteType("https://wiediversistmeingarten.org/view/")
print(b)
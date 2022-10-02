import pandas as pd, json

#returns a list of urls from a given file
def getUrls(urls):
    data = pd.read_csv (f'urls\{urls}.csv')
    df = pd.DataFrame(data, columns= ['urls']) # add 
    #print (df)
    return df['urls'].tolist()

# returns if any string of an Array is in Any of the Strings of another Array
def isAStringOfArray2InAStringOfArray1(array1, array2):
    for a1 in array1:
        for a2 in array2:
            if a2 in a1:
                return True
    return False

# C4
def includesIVFrameworkName(array):
    ivFrameworkNames =['highcharts', 'recharts', 'tableau', 'd3', 'apexcharts', 'chartkick', 'amcharts', 'dataviz']
    return isAStringOfArray2InAStringOfArray1(array, ivFrameworkNames)
# C5
def includesIGVFrameworkName(array):
    igvFrameworkNames =['leaflet', 'cartodb', 'earth-js', 'earth.js', 'esri', 'mapboxgl', 'cartovista', 'strava', 'mangomap', 'amcharts', 'maptiler']
    return isAStringOfArray2InAStringOfArray1(array, igvFrameworkNames)
# C6
def containsPhraseWhichIndicatesItIsAnIV(description, title):
    phrases=['interactive', 'interactive visualisierung', 'Datenvisualisierung']
    db=isAStringOfArray2InAStringOfArray1(description, phrases)
    tb=isAStringOfArray2InAStringOfArray1(title, phrases)
    return db or tb
# C7
def containsPhraseWhichIndicatesItIsAnIGV(description, title):
    phrases=['map', 'interactive', 'geovisualisierung', 'geovisualization']
    db=isAStringOfArray2InAStringOfArray1(description, phrases)
    tb=isAStringOfArray2InAStringOfArray1(title, phrases)
    return db or tb
# C8
def containsElementWithIdWhichIndicatesItIsAnIV(elementIds):
    ids=['apexcharts', 'highchart', 'viz', 'viz-client-container'] # viz mit reinnehmen?
    return isAStringOfArray2InAStringOfArray1(elementIds, ids)
# C9
def containsElementWithIdWhichIndicatesItIsAnIGV(elementIds):
    ids=['map', 'globe', 'county-map', 'cartoVistaDiv', 'mapholder']
    return isAStringOfArray2InAStringOfArray1(elementIds, ids)
# C10
def containsElementWithClassWhichIndicatesItIsAnIV(classNames):
    classIds=['apexcharts', 'tableau','highchart', 'recharts', 'VictoryContainer', 'rv-xy-plot', 'v-charts', 'map']
    return isAStringOfArray2InAStringOfArray1(classNames, classIds)
# C11
def containsElementWithClassWhichIndicatesItIsAnIGV(classNames):
    classIds=['esri', 'esri-map', 'mapboxgl', 'cortoVista', 'leaflet']
    return isAStringOfArray2InAStringOfArray1(classNames, classIds)

# helpfunction two of {C7,C9,C11}
def areTwoOfC7C9C11True(description, title, elementIds, classNames):
    phrase=containsPhraseWhichIndicatesItIsAnIGV(description, title)
    id=containsElementWithIdWhichIndicatesItIsAnIGV(elementIds)
    clas=containsElementWithClassWhichIndicatesItIsAnIGV(classNames)
    if clas and phrase:
        return True
    elif clas and id:
        return True
    elif phrase and id:
        return True
    else:
        return False

# helpfunction two of {C6,C8,C10}
def areTwoOfC6C8C10True(description, title, elementIds, classNames):
    phrase=containsPhraseWhichIndicatesItIsAnIV(description, title)
    id=containsElementWithIdWhichIndicatesItIsAnIV(elementIds)
    clas=containsElementWithClassWhichIndicatesItIsAnIV(classNames)
    if clas and phrase:
        return True
    elif clas and id:
        return True
    elif phrase and id:
        return True
    else:
        return False

# C1 is true if C4 or two of {C6, C8, C10} are true 
def isIV(external_links, external_scripts, description, content, elementIds, classNames):
    if includesIVFrameworkName(external_links) or includesIVFrameworkName(external_scripts):
        return True
    elif areTwoOfC6C8C10True(description, content, elementIds, classNames):
        return True
    else:
        return False
    
# C2 is true if C5 or two of {C7, C9, C11} are true 
def isIGV(external_links, external_scripts, description, content, elementIds, classNames):
    if includesIGVFrameworkName(external_links) or includesIGVFrameworkName(external_scripts):
        return True
    elif areTwoOfC7C9C11True(description, content, elementIds, classNames):
        return True
    else:
        return False


    
# classifies each website in the file with the given filename
# the syntax of the given file has to be a json with the following attributes:
# {url:String,content:String,description:String,keywords:String,external_links:Array,external_scripts:Array,div_ids:Array,div_classes:Array}

def classify(filename):
    #f=pd.read_json(f'json\{filename}.json')
    #print(f)
    with open(f'json\{filename}.json') as f:
        d = json.load(f)
        for i in d:
            print(i['url'])
            if isIGV(i['external_links'],i['external_scripts'], i['description'], i['content'], i['div_ids'], i['div_classes']):
                i['classifiedType']='IGV'
                print('IGV')
            elif isIV(i['external_links'],i['external_scripts'], i['description'], i['content'], i['div_ids'], i['div_classes']):
                i['classifiedType']='IV'
                print('IV')

            else:
                i['classifiedType']='noIV' # C3
                print('noIV')
            
    f.close()
    


# classifies the file 'scraped_data_evaluation' out of the json folder
classify('scraped_data_evaluation')
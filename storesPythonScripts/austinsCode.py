import csv
import googlemaps
import time

from bs4 import BeautifulSoup

import requests
gmaps = googlemaps.Client(key="AIzaSyCXO2FQu10Ru7KANRnVLcCJsVCmH5L33fM")



master = []
urls = []
dirty = []
Statelinks = []
other = []
with open('pantriesCSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|')
    for row in readCSV:
        #print(row)
        for i in row:
           # print(i)
            dirty.append(i)
def genLinks(dirtyList, linkList):

    for noodle in dirtyList:
        #formattedBank = bank.split(" ",1)
        bowl = BeautifulSoup(noodle,features="html.parser")
        #links.append(bowl.find_all('a', href = True))
        #other.append(bowl.find_all('a', attrs={'class':'href'}))
        for a in bowl.find_all('a', href=True):
            #print ("Found the URL:", a['href'])
            linkList.append(a["href"])   # statelinks done forward them onward to get towns
    return linkList



Statelinks = genLinks(dirty,Statelinks)


tableCount = 0
townLinks = []
dirtyTownTable = []
#print(Statelinks)
for url in Statelinks:#[0:2]
    locations = []
    if url == "URL":
        master[0].append(['locations'])
        continue
    else:
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        for table in soup.find_all('table'):
            dirtyTownTable.append(table)





 #   bowl = BeautifulSoup(noodle,features="html.parser")
 ###  #other.append(bowl.find_all('a', attrs={'class':'href'}))
 #   for a in bowl.find_all('a', href=True):
 #       #print ("Found the URL:", a['href'])
 #       townLinks.append(a["href"])   # statelinks done forward them onward to get towns



print("--------------TEST________________")
#print("Dirttowntable",dirtyTownTable)

more = []
#print(dirtyTownTable[0])
for i in range(0,(len(dirtyTownTable)-1)):
    StringedTownTable = str(dirtyTownTable[i])
    more.extend(StringedTownTable.split("<td>"))
#print(more)
townLinks = genLinks(more,townLinks)


print("StateLinks",Statelinks)
print("TownLinks",townLinks)
jsonBS = []
lines =[]

dicts = []

iList=[]
intab = "\r\n\t{}"
outtab = ""
for url in townLinks:#[0:2]
    if url == "URL":
        master[0].append(['locations'])
        continue
    else:
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        #print(soup.prettify())
        blogs = soup.findAll("script",{"type":"application/ld+json"})
        jsonBS = ([b.string for b in blogs])
        #print(jsonBS)
        #print(jsonBS)
        for i in jsonBS:
            i = str(i)
            i.strip()
            i = i.replace("{","")
            i = i.replace("}","")
            iList=( i.split(",",9))
    dict = {}
    for i in range(0,(len(iList)-1)):

        if i == 2:
            b4seg = iList[i]
            b4seg = b4seg.strip()
            #print(b4seg)
            Seg = b4seg.split(":",1)
            #print(Seg)
            iList[2] = Seg[1].strip()
            #print(iList[2])
        #print("ilist[i]",iList[i])
        kv = iList[i].split(":") # key value pairing
        #print("kv",kv)
        try:
            dict[kv[0].strip().replace('"',"").replace("'","")]=kv[1].strip().replace('"',"").replace("'","")   # cleans up all that tag stuff
        except IndexError:
            continue
        dicts.append(dict)
for dict in dicts:
    try:
        Address = dict["streetAddress"]+", "+dict["addressLocality"]+", "+dict["addressRegion"]
        #print(Address)
    except KeyError:
        print("dict: ",dict)
    for val in dict:
        print(val,"  ",dict[val])
    print("KEYS: ",dict.keys())
    geocode_result = gmaps.geocode(Address)
    # Geocoding an address
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    line = [dict["name"], [lat, lng]]
    lines.append(line)
print(lines)






'''
  Address =  dict["streetAddress"]+", "+dict["addressLocality"]+", "+dict["addressRegion"]
        print(Address)
        geocode_result = gmaps.geocode(Address)
        # Geocoding an address
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        line = [dict["name"], [lat, lng]]
        lines.append(line)
        print(lines)









            Segs = iList[i][2].split(":", 1)
            print("Segs",Segs)
            #idealSpot = iList[i][2]
            #idealSpot = Segs[1]
            cleanLine =iList[i][2].strip()
            iList[i] = cleanLine
            kv = iList[i].split(":",1)
            dict[kv[0].replace('"',"")]=kv[1].replace('"',"")
        for val in dict:

                        print(val,"  ",dict[val])
                #print(iList)









Address =  dict["streetAddress"]+", "+dict["addressLocality"]+", "+dict["addressRegion"]
print(Address)
geocode_result = gmaps.geocode(Address)
# Geocoding an address
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
line = [dict["name"], [lat, lng]]
lines.append(line)
print(lines)


'''






















'''
            for row in table.findAll("tr"):
                location = []
                cells = row.findAll("td")
                if cells[0].string == "Store #":
                    locations.append([''])
                    continue
                for cell in cells:
                    if cells.index(cell) == 0:
                        continue
                    location.append(cell.string)
                locations.append(location)
        master[urls.index(url)].append(locations)
print(master)








    
    
    
for noodle in dirty:
    #formattedBank = bank.split(" ",1)
    bowl = BeautifulSoup(noodle,features="html.parser")
    #links.append(bowl.find_all('a', href = True))
    #other.append(bowl.find_all('a', attrs={'class':'href'}))
    for a in bowl.find_all('a', href=True):
        print ("Found the URL:", a['href'])
        Statelinks.append(a["href"])   # statelinks done forward them onward to get towns
'''

from math import *


def check( iden, d):
    if iden in d.id.values:
        return True
    else:
        return False
    

def coords(identity, d):
    if check(identity, d)==True:
        log=[]
        latitude = d[d.id==identity].lat
        log.append(latitude)
        longitude=d[d.id==identity].long
        log.append(longitude)
        return log
    else:
        return "cannot find id"
    

def distance(id1, id2, dd):

    log1=coords(id1,dd)
    log2=coords(id2,dd)
    lon1 = radians(log1[1])
    lon2 = radians(log2[1])
    lat1 = radians(log1[0])
    lat2 = radians(log2[0])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)    



def pricediff(id1, id2, dd):

    price1= dd[dd.id==id1].price.item() 
    price2= dd[dd.id==id2].price.item()
    diff = price1 - price2
    return diff
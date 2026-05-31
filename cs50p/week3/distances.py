distance = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 10": "44 AU"
}

def main():
    spacecraft = input ("Enter spacecraft: ")

    try:
        au = float (distance[spacecraft])
    except KeyError:
        print (f"'{spacecraft}' is not in dictionary")
        return 
    except ValueError:
        print (f"Can't convert '{distance[spacecraft]}' float")
        return
    
    m = convert (au)
    print (f"{m} m away")

def convert (au):
    return au * 149597870700
    
main ()
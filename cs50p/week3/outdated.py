months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = input ("Date: ").strip()
        if "/" in date:
            parts = date.split ("/")
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        else:
            if "," not in date:
                raise ValueError
            parts = date.split (" ")
            month = months.index(parts[0]) + 1
            day = int(parts[1].replace ("," , ""))
            year = int(parts[2])

        if 1<= month <= 12 and 1<= day <= 31:
            print (f"{year}-{month:02}-{day:02}")
            break


    except ValueError:
        pass





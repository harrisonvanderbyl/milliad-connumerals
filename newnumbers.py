vowels = [
    "error",
    "u",
    "e",
    "i",
    "æ",
    "ɛ",
    "ɪ",
    "ʌ",
    "oʊ",
    "oi"
]

prefixes = [
    "d",
    "th",
    "l",
    "g",
    "b",
    "f",
    "s",
    "m",
    "p"
]

suffixes = [
    "n",
    "sh"
]

def convertMilliadints(threechars):
    if(threechars.__len__() < 3):
        threechars = "0" + threechars
    if(threechars.__len__() < 3):
        threechars = "0" + threechars

    if threechars == "000":
        return ""
    if threechars[1:] == "00":
        return vowels[int(threechars[0])] + "kn" 
    
    if threechars[:2] == "00":
        return vowels[int(threechars[2])] + "n"
    
    if threechars[2] == "0" and threechars[0] == "0":
        return vowels[int(threechars[1])] + "nk"
    
    if threechars[1] == "0":
        return vowels[int(threechars[0])] + "nk" + vowels[int(threechars[2])]
    
    if threechars[2] == "0":
        return vowels[int(threechars[0])] + "n" + vowels[int(threechars[1])] + "k"
   
    if threechars[0] == "0":
        return vowels[int(threechars[1])] + "n" + vowels[int(threechars[2])]
    
    return vowels[int(threechars[0])] + "n" + vowels[int(threechars[1])] + "n" + vowels[int(threechars[2])]

def convertMilliadpartials(threechars):
    if(threechars.__len__() < 3):
        threechars = threechars + "0"
    if(threechars.__len__() < 3):
        threechars = threechars + "0" 

    if threechars == "000":
        return ""
    if threechars[1:] == "00":
        return vowels[int(threechars[0])] + "ksh" 
    
    if threechars[:2] == "00":
        return vowels[int(threechars[2])] + "sh"
    
    if threechars[2] == "0" and threechars[0] == "0":
        return vowels[int(threechars[1])] + "shk"
    
    if threechars[1] == "0":
        return vowels[int(threechars[0])] + "shk" + vowels[int(threechars[2])]
    
    if threechars[2] == "0":
        return vowels[int(threechars[0])] + "sh" + vowels[int(threechars[1])] + "k"
   
    if threechars[0] == "0":
        return vowels[int(threechars[1])] + "sh" + vowels[int(threechars[2])]
    
    return vowels[int(threechars[0])] + "sh" + vowels[int(threechars[1])] + "sh" + vowels[int(threechars[2])]


def convertToNew(number):
    string = f"{number:.9f}"
    
    splits = string.split(".")
    if len(splits) > 1:
        whole = splits[0]
        decimal = splits[1]
    else:
        whole = splits[0]
        decimal = ""

    newWhole = ""
    for i in range(0, len(whole), 3):
        prefixesIndex = i//3
        prefix = prefixes[prefixesIndex]
        vowel = convertMilliadints(whole[-3:])
        whole = whole[:-3]
        if vowel != "":
            newWhole = prefix + vowel + newWhole
       
    newDecimal = ""
    for i in range(0, len(decimal), 3):
        prefixesIndex = i//3
        prefix = prefixes[prefixesIndex]
        vowel = convertMilliadpartials(decimal[:3])
        decimal = decimal[3:]
        if vowel != "":
            newDecimal = newDecimal + prefix + vowel

    return newWhole + newDecimal


print(convertToNew(0.000045))
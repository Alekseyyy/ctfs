# By Aleksey
# NOTE: that this only got partial credit :P

def isMAC48Address(inputString):
    x = inputString.split("-")
    if len(x) != 6:
        return False
    for k in x:
        for w in k:
            if w not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                return False
            
    return True

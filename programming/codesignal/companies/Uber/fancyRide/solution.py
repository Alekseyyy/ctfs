# CodeSignal Company Challenges
#
# A solution to Uber's "fancyRide" challenge
# By Aleksey
#

def fancyRide(l, fares):
    winner = None
    for x, y in zip([l * fare for fare in fares], ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]):
        if x > 20:
            return winner
        else:
            winner = y
    return winner

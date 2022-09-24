# Read Plant xml                    project 1
#
#
# import tools
import xml.etree.ElementTree as ET
tree = ET.parse('plant_catalog.xml')


# define components
root = tree.getroot()               # returns catalog
global eTargetSF
eTargetSF = 'PLANT'


# save common name and price into array (list)
unitMax = len(root.findall(eTargetSF))
noList = range(0, unitMax, 1)       # returns 36

plantNames = ['']                   # empty string
plantLight = ['']                   # empty string
plantPrice = [0]                    # empty integer
dotsLand = ['']


# fill out empty plantNames and plantPrice
# this creates two lists full unitMax size but empty
for listfill in noList:
    listfill = [0]
    plantPrice = plantPrice + listfill
    listfill = ['']
    plantNames = plantNames + listfill
    plantLight = plantLight + listfill
    dotsLand = dotsLand + listfill   

# parse through xml and fill new arrays (lists)
for pegs in noList:
    plantNames[pegs] = root[pegs][0].text
    plantLight[pegs] = root[pegs][3].text
    plantPrice[pegs] = root[pegs][4].text

    # calculate spacing for string
    stringLength = len(plantNames[pegs])        # within for loop so will do for each
    stringMax = 19 + 8                          # longest namae is 19 long plus a some extra
    stringSpaceExtra = stringMax - stringLength

    # add dots
    for newDot in range(0, stringSpaceExtra, 1):
        newDot = '.'
        dotsLand[pegs] = dotsLand[pegs]+newDot


# accurate function
""" 
def plantno( j ):
    if j < unitMax:
     print(plantNames[j]+dotsLand[j]+plantPrice[j])


# test function
print('')
fullRange = range(0, unitMax, 1)
for slots in fullRange:
 plantno(slots)
""" 
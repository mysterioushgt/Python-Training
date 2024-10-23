stationlist=("Gwalior","Jhansi","Bina","Bidisha","Bhopal","Habibganj")
targetlist=list(stationlist) #converting tuple into list
print(targetlist)
targetlist.pop(2)
targetlist.append("Rani Kamlapati")
# targetlist.insert(2,"Rani Kamlapati")
stationlist=tuple(targetlist) # converting the modified list into tuple
print(stationlist)
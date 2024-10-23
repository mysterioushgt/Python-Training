name ="saloni"
print(name.center(10,"*"))


str="my name is saloni  and my age is 21"
# print(str.replace("is","was",1))
is_pos1=str.find("is")
# is_pos2=str.find("is",is_pos1)   #this will start from first is
is_pos2=str.find("is",is_pos1+1)
print(is_pos2)

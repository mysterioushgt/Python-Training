# CIRCUIT ID ENCRYPTION

circuitid="LON/LON/LE-123456"
parts=circuitid.split("/")
newcircuitid=parts[2]
newcircuitid =newcircuitid[:2]+"XXX-"+newcircuitid.split("-") [1]
print(newcircuitid)
print("Encrypted ID = " ,parts[0]+"/"+parts[1]+"/"+newcircuitid)
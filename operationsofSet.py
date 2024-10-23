pricorus={"Sales","IT","CSO","FSO","LDM"}
symphony={"Sales","CSO","Purchase","HR","Admin"}

#symphony has produced pricorus
newdepts =pricorus-symphony # finding the difference
print("New Depts to be formed")
print(newdepts)
print("Total new Deptd = %d" %(len(newdepts)))

cdept =pricorus & symphony  # & stands for intersection
print("Common depts to be formed")
print(cdept)
print("total common depts = %d" %len(cdept))

#How To Conbine both these Sets -- Union Process
overalldept = pricorus | symphony
print("overall depts to be formed")
print(overalldept)
print("total common Depts = %d" %len(overalldept))
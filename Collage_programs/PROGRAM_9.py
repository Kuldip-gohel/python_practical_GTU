#genrate to empty dictnory

student={}

#add value of dictnory

student["name"]="Himanshu"
student['age']=20
student['gender']="male"

#print dictnory
print(student)

#specific key
print(student["name"])
#if value not found to given defualt value
print(student.get("car","unknown"))

#sort content of dictnory
print(sorted(student))

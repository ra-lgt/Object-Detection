import pyttsx3  as py

files=open("demo.txt","r")
list1=[]
list2=[]
# getting strings from files
for i in files:
    list1.append(i)
print(list1)

#splitting string by ,
for j in list1:
    list2+=j.split(",")
print(list2)

length=len(list2)

start=py.init()

for k in range (length):
    start.say(list2[k])
    start.runAndWait()

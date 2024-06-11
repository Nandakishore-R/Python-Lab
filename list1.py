names = ['Nandu','KJ',"Geena",'Jithin',"Sajith"]

if "Nandu" in names:
    print("Name is in the list")
else :
    print("Name is not in the list")

for n in names:
    print(n)

print()

names.sort()
# for n in names:
#     print(n)
i=0
while i<len(names):
    print(names[i])
    i+=1

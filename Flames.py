# Flames calculator
def flames_trick(flames,total_count):
    count=0
    while(count<=total_count):
        if(count==total_count):
            i=(count%len(flames))-1
            if(i==-1):
                i=len(flames)-1
            flames.remove(flames[i])
            break
        count+=1
    flames=flames[i:]+flames[:i]
    return flames
list1=list(input("Enter the 1st name: ").lower().replace(" ",""))
list2=list(input("Enter the 2nd name: ").lower().replace(" ",""))
flames=['F','L','A','M','E','S']
dictionary={'F':'Friends','L':'Lovers','A':'Affection','M':'Marriage','E':'Enemies','S':'Siblings'}
for i in list1:
    if i in list2:
        list2.remove(i)
        list1.remove(i)
for i in list2:
    if i in list1:
        list1.remove(i)
        list2.remove(i)
print(list1,list2)
total_count=len(list1)+len(list2)
print(total_count)
flames1=list(flames)
while(len(flames1)>1):
    flames1=flames_trick(flames1,total_count)
key="".join(flames1)
print(flames)
print(dictionary[key])

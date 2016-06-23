#Enter without values to finish adding values to search.
VTS=[]
print "Enter without value to finish adding values to search.
while True:
    input = raw_input("Enter the value to add to search")
    if input != "":
        VTS.append(int(input))
    else:
        break
i=0
swap=1
print VTS
while swap >= 1:
    swap=0
    i=0
    while i < len(VTS):
        if (i+1) != len(VTS):
            if VTS[i]>VTS[i+1]:
                big=VTS[i]
                small=VTS[i+1]
                VTS[i],VTS[i+1]=small,big
                print VTS
                swap=swap+1
        i=i+1
    print "Total Number of Swaps"+str(swap)
print "Final Sorted List"
print VTS

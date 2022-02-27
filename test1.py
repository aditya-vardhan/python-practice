name=raw_input('enter values: ') # "5 2 9 4 5 12"
arr=name.split(' ') #["5","2","9","4","3"] 
arr = map(int, arr)
arr.sort() #["2","3","4","5","9"] 
print arr
arrLength=len(arr) #specifies length of the above array
reminder=arrLength%2 #gives division reminder for eg: 8%2 which is 0
if(reminder==0): #check if reminder is 0 which means array is even
    middleValue1Position=arrLength/2 -1 # it gives 2
    middleValue2Position=arrLength/2 # it gives 3
    middleVal1 = arr[middleValue1Position] # it gives "9"
    middleVal2 = arr[middleValue2Position] # it gives "4"
    # middleVal1Number= int(middleVal1)  # this will convert "9" to 9
    # middleVal2Number= int(middleVal2)  # this will convert string to number
    output=middleVal1+middleVal2 # this will do 9+4
    print output
else:
    middleValPosition=arrLength/2
    middleVal=arr[middleValPosition]
    # middleValNumber= int(middleValPosition)
    print middleVal



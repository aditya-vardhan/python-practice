# calculate number of special characters in user provided command line string excluding spaces
name=raw_input('enter special character string: ') # hsdf#sdfl sdf@ 123 sdfj
specialCharacters=0
stringLength=len(name) # it gives total length of user provided string
for indexPosition in range(0, stringLength):
    currentIndexValue = name[indexPosition]
    if currentIndexValue.isalpha():
        continue
    elif currentIndexValue.isdigit():
        continue
    #elif currentIndexValue == ' ':
        #continue
    else:
        specialCharacters += 1
print specialCharacters


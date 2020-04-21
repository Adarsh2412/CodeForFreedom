units=int(input("Enter number of units: "))
total=0.0
if units<=50:
    total=units*0.50
elif units<=150:
    total=25+(units-50)*0.75
elif units<=250:
    total=25+75+(units-150)*1.2
elif units>250:
    total=25+75+120+(units-250)*1.5
else:
    print("Invalid Input")
total+=(20*total/100)
print("Total Elictricity Bill is: "+str(total))
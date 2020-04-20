# Take input of size of list and the correct order of strings 
num=int(input("Enter size of list: "))
print("Enter the required list order")
list_number=list(range(0,num))
for i in range(0,num):
    list_number[i]=int(input("Enter order: "))

#Take input of strings
string_list=list(range(0,num))
print("Enter the Strings that need to be ordered")
for i in range(0,num):
    string_list[i]=input("Enter string number "+str(i+1)+" : ")

#Bring String to correct order
string2_list=list(range(0,num))
for i in range(0,num):
    string2_list[list_number[i]-1]=string_list[i]

# Make necassary changes to each string as directed by the requirements
for i in range(0,num):
    if((i+1)==len(string2_list[i])):
        string2_list[i]=string2_list[i].upper()
    elif string2_list[i]==string_list[i]:
        continue
    else:
        string2_list[i]=string2_list[i].lower()

#Print the final String in ordered format
print("String in ordered format is: ")
for i in string2_list:
    print(i)

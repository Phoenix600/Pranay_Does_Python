# Taking data from the user 
int_no_of_persons = int(input("[+]Enter the number of emails you want to add : "))

# consider empty list, becomes easy to add elements using append() method
list_person_name = []

list_email = []
for COUNT in range(0,int_no_of_persons):
    list_person_name.append(input(f"[+]Enter the name of person {COUNT+1} : "))
    

# persons_identity = input("Is Following list if for students[0] / Professor[1] : ")
persons_identity = int(input("Is Following list if for students[0] / Professor[1] : "))
# list_person_name = list_email
list_email  = list_person_name

# if persons_identity == "Professor" or persons_identity == "professor" :
if persons_identity == 1 :
    # print('@prof.college.edu'.join(list_email),sep="\n")
    for INDEX in range(0,len(list_email)) :
        list_email[INDEX] = list_email[INDEX] + "@prof.college.edu "
else :
    # print('@student.college.edu'.join(list_email),sep="\n")
    for INDEX in range(0,len(list_email)) :
        list_email[INDEX] = list_email[INDEX] + "@student.college.edu "

print(list_email)

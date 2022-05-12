# All Essential Variables are declared here 
# empty list 
List_sample = []
# keeping the track of indexing 
int_index = int(0)

int_index = int(input("[+]Enter the number of lines you want to pass : "))

for COUNT in range(0,int_index) :
    List_sample.append(input())


for INDEX in range(0,int_index) :
    print(List_sample[INDEX].upper(),end="\n")

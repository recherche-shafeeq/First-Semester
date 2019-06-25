## IMPORTS GO HERE
import os
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###
def split_safe(s):
    ind = 0
    lst = ['']
    boolee = 0
    boole = 0

    for ch in s:
        if ch == ',' and boolee == 0:
            lst.append('')
            ind += 1
            boole  = 1

        elif ch == "'" and boolee == 0:
            boolee = 1

        elif ch == "'" and boolee == 1:
            boolee = 0

        elif ch == " " and boole ==0:
            lst[ind] = lst[ind] + ch

        elif ch !=' ':
            lst[ind] = lst[ind] + ch
            boole = 0

    return lst
#### End OF MARKER



### YOUR CODE FOR read_data() FUNCTION GOES HERE ###
def read_data(directory,filename):
    new_lst = []
    file = os.path.join(directory,filename)
    with open(file, "r") as f:
        for line in f:
            a=split_safe(line.strip())
            new_lst.append(a)
    return new_lst
#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass







 

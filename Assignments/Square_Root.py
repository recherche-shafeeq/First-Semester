## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR good_enough() FUNCTION GOES HERE ####
def good_enough(n,g):

    if abs((g*g)-n)<0.00001:

        return True

    else:

        return False
#### End OF MARKER


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(n,g=0.1,m=0):
	m=m+1

	if good_enough(n,g):

		print("Took:",m,"steps")
		j=round(g,9)
		return (j)
	else:

		better_guess=improve_guess(n,g)

		return sqrt(n,better_guess,m)

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(n,g):
	a=abs((g**2-n)/(2*g))
	b=abs(g-a)
	return (b)
#### End OF MARKER




if __name__ == '__main__':
    print(sqrt(36))
Server time: Tue, 25 Jun 2019 17:27:24 +05

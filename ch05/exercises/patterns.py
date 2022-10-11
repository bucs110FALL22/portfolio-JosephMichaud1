#Part 1
def star_pyamid(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
numOfRows = int(input("How many rows would you like?: "))
star_pyamid(numOfRows)
#Part 2
def rstar_pyamid(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
numOfRows = int(input("How many rows would you like?: "))
rstar_pyamid(numOfRows)



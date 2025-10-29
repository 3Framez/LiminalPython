#Lists -a collection of multiple elements. Unlike strings, They are mutable (can be changed)


myList = [3,2,4,1,5]
print(myList.index(4)) #locating the index position of a specific element
countList = myList.count(3) #number of times a specific elements occurs
print(countList) #count() returns a value, which should be captured

myList.reverse() #reverses the given order of the list
print(myList)
myList.sort() #sortd the list in order
print(myList)

# pop() returns a value so it can be captured
popped = myList.pop() #removes the last element in the list and changes the contents of the list
print(myList) #updated list
print(popped) #popped value has been captured

myList[0] = 'S' #first element at the oth index position changed
print(myList)

myList[1] = ['hello', 'bye'] #list within a list
print(myList)

#append function adds a single element to the last index position, but it returns no value, so unlike pop(), it cant be captured
myList.append("hi")
print(myList)

#slicing lists
print(myList[1][0:2])  #[identify  the 1st index position][start a 0th position: give me two elements]

listLength = len(myList)
print(listLength) #length of entire list

#merging two lists together
list1 = [1,2,3,4,5,6]
list2 = ["b","d","a","z","x"]
newList = list1 + list2
print(newList)

"""
from the 2 lists above get the result: ['d','b','a',3,2,1]
"""
list1.reverse()
list2.sort()
list2.reverse()
print(list2 + list1)
# combinedList = list2 + list1
print(list2[2:5]+list1[-3:]) #start slicing from the 2nd position : include elements up to the 5th one] + [start slicing from the 3rd last element : give me the remaing elements]



list1 = [1,2,3,4,5,6]
print(list1[2:5]) #start slicing from the second index position: and give me 5 elements starting from the beginning of the list
# to get [3,4,5]
# why doesnt this work



# Insertion sort in Python
def insertionSort(array,n):
    booksRead = 0
    for step in range(1, n):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            booksRead+=1
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return booksRead,array



n = int(input())
original = list(input())
booksRead,organized = insertionSort(original.copy(),n)
answer = True

for i in range(n):
    moved = i-organized.index(original[i])
    if moved < -5:
        print("A Database Systems Student read a book.")
        answer = False
        break

if (answer):
    print(booksRead)

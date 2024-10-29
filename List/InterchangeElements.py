'''
Program to interchange first and last elements in a list
'''
def Interchange(list, a, b):
    list[a], list[b] = list[b], list[a]

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    index1 = int(input("Enter the index of the first element: "))
    index2 = int(input("Enter the index of the second element: "))
    if index1 > len(List)-1 or index1<-len(List) or index2<-len(List) or index2 > len(List)-1:
        print("Index out of range\nPlease Try Again")
        continue
    break

Interchange(List, index1, index2)
print(List)

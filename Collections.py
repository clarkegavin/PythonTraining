# List: Ordered, changeable and allow duplicates
# Tuple: Ordered and unchangeable
# Set: Unordered and unchangeable and unindexed
# Dictionary: Ordered and changeable

def main():
    print("---------Lists--------")
    firstList = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
    print(firstList)
    print(len(firstList))
    print(type(firstList))
    print(firstList[-2]) # negative indexing, means index starting from the end where -1 is the last item
    print(firstList[2:4]) # range of indexes
    firstList[1:3] = ["blackberry", "plum"]
    print(firstList)
    firstList[1:4] = ["blackcurrent", "gooseberry"]
    print(firstList)
    firstList[1:2] = ["watermelon", "tomato"]
    print(firstList)
    firstList.insert(2, "strawberry")
    print(firstList)
    firstList.append("redberry")
    print(firstList)
    tropical = ["mango", "pineapple", "papaya"]
    firstList.extend(tropical)
    print(firstList)
    
main()

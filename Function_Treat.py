data=[]

def inputData():
    size=int(input("Enter Size Of Array:\n"))
    for i in range(size):
        items=int(input("Enter Data For 1D Array(Seperated By Spaces): "))
        data.append(items)
        print("\nData Has Been Stored Successfully\n")
        
def displayData():
    if len(data)==0:
        print("Please Enter Data First\n")
        return
    print("Data Summary:\n")
    
    totalValue()
    min()
    max()
    sum_data()
    avg()

def totalValue():
    j=0
    for i in data:
        j+=1
    print(f"Total Elements: {j}\n")
    return j

def min():
    min_val = data[0]
    for i in data:
        if i < min_val:
            min_val = i
    print(f"Minimum Value: {min_val}\n")
    return min_val

def max():
    max_val = data[0]
    for i in data:
        if i > max_val:
            max_val = i
    print(f"Maximum Value: {max_val}\n")
    return max_val

def sum_data():
    total = 0
    for i in data:
        total += i
    print(f"-Sum Of All Elements: {total}\n")
    return total

def avg():
    total = 0
    for i in data:
        total += i
    average = total / len(data)
    print(f"-Average Of All Elements: {average}\n")
    return average

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

def sortData():
    if len(data) == 0:
        print("Please Enter Data First\n")
        return
        
    print("\nChoose Sorting Option:")
    print("1. Ascending Order")                          
    print("2. Descending Order\n")
    
    sortChoice=int(input("Enter Your Choice:\n"))
    if sortChoice==1:
        data.sort()
        print("\nSorted Data In Ascending Order:\n")
        print(*data, sep=", ")
        
    elif sortChoice==2:
        data.sort(reverse=True)
        print("\nSorted Data In Descending Order:\n")
        print(*data, sep=", ")

def statistics():
    if len(data) == 0:
        return None, None, None, None
        
    minimum = data[0]
    maximum = data[0]
    total = 0
    count = 0
    
    for i in data:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
        total += i
        count += 1
        
    average = total / count
    return minimum, maximum, total, average

def filterData():
    if len(data) == 0:
        print("Please Enter Data First\n")
        return
    threshold = int(input("Enter Threshold Value To Filter Out Data Above: "))
    filteredData = list(filter(lambda x: x <= threshold, data))
    print(f"\nFiltered Data (Values <= {threshold}):\n")
    print(*filteredData, sep=", ")

while True:
    print("Welcome To Data Analyzer And Transformer Program\n")
    
    print("1. Input Data")
    print("2. Display Data Summary(Built-In Functions) ")
    print("3. Calculate Factorial(Calculate Functions) ")
    print("4. Filter Data By Threshold (Lambda Functions) ")
    print("5. Sort Data ")
    print("6. Display Dataset Statistics (Return Multiple Data) ")
    print("7. Exit\n")
    
    choice=int(input("Enter Your Choice:\n"))
    
    match choice:
        
        case 1:
            inputData()
        
        case 2:
            displayData()
        
        case 3:
            num=int(input("Enter Number To Calculate Factorial: "))
            result=fact(num)
            print(f"Factorial Of {num} Is: {result}\n")
        
        case 4:
            filterData()
        
        case 5:
            sortData()
        
        case 6:
            minimum, maximum, total, average = statistics()
            if minimum is not None:
                print(f"Minimum Value: {minimum}")
                print(f"Maximum Value: {maximum}")
                print(f"Sum Of All Values: {total}")
                print(f"Average Value: {average}\n")
            else:
                print("Please Enter Data First\n")
        
        case 7:
            print("\n Thank You For Using Data Analyzer And Transformer Program!")
            break
        
        case _:
            print("\n Invalid Choice! Please Try Again.\n")
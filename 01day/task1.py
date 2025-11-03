arr = []
length = int(input("Enter your valuse length: "))
for i in range(length):
        data = int(input("Enter value"))
        arr.append(data)
def maxnum():
    maxval = arr[0] 
    for i in range(len(arr)):
        
        if maxval < arr[i]:
            maxval = arr[i]
    print("Maximum Value is ",maxval)
maxnum()
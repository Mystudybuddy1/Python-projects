# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] < pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1


# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)

#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)


# mylist = []

# i = 0

# while i < 6:
#     x = int(input("Enter your marks: "))
#     mylist.append(x)
#     i += 1

# print("Before sorting:", mylist)

# quicksort(mylist)

# print("After sorting:", mylist)


#----------------------------------------------------

weights = []

n = int(input("How many packages?: "))

for i in range(n):
    weight = float(input("Enter package weight: "))
    weights.append(weight)

for i in range(n):
    for j in range(n - i - 1):
        if weights[j] > weights[j + 1]:
            weights[j], weights[j + 1] = weights[j + 1], weights[j]

print(weights)


#------------------------------------------------------

prices = []

n = int(input("How many products: "))

for i in range(n):
    price = int(input("Enter price: "))
    prices.append(price)

n = len(prices)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if prices[j] < prices[min_index]:
            min_index = j

    prices[i], prices[min_index] = prices[min_index], prices[i]

print(prices)  
# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    if a > b:
        return a
    elif b> c:
        return b
    else:
        return c

print(max_num(15,25,35))

def max_num(a,b,c):
    return max(a,b,c)

print(max_num(15,25,35))


# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(num):
    if len(num) == 0:
        return 0
    product = num[0]
    if len(num) > 1:
        for i in (num[1:]):
            product = product * i
        return product
      
print(mult_list([5,2,3]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    # return s[::-1]
  for i in range(len(s)-1, -1, -1):
    print(s[i])
(rev_string('abcdefghijk'))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(n, start_num, end_num):
    return start_num <= n <= end_num if end_num >= start_num else end_num <= n <= start_num
    # return n in range(start_num, end_num+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))






# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.+


def pascals(numRows):
    t = []
    for i in range(numRows):
        t.append([])
        t[i].append(1)
        for j in range(1,i):
            t[i].append(t[i-1][j-1]+t[i-1][j])
        if i != 0:        
            t[i].append(1)
    return t
print(pascals(5))


# def printTriangle(t):
#     printString = ""
#     for i in range(0,len(t)):
#         printString = " " * (len(t) - i)
#         for j in range(0,len(t[i])):
#             printString = printString + str(t[i][j]) + " "
#         print(printString)
# printTriangle(pascals(5))







import statistics

# Add IQR, UQ, LQ 
# Creating an ordered number line from a given number list
ord_list = []

rang = int(input("How many numbers are in your list? ")) # sets the range and therefore the amount of repetitions asking for a new number

for i in range(rang): # rang is the number of integers you want to sort
    number = float(input("Please enter a number: "))
    ord_list.append(number)
    ord_list.sort()
print(ord_list)

def mean(ord_list):
    mean = sum(ord_list) / len(ord_list)
    meanstr = str(mean)
    return mean
    
def median(ord_list):
    med = statistics.median(ord_list)
    medstr = str(med)
    print("The median is: " + medstr)

def difference(ord_list):
    rng = ord_list[-1] - ord_list[0]
    rngstr = str(rng)
    print("The range is: " + rngstr)

"""def percent1(ord_list):  # Consider using numPy?
    ord_list.quartile"""    # Could try and make it work for an odd data set

def mode(ord_list):
    mod = statistics.mode(ord_list) #Throws error if number of modes > 1. Needs fixing (Could use 'try' and 'except')
    modstr = str(mod)
    if mod != int():
        print("No Mode")

def variance(ord_list):
    average = float(mean(ord_list))
    print("The mean is: " + str(average))
    num_no_sigma_squared = 0
    squared_total = 0
    xixbar = []
    xixbar_squared = []
    sigma = sum(ord_list)
    denominator = len(ord_list) - 1
    for i in ord_list:
        num_no_sigma = (i - average) # (xi - xbar)
        xixbar.append(num_no_sigma)
        num_no_sigma_squared = num_no_sigma_squared + num_no_sigma
    for n in xixbar:
        num_squared = n ** 2
        xixbar_squared.append(num_squared)
    for x in xixbar_squared:
        squared_total += x
    numerator = squared_total
    var = numerator / denominator
    print("The variance is " + str(var))
    return var

def standard_deviation():
    sqrt = variance(ord_list)**(0.5)
    print("The standard deviation is: " + str(sqrt))
"""
def gcd(ord_list): # Will only find the GCD of 2 numbers
    primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    greatest_common_devisor = 0
    AA = 0
    A = ord_list[0]
    B = ord_list[1]
    def prime(A, B):
        while AA // y != 1 or AA // y != AA:
            notprime = True
        else:
            notprime = False
    if len(ord_list) > 2:
        print("Cannot commpute greatest common devisor (Too many numbers)")
    if A == 0:
        greatest_common_devisor = B
    if B == 0:
        greatest_common_devisor = A
    while notprime == True:
        for y in primelist:
            if A > y:
                bisect_left(primelist, y)
            if B > y:
                bisect_left(primelist, y)"""
            
def r_m_m(ord_list):
    mean(ord_list)
    median(ord_list)
    difference(ord_list)
    if len(set(ord_list)) != len(ord_list):
        mode(ord_list)
    else:
        print("There is no mode")    
    variance(ord_list)
    standard_deviation()
    
r_m_m(ord_list)
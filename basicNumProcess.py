import statistics

# Add Standard Deviation
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
    print("The mean is: " + meanstr)
    return mean

def median(ord_list):
    med = statistics.median(ord_list)
    medstr = str(med)
    print("The median is: " + medstr)

def range(ord_list):
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
    print("The average is: " + str(average))
    numx = 0
    sigma = sum(ord_list)
    print("Sigma is: " + str(sigma))
    denominator = len(ord_list) - 1
    print("Denominator is: " + str(denominator))
    for i in ord_list:
        numz = i - average
        print("Numz: " + str(i) + " - " + str(average))
        numx += numz
        print("Numx: " + str(numx))
    numerator = sigma * numx
    print("Numerator is: " + str(numerator))
    var = numerator / denominator
    print("The varience is " + str(var))
    return var

#def standard_deviation():
         
def r_m_m(ord_list):
    mean(ord_list)
    median(ord_list)
    range(ord_list)
    if len(set(ord_list)) != len(ord_list):
        mode(ord_list)
    else:
        print("There is no mode")    
    variance(ord_list)
    
r_m_m(ord_list)
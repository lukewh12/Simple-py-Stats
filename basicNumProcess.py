import statistics

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
    mod = statistics.mode(ord_list) #Throws error if number of modes > 1. Needs fixing
    modstr = str(mod)
    print("The mode is: " + modstr)

def r_m_m(ord_list):
    mean(ord_list)
    median(ord_list)
    range(ord_list)
    mode(ord_list)

r_m_m(ord_list)

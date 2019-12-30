import statistics as st

x_list = []
y_list = []

rang = int(input("How many coordinates are in your list? ")) # sets the range and therefore the amount of repetitions asking for a new number

for i in range(rang): # rang is the number of integers you want to sort
    x_coord = float(input("Please enter x: "))
    y_coord = float(input("Please enter y: "))
    x_list.append(x_coord)
    y_list.append(y_coord)
    mean_x = st.mean(x_list)
    mean_y = st.mean(y_list)

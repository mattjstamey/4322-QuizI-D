'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
emp_file = open('employee_data.csv')
emp_reader = csv.reader(emp_file, delimiter = ',')
next(emp_reader)

#create an empty dictionary
emp_dict = {}

#use a loop to iterate through the csv file

for i in emp_reader:
    #check if the employee fits the search criteria
    if i[4] == 'CSR' and i[3] == 'Marketing':
        print(f"Manager Name: {i[1]} {i[2]} Current Salary: ${int(i[5]):,.2f}")
        emp_dict[f"{i[1]} {i[2]}"] = round(int(i[5])*1.1,2)


    



print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for i in emp_dict:
    print(f"Manager Name: {i} New salary: ${int(emp_dict[i]):,.2f}")

        

        
    

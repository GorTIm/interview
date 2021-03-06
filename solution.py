#Solution to the interview problem

"""
Problem 1
In a Fibonacci sequence, each new term is generated by adding the previous two terms. By starting with 0 and 1, 
the first 10 terms will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …

Create a program that accepts a parameterized value for the max Fibonacci value. 
The program should finds the terms in the Fibonacci sequence whose values do not exceed 
the parameterized value and then provides the sum of the odd-valued terms. 
For example, for a parameterized value of 22, the Fibonacci sequence
would be 0, 1, 1, 2, 3, 5, 8, 13, 21 and the sum of the odd-values would
be: 44

"""
def findOddValuesInFib(p_value):
    p_value=int(p_value)
    if p_value<0:
        return -1
    pre=0
    next=1
    count=0
    while next<=p_value:
        if next%2==1:
            count+=next
        temp=next
        next+=pre
        pre=temp
    return count



"""
Problem 2
This link is to a CSV (Comma Separated values) file which contains people's first name, last name, 
address and province. All of the values are separated by commas. Please open the CSV file in a separate browser 
tab/window. You can then download the file by selecting File -> Download -> Comma-Separated values.

Please create a program to process the CSV file and only output the
residents of Ontario.

HINT: You should use a library to read and handle the CSV file rather than creating your own functions for parsing the file.

"""


import pandas as pd
def selectRow(s):
    s='Ontario'
    dataset=pd.read_csv('address - address.csv')
    condition=dataset.Province==s

    result=dataset[condition]

    return result
        




if  __name__=="__main__":
    ip=input("Enter your input value:")
    print(findOddValuesInFib(ip))
    print(selectRow("a"))


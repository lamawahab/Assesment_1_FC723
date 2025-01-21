#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:00:53 2025

@author: lamaalabdulwahab
"""

#function to calculate the greatest common dividor
def GCD(a,b):
    #if one of the numbers is zero then the GCD is the other number
    if a==0: #if a is zero the result is b
        result=b
    elif b==0:#if b is zero the result is a 
        result=a
    else:#if none of them is zero then it goes into the algorithm
        while a!=0 and b!=0: #the algorithm continues until one of the two numbers is zero
        #locate which is the higher number and which is lower
            if a>b:#if a is bigger then b is lower
                big=a
                small=b
            else:#if b is higher then a is lower
                big=b
                small=a
            reminder=big%small #find the reminder by using modulo
            #assign new values to a and b to repeat proccess untill one of the values is zero
            a=small 
            b=reminder
            #CHECK AGAIN: if one of the numbers is zero then the GCD is the other number
            if a==0:#if a is zero the result is b
                result=b
            elif b==0:#if b is zero the result is a 
                result=a
    return result#return the GCD

#a function that checks whether the number is a float or not
def Is_float(num):
    return num % 1 != 0

#a function that takes user input and check whether it is valid or not
def User_input():
    print("Please enter two positive integers to continue: ")
    num1 = float(input("Enter the first number: "))#use float() function to change it from string and be able to operate on it 
    num2 = float(input("Enter the second number: "))
    
    #check the validity of the inputs, if they are wrong asks user to input again until correct
    # the euclidean algorithm does not work if both numbers are zero or if one or both numbers is a float or if one or both numbers is negative
    while (num1==0 and num2==0) or (num1<0 or num2<0) or (Is_float(num1)) or (Is_float(num2)):
        print("Your input is invalid please try again, enter two positive integers to continue")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
    result = GCD(num1,num2)#after ensuring validity, call the GCD function for the two numbers
    print(f"the greatest common dividor of {num1} and {num2} is {result} ")#print result
    

User_input()#call function to start program



    
                                            
                
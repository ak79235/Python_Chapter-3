# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:16:16 2020

@author: ak792
"""
# Write a program to perform addition, subtraction, multipliocation, division,
# integer division, and modulo division on two integer numbers.
print("Program to perform addition, subtraction, multiplication, division,integer division, and modulo division on two integer numbers.\n\n\n")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
integer_division = num1 // num2
modulo_division = num1 % num2
print("Addition of " + str(num1) + " and " + str(num2) + " = " + str(addition))
print("Subtraction of " + str(num1) + " and " + str(num2) + " = " + str(subtraction))
print("Multiplication of " + str(num1) + " and " + str(num2) + " = " + str(multiplication))
print("Division of " + str(num1) + " and " + str(num2) + " = " + str(division))
print("Integer Division of " + str(num1) + " and " + str(num2) + " = " + str(integer_division))
print("Modulo Division of " + str(num1) + " and " + str(num2) + " = " + str(modulo_division))
input()
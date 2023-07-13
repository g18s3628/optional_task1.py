#Request user to input lengths of all three sides of a triangle 
side1 = float(input("Enter length of side 1 of triangle:"))
side2 = float(input("Enter length of side 2 of triangle:"))
side3 = float(input("Enter length of side 3 of triangle:"))

#Import the maths library 
import math

#Summation of all the sides and divide by two and name it name variable 
s = (side1 + side2 + side3)/2
#Calculate the area of the triangle 
area = math.sqrt((s * (s - side1)*(s - side2)*(s - side3)))
print("The area of the triangle is:", area) #Print out the area of triangle 

# Team Members: Will Giebel
# Course: CS151, Prof. Mehri
# Date: 9/27/21
# Programming Assignment: 1
# Program Inputs: [Length, Width, Height]
# Program Outputs: [Area of the Room, gallons of primer and paint]
l= float(input("Enter value for Length of room: "))
h = float(input("Enter value for Height of room: "))
w = float(input("Enter value for width of room: "))
volume= l*w*h

print("Volume of Room: ",volume, "ft².")

p= volume/200.0
print("Amount of primer needed to paint room :", p, "gallons")

pa = volume/350.0
print("Amount of paint needed to paint room :",pa, "gallons")


import math#these import the dependancies to understand what I want
import time
import sys

typesofproducts = int(input("How many different products are you moving? "))#asks how many products you move so it can loop a certain amount of times
productlist = []#makes a list so we can save each product as a sepearate variable
for i in range(typesofproducts):
    name = input(f"What is the name of the product number {i+1}? ") #asks the name of each product then it loops and asks the question differently depending on the loop number
    num = float(input(f"How much does one {name} weigh in g? "))#asks for the mass of one product
    num2 = float(input(f"How many {name}s are there of that type? "))#asks how many products there are
    num3 = float(input(f"How far has the {name} gone in miles? "))#asks how far it has gone in miles
    num = math.ceil(num)
    num2 = math.ceil(num2)
    num3 = math.ceil(num3)#these round the numbers
    endnum = num * num2 * num3 #this multiplies them together
    endnum = (endnum / 80)#this estimates the carbon output
    productlist.append([name, endnum])
    i = i + 1
print("\n")
for i in productlist:
    print("product name:", i[0],
          "approximate carbon dioxide output in grammes is :", i[1])
print("\n")
print("Good tips to lower carbon dioxide output while driving an automobile aka car aka lorry aka motor car aka car with a internal combustion engine aka a driving ting:")
time.sleep(3)
print("1. Don't Drive Lots")
time.sleep(3)
print("2.Use a electric vehicle if possible")
time.sleep(3)
print(
    "3.Carry less in your car. Thour own birth giver possesseth a quiteth significant amounteth of weight withinith her owneth body, for one sucheth example"
)
time.sleep(3)
print("\n")
sys.exit("Done")

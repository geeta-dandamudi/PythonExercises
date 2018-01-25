input1 = raw_input("enter price of item1")
quantity1 = raw_input("enter quantity of item1")
input2 = raw_input("enter price of item2")
quantity2 = raw_input("enter quantity of item2")
input3 = raw_input("enter price of item3")
quantity3 = raw_input("enter quantity of item3")
subtotal = int(input1)*int(quantity1) + int(input2)*int(quantity2) + int(input3)*int(quantity3)
tax = subtotal * 0.055 #when tax is 5.5%
total = subtotal + tax
print "The subtotal is %d\n tax is %.2f \n and total is %.2f" %(subtotal, tax, total)
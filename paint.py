import math
l = raw_input("enter length")
w = raw_input("enetr width")
area = int(l) * int(w)
paint_required = int(math.ceil(area / float(350))) # Assuming that 1 gallon of paint covers 350 sq ft and only a full gallon paint can be purchased.
print "%d gallons of paint is required to paint %d area " %(paint_required, area)
open_file = open("CupcakeInvoices.csv")

total_chocolate = 0
total_strawberry = 0
total_vanilla = 0

for flavor in open_file:  
    flavor = flavor.strip()
    flavors = flavor.split(',')
    print(flavors)
    for taste in flavors: 
        if taste == "Chocolate":
            total_chocolate += 1
        elif taste == "Vanilla":
            total_vanilla += 1
        elif taste == "Strawberry": 
            total_strawberry += 1    

print ("Chocolate:", total_chocolate)
print ("Strawberry:", total_strawberry)
print ("Vanilla:", total_vanilla)


open_file.close()

# # Loop through all the data and print out the 
# total for each invoice (Note: this data is not 
# provided by the csv, you will need to calculate it. 
# Also, keep in mind the data from the csv comes back as a string, you
#  will need to convert it to a float. Research how to do this.).

data = open("CupcakeInvoices.csv")
for row in data:
  values = row.split(',')
  total = int(values[3]) * float(values[4])
  print(total)



for row in data:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)

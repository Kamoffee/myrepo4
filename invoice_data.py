# Read data from "invoice_data.txt", split each line, format the output, and calculate total price
with open("invoice_data.txt", "r") as file:
    tpl = [f"{number[0]:15}{int(number[1]):3d}{float(number[2]):7.2f}{(int(number[1]) * float(number[2])):8.2f}" for line in file for number in [line.split()]]

# Print the formatted output
for item in tpl:
    print(item)


# # Initialize an empty list to store tuples
# invoice_data = []

# # Read the file line by line and create tuples
# with open("invoice_data.txt", "r") as file:
#     for line in file:
#         # Split each line into its components
#         item, quantity, price_per_item = line.split()
        
#         # Convert quantity to an integer and price_per_item to a float
#         quantity = int(quantity)
#         price_per_item = float(price_per_item)
        
#         # Create a tuple and append it to the list
#         invoice_data.append((item, quantity, price_per_item))

# # Output the data using f-string
# for item, quantity, price_per_item in invoice_data:
#     total_price = quantity * price_per_item
#     print(f"{item:<15} {quantity:3d} {price_per_item:8.2f} {total_price:9.2f}")

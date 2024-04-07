# Read the content from key.txt and get col and row values
with open("key.txt", "r") as key:
    col, row = [int(line.strip()) for line in key]

# Read characters from secret.txt and add them into a single list row by row
with open("secret.txt", "r") as secret_file:
    # Concatenate characters from each line to form a single row
    lista = [char.strip() for line in secret_file for char in line]

# Write the list into public.txt       
with open("public.txt", 'w') as new:
    # Write the concatenated characters to the file
    new.write(''.join(lista))


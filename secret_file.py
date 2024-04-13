# Read the content from key.txt and get col and row values
with open("key.txt", "r") as key:
    col, row = [int(line.strip()) for line in key]

# Read characters from secret.txt and add them into a single list row by row
with open("secret.txt", "r") as secret_file:
    secret = ''.join(char.strip() for line in secret_file for char in line)

# Split the secret into chunks of size 'col' to represent each row
chunks = [secret[i:i+col] for i in range(0, len(secret), col)]

# Write the chunks into public.txt
with open("public.txt", 'w') as new:
    for chunk in chunks:
        new.write(chunk + '\n')

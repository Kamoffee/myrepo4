import shutil
def copied_file(source_file, destination_file):
    try:
        with open(source_file, "rb") as source:
            with open(destination_file, "wb") as destination:
                destination.write(source.read())
                print(f"{source_file} was copied to {destination_file}")
    except IOError as e:
        print(f"Unable to copy file. {e}")

source_file = "numbers.txt"
destination_file = "even_numbers.txt"

copied_file(source_file, destination_file)
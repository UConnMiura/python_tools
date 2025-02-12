import sys  # Import the sys module to handle command-line arguments
import time  # Import the time module to measure execution time

# Check if the correct number of arguments is provided (gene_id and filename)
if len(sys.argv) != 3:
    print("Usage: python get_gene_name.py <gene_id> <filename>")  # Inform the user about the correct usage
    sys.exit(1)  # Exit the script with an error code if arguments are not correct

gene_id = sys.argv[1]  # The first command-line argument is the gene_id (e.g., ENSMUSG00000051951)
file = sys.argv[2]  # The second command-line argument is the file name (e.g., genes.gtf)

# Try to open and read the file. If the file doesn't exist, print an error and exit
try:
    with open(file, 'r') as f:
        lines = f.readlines()  # Read all lines of the file into a list
except FileNotFoundError:  # Handle the case where the file doesn't exist
    print(f"Error: File '{file}' not found!")
    sys.exit(1)  # Exit with an error code if the file doesn't exist

# Start measuring the time the script takes to execute
start_time = time.time()

# Loop through each line in the file
for line in lines:
    if line.startswith("##"):  # Skip lines that start with '##' (these are comments or metadata)
        continue
    
    # Split the line into columns by tab characters
    columns = line.split("\t")
    
    # The 9th column (index 8) contains the attributes (gene_id, gene_name, etc.)
    attributes = columns[8]
    
    # Check if the gene_id is present in the 9th column's attributes
    if f'gene_id "{gene_id}"' in attributes:
        # If we found the gene_id, look for gene_name within the attributes
        for item in attributes.split(";"):  # Split the attributes by ";"
            if "gene_name" in item:  # Look for the 'gene_name' attribute
                gene_name = item.split("gene_name ")[1].strip().strip('"')  # Extract the gene_name, remove quotes and extra spaces
                print(gene_name)  # Output the gene_name
                break  # Exit the loop once we've found and printed the gene_name
        break  # Exit the outer loop once the correct gene_id is found

# End time measurement after processing
end_time = time.time()

# Calculate the elapsed time (time it took to run the script)
elapsed_time = end_time - start_time

# Print the execution time in seconds
print(f"Script execution time: {elapsed_time:.2f} seconds")

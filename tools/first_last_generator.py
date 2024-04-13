def generate_usernames(firstnames_path, lastnames_path, output_path):
    # Read the first names and last names from the provided files
    with open(firstnames_path, 'r') as f:
        firstnames = f.read().splitlines()
        
    with open(lastnames_path, 'r') as f:
        lastnames = f.read().splitlines()
    
    # Open the output file where the combinations will be written
    with open(output_path, 'w') as out:
        # Iterate over every combination of first name and last name
        for firstname in firstnames:
            for lastname in lastnames:
                # Create different username formats
                formats = [
                    f"{firstname[0].lower()}.{lastname.lower()}",  # j.doe
                    f"{firstname[0].lower()}{lastname.lower()}",    # jdoe
                    f"{firstname.lower()}{lastname.lower()}",       # johndoe
                    f"{firstname.lower()}.{lastname.lower()}"       # john.doe
                ]
                
                # Write each format to the output file
                for format in formats:
                    out.write(format + '\n')

# Use the function by specifying the paths to your firstnames.txt and lastnames.txt
generate_usernames('firstnames_geo.txt', 'lastnames_geo.txt', 'output.txt')

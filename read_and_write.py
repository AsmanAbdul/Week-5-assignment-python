def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (for example, converting text to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Content successfully modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = "example.txt"
output_filename = "modified_example.txt"
read_and_modify_file(input_filename, output_filename)

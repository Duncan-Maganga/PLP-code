# Exception Handling

Errors happen! To make sure your programs are error-proof and user-friendly, Python provides Exception Handling. It’s the art of catching errors and handling them gracefully.

### Basic Structure of try-except Blocks ⚙

**try:** Runs code that might throw an error.  
**except:** Catches the error, allowing you to respond without crashing.  

**Example**
I created a program that reads a file and writes a modified version to a new one. I also built in error handling by asking the user for a filename and managing cases where the file doesn’t exist or can’t be read. Through this, I learned how to manage files efficiently in Python and handle errors gracefully, which allows me to build stronger and more reliable applications.


**Check it out ===>**
```
# creating input.txt file 

with open("input.txt", "w") as file:
    file.write("Hello, this the first file\n")
    file.write("This is the second line\n")
    file.write("This is the third line\n")
    file.write("This is the fourth line\n")
    file.write("This is the fifth line\n")

    # Lets try to reaad the file
def process_text_file():
    try:
        with open("input.txt", "r") as file:
            content = file.read()
                
# Lets count the words in the file 
        words = content.split()
        word_count = len(words)

# Lets convert into UPPERCASE
        uppercase_content = content.upper()

# Lets write the file output

        with open("output.txt", "w") as output_file:
            output_file.write("Processed Text File:\n")
            output_file.write("=" * 50 + "\n")
            output_file.write(uppercase_content)
            output_file.write("\n" + "=" * 50 + "\n")
            output_file.write(f"Total word count: {word_count}\n")


# Message to show the file has been created and prossessed
        print("Text file has been created and processed.")
        print(f"Total word count: {word_count}")

 # Handle the errors
    except FileNotFoundError:
        print("File not found, please check the file path or create it first.")
    except Exception as e:
        print(f"An error occured: {e}")
    
    with open("output.txt", "r") as f:
        content = f.read()
        print("Contents of output.txt:\n")
        print(content)


# RUN THE FUNCTION
process_text_file()
```
# Best Practices   
- Use with for file handling: Auto-close files, preventing potential leaks.  
- Check file existence before reading/writing, to avoid crashes.  
- Handle specific exceptions over general ones (e.g., FileNotFoundError instead of Exception).  
- Document error messages clearly for easier debugging and user support.  

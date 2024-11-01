def main():
    # Define the path to the file
    path_to_file = 'books/frankenstein.txt'

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Print the contents of the book
    #print(file_contents)

    #Count the words in the book
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

    #Count the characters in the book
    char_count = count_characters(file_contents)
    print("Character counts:", char_count)

    #Generate and print report
    print_report(path_to_file, word_count, char_count)

def count_words(text):
    #Split the text into words and return count
    words = text.split()
    return len(words)

def count_characters(text):
    #Create a dictionary to store character counts
    char_count = {}

    #Convert the text to lower case
    text = text.lower()

    #Loop through each character in the text
    for char in text:
        #Ignore spaces and other non-alphabetic characters if needed
        if char.isalpha(): #Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1 #Increment count if character exists 
            else:
                char_count[char] = 1 #Initialize count if char is new
    return char_count

def print_report(path, word_count, char_count):
    #Print the header
    print(f"---Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    #Sort characters by frequency in descending order
    sorted_characters = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    #Print each character count
    for char, count in sorted_characters:
        print(f"The '{char}' was found {count} times")
    
    #Print the footer
    print("--- End Report ---")

# Call the main function
if __name__ == "__main__":
    main()

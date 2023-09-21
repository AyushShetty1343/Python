#6a
def display_first_n_lines(filename,n):
    try:
        with open(filename,'r') as file:
            lines=file.readlines()
            for i in range(n):
                if i<len(lines):
                    print(lines[i].strip())
                else:
                    break
    except FileNotFoundError:
        print("not found")
        
def find_word_frequency(filename,word):
    try:
        with open(filename,'r') as file:
            content=file.read().lower()
            wordcount=content.count(word.lower())
            print("the word",word," occurs",wordcount," times")
    except FileNotFoundError:
        print("not found")
    
filename=input("enter a filename: ")
n=int(input("enter number of lines to display: "))
print("first n lines of the file: ")
display_first_n_lines(filename,n)
word=input("enter a word to find frequency: ")
find_word_frequency(filename,word)
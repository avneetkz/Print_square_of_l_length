# defining function for printing square 
def square(ch,len):
    for i in range(0,len):
        for j in range(0,len):
            print(ch, end=' ')
        print()

# driver code 
if __name__=="__main__":
    char=input("Enter the character of your choice: ")
    occ=int(input("Enter the number of occurrences: "))
    square(char, occ)

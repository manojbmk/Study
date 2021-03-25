my_str =["Manoj","malayalam","rugur","cake",1221,335]

for word in my_str:
    if type(word) == str:
        if word[::-1] == word:
            print(word," is palindrome")
        else:
            print("{} is not palindrome".format(word))
    elif type(word) == int:
        rem = rev = 0
        tmp = word 
        while tmp > 0:
            rem = tmp%10
            rev = rev*10+rem
            tmp = tmp//10
        if word == rev:
            print(word, " is a palindrome number")
        else:
            print(word, " is not a palindrome number")
    else:
        print("Invalid object in the list ")
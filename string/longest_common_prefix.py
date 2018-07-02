words = ["geeksforgeeks", "geeks",
                    "geeka", "geezer"]

# words = [
#   "abcdefgh",
#   "aefghijk",
#   "abcefgh"
# ]

def find_lcd(words):
    
    if not words:
        return False
    
    lcd = min(words)
    
    for word in words:
        counter = 0
        for letter in word:
            if counter < len(lcd) and letter == lcd[counter]:
                counter += 1
        
        if counter < len(lcd):
            lcd = word[:counter]
    
    return lcd    
    

print (find_lcd(words))

def max_char(txt:str):
    for char in txt:
        if len(txt) == 1:
            return char
        else:
            first = txt[0]
            rest = txt[1:]
            max_rest = max_char(rest)
            if max_rest > first:
                return max_rest
            else:
                return first
                    
            
         
txt = input("Word?" )
print(max_char(txt))
    

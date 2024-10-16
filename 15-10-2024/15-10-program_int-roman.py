def integer_to_roman(n):
    
    
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'}

    result = ''
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        
        #calculates how many times the current Roman numeral value (value) fits into n.
        count = n // value
        
        # appends the corresponding Roman numeral symbol (symbol) to the result string.and multplied with count
        result += symbol * count
        

        #updates n for the next iteration.
        n -= value * count

    return result
    
print(integer_to_roman(n=3749))
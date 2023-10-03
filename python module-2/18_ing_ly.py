def add_ing_or_ly(input_string):
    if len(input_string) < 3 :
        return input_string
    

    if input_string[-3:] == 'ing':
        result = input_string + 'ly'
    else:
        result = input_string + 'ing'

    return result



input_string = input("Enter String :")
new_string = add_ing_or_ly(input_string)
print("Result" , new_string)
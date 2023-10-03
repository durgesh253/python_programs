
input_string = "The weather is not that poor today, but not poor at all."

index_not = input_string.find('not')
index_poor = input_string.find('poor')

if index_not != -1 and index_poor != -1 and index_not < index_poor:
    
    input_string = input_string[:index_not] + 'good' + input_string[index_poor + 4:]

print(input_string)

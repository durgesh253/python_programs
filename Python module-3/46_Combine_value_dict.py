
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

result = {}

for item_dict in data:
    item_name = item_dict['item']
    amount = item_dict['amount']
    result[item_name] = result.get(item_name, 0) + amount

print("Combined Values:")
print(result)

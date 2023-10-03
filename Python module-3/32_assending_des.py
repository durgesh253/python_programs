my_dict = {'apple': 3, 'banana': 2, 'cherry': 5, 'date': 1}

assending_dict = dict(sorted(my_dict.items(), key=lambda item : item[1]))
dessending_dict = dict(sorted(my_dict.items() , key=lambda item : item[1] , reverse=True))


print("Assending dictonary is :",assending_dict)
print("Dessending dictonary is :",dessending_dict)

# Yes, you can use a single except block to handle multiple exceptions in Python by
# specifying multiple exception types within thesame except block

try:
    result = 10 / 0
except (ZeroDivisionError , NameError) as e:
    print(f"an error occured : {e}")
def area(width, height = None):
    if height == None:
        height = width
    return width*height

print(area(5))
print(area(5,8))
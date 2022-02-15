#Reading command line arguments
#Obviously this one must run on a console command line
import sys

name = sys.argv[1]
print("Hello " + name + "!!!")

print(" ")
print("This is the argv[0]: " + sys.argv[0])

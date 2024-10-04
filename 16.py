# Global variables

# Create a variable outside of a function, and
# use it inside the function and outside the function

a = "simple"      # scope of variable a is global

def myfunction():
    print("Python is " + a)

myfunction()
print(a)
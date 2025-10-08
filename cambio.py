#codigo super importante
def add(a,b):
    print("lolaso")
    return a + b
# COMENTARIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

"""
COMENTARIO MUTLILINEAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAA
"""
def sub(a,b):
    return a - b

def my_function():
  print("Hello from a function")

my_function()

# pene

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def countries(country = "Norway"):
  print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function("Brazil")

def nameFood(food):
  for x in food:
    print(x)


fruits = ["apple", "banana", "cherry"]

nameFood(fruits)

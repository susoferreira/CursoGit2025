#codigo super importante
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def my_function():
  print("Hello from a function")

my_function()



def my_function(fname):
  print(fname + " Refsnes")

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

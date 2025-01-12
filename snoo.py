def show(value):
  print(value)
def ask(value) :
  a = input(value)
  return a
def allTrue(value) :
  a=all(value)
  return a
def anyTrue(value) :
  a=any(value)
  return a
def convert(value) :
  a=bin(value)
  return a
def isfunc(value) :
  a=callable(value)
  return a
def getletter(value) :
  a=chr(value)
  return a
def info(value) :
  dir(value)
def getdiv(value) :
  a=divmod(value)
  return a
def multi(value) :
  eval(value)
def exe(value) :
  exec(value)
def deci(value) :
  a=float(value)
  return a
def getnum(value) :
  a=ord(value)
  return a
def expose(value1, value2) :
  a=pow(value1, value2)
  return a
def addall(value) :
  a=sum(value)
  return a
def file(name, settings) :
  a=open(name, settings)
  return a
def searchlist(value, search) :
  for x in value :
    if x==search :
      return  True
def searchdic(value, search) :
  for x in value :
    if x==search :
      return  True
def snoopyScene() :
  import turtle
  global scene
  scene = turtle.Turtle()
def snoopyGo(value) :
  scene.forward(value)
def snoopyTurn(value) :
  scene.right(value)
def my_function( greeting,*kids):
#   print("The youngest child is " + kids[2])
#   print (type(kids))
  for i in kids:
    print( greeting,i)
my_function(" hello","Emil", "Tobias", "Linus")
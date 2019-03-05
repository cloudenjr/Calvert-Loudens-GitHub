import Rasing_Exceptions_Ducks   # here we're importing the file Raising_Exceptions_Ducks which holds the .py file with
                                 # Duck classes and attributes

# Here we create instances of flock & ducks to use in the program

flock = Rasing_Exceptions_Ducks.Flock()
donald = Rasing_Exceptions_Ducks.Duck()
daisy = Rasing_Exceptions_Ducks.Duck()
duck3 = Rasing_Exceptions_Ducks.Duck()
duck4 = Rasing_Exceptions_Ducks.Duck()
duck5 = Rasing_Exceptions_Ducks.Duck()
duck6 = Rasing_Exceptions_Ducks.Duck()
duck7 = Rasing_Exceptions_Ducks.Duck()
percy = Rasing_Exceptions_Ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)
flock.add_duck(percy)

flock.migrate()

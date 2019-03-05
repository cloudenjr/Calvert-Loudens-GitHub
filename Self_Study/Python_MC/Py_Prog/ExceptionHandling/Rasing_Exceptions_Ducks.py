class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate  # by removing the () from .aviate, we're just making a reference to the aviate method

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

# parameters are annotated by using a colon followed by the type of parameter, and returned values are annotated by
# using the literal, a dash and > symbol

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:  #  this is a hint to inform parameters of what their values should be
                                             #  - if you use a hit for a param, then use it for all params, and return
                                             # values

        fly_method = getattr(duck, 'fly', None)  # getattr() checks an objects dictionary to see if it contains the
                                                 # attribute we specify
        # if  type(duck) is Duck:   # NEVER DO THIS, this doesnt work
        # if isinstance(duck, Duck):  # if you MUST do this type of checking, ALWAYS use 'isinstance()' method when
                                      # dealing with classes
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrage")  # TODO remove this before release
                # adding comment that contains () causes IntelliJ to track it as an item that needs to be done
                # also not case sensitive
            except AttributeError as e:  # syntax to store attribute error in variable to do something with later
                print("One duck down")
                problem = e
                # pass
        if problem:
            raise problem

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

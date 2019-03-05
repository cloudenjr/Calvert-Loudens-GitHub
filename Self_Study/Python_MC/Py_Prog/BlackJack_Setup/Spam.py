def spam1():

    def spam2():

        def spam3():
            # z = " even more spam"
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        # y = " more spam"
        y = " more " + x  # y must exist before spam3() is called
        y += spam3()  # do not combine these assigmnents
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam" # x must exist before spam2() is called
    x += spam2()  # do not combine these assignments
    # - merging above 2 lines of code to ' x = "spam" + spam2()' causes errors; sometimes you need mult lines to def a var
    # - wherever possible try to write functions so that they only use local variables and parameters
    # - only access global and nonlocal variables when its absolutely necessary
    # - no matter how trivial a change you've made, test the program thoroughly to make sure you haven't broken anything
    # - when defining variables using mult lines of code, include a comment so next programmer is aware of your logic
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())

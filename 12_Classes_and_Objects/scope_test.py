def scope_test():
    def do_local():
        spam = "local_spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal_spam"

    def do_global():
        global spam
        spam = "global_spam"

    spam = "test spam"
    do_local()
    print("After local assignment :", spam)
    do_nonlocal()
    print("After non-local assignment :", spam)
    do_global()
    print("After global assignment :", spam)


scope_test()
print("In global scope :", spam)

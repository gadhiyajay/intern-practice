def outfx(infx):
    def infx():
        print("HELLO THERE STARING THIS FUNCTION")
        infx()
        print("BYE BYE ENDING THIS FUNCTION")
        return infx
@outfx
def greet():
    print("Hello World!!")
# greet()


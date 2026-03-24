def third():
    print("I am third")
    print("third is done, going back to second")

def second():
    print("I am second")
    third()
    print("I am back in second")

def first():
    print("I am first")
    second()
    print("I am back in first")

first()



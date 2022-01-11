from logic import (
    Atom,
    Constant,
    Forall,
    Implies,
    And,
    createResolutionKB,
    createModelCheckingKB,
)


##### helper functions #####

counter = 1


def ask_p(kb, f):
    global counter
    print("\r\n", counter, "\tAsk: \t", f, "?")
    print(">>", "\t" + str(kb.ask(f)))
    counter = counter + 1


def tell_p(kb, f):
    global counter
    print("\r\n", counter, "\tTell: \t", f)
    print(">>", "\t" + str(kb.tell(f)))
    counter = counter + 1


##### /helper functions #####

kb = createResolutionKB()


def Croaks(x):
    return Atom("Croaks", x)


def EatsFlies(x):
    return Atom("Eats Flies", x)


def Chirps(x):
    return Atom("Chirps", x)


def Sings(x):
    return Atom("Sings", x)


def Animal(x):
    return Atom("Is a", x)


def Colour(x):
    return Atom("Colour", x)


frog = Constant("frog")
canary = Constant("canary")

green = Constant("green")
yellow = Constant("yellow")

kb = createResolutionKB()

# anywhere it is raining, it is wet

tell_p(kb, Forall("$x", Implies(And(Croaks("$x"), EatsFlies("$x")), Animal(frog))))

tell_p(kb, Forall("$x", Implies(And(Chirps("$x"), Sings("$x")), Animal(canary))))

tell_p(kb, Forall("$x", Implies(Colour(green), Animal(frog))))

tell_p(kb, Forall("$x", Implies(Colour(yellow), Animal(frog))))

ask_p(kb, Colour(frog))

# # is somewhere wet?
# ask_p(kb, Exists("$y", Wet("$y")))

kb.dump()

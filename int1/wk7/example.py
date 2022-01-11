from logic import *

Wumpus = Atom("Wumpus")
Hole = Atom("Hole")


def ask_p(kb, f):
    print("Ask: ", f)
    print(kb.ask(f))


def tell_p(kb, f):
    print("Tell: ", f)
    print(kb.tell(f))


kb = createResolutionKB()
tell_p(kb, Implies(Wumpus, Hole))
ask_p(
    kb,
)
ask_p(kb, Rain)
tell_p(kb, Rain)
ask_p(kb, Wet)
kb.dump()

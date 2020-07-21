from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Knight & Knave puzzle
    Or(AKnight, AKnave),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),

    # What character said
    Or(And(AKnight, AKnave), Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Knight & Knave puzzle
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),

    # What character said
    Or(And(AKnave, BKnave), Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Knight & Knave puzzle
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),

    # What characters said
    Or(Or(And(AKnight, BKnight), And(AKnave, BKnave)), Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Or(Or(And(AKnight, BKnave), And(AKnave, BKnight)), Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Knight & Knave puzzle
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, AKnave))),
    Implication(BKnight, Not(Or(Implication(AKnight, AKnave), Implication(AKnave, AKnave)))),
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),

    # What characters said
    Or(Or(AKnight, AKnave), Not(Or(AKnight, AKnave))),
    Or(Or(Implication(AKnight, AKnave), Implication(AKnave, AKnave)), Not(Or(Implication(AKnight, AKnave), Implication(AKnave, AKnave))))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

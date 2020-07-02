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
  And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))), #verify A is either Knight or knave but not both
  Or(And(AKnight,And(AKnight,AKnave)),And(AKnave,Not(And(AKnight,AKnave)))  #statement about A
))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),  #verify A and B is eiter knight or knave but not both
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    Or(
       And(AKnight,And(AKnave,BKnave)),         #A being Knight and statement
       And(AKnave,Not(And(AKnave,BKnave)))      #A being Knave
       ) 
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),       #verify A knight xor A knave
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),       #verify for B  knight Xor knave
    Or(
       And(And(AKnight,BKnight),Not(And(AKnight,BKnight))),     #A being knight and so, A,B both Knight
       And(Not(And(AKnave,BKnave)),And(AKnave,AKnave))          #A being knave and so, Not operation 
       
       )
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),  #cknight xor cknave
    Or(
       And(BKnave,And(AKnight,Not(CKnave))),            #things said by B for A and C being knight or knave
       And(BKnight,And(Not(AKnave),CKnave),AKnight)
       ),
    Or(
       AKnight, Not(AKnave)     #things said by A both possiblity
       ),
    Or(                         #things said by C both cases
      And( CKnight,AKnight),
      And(CKnave,Not(AKnight))
       )

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

from FiniteAutomata import FiniteAutomata

class Console:

    def __init__(self):
        self.fa = FiniteAutomata.readFromFile('FA.in')

    def displayAll(self):
        print(self.fa)

    def displayStates(self):
        print(self.fa.Q)

    def displayAlphabet(self):
        print(self.fa.E)

    def displayTransitions(self):
        print(self.fa.S)

    def displayFinalStates(self):
        print(self.fa.F)

    def displayInitialState(self):
        print(self.fa.q0)

    def checkDFA(self):
        print(self.fa.isDfa())

    def checkAccepted(self):
        seq = input()
        if self.fa.isAccepted(seq):
            print("Valid")
        else:
            print("Invalid")

    def displayMenu(self):
        print("1.Display states")
        print("2.Display alphabet")
        print("3.Display initial state")
        print("4.Display final states")
        print("5.Display transitions")
        print("6.Check DFA")
        print("7.Check accepted sequence")
        print("exit")

    def run(self):
        cmds = {'1': self.displayStates, '2': self.displayAlphabet, '3':self.displayInitialState,
                '4': self.displayFinalStates,'5': self.displayTransitions, '6': self.checkDFA,
                '7': self.checkAccepted}
        exit = False
        while not exit:
            self.displayMenu()
            print(">>")
            cmd = input()
            if cmd in cmds.keys():
                cmds[cmd]()
            elif cmd == "exit":
                exit = True
            else:
                continue

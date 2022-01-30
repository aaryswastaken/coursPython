import exercices
import os
import sys


def clearTerm():
    os.system('cls' if os.name == 'nt' else 'clear')


def pressEnterToContinue():
    input("Press enter to continue ...")


rLen = len(exercices.registered)


def lenOfStr(n):
    return len(str(n))


Pass = False
selected = None
func = None

className = ""
funcName = ""

if len(sys.argv) == 3:
    print("Found args ... searching")
    classId = int(sys.argv[1])
    if classId < rLen:
        classInst = exercices.registered[classId]()
        className = classInst.__name__
        funcId = int(sys.argv[2])
        if funcId < len(classInst.registered.keys()):
            funcName = [*classInst.registered][funcId]
            func = classInst.registered[funcName]

if func is None:
    print("Args invalid ... continuing default gui\n" if (len(sys.argv) > 1) else "", end="")
    while not Pass:
        clearTerm()
        for id, register in enumerate(exercices.registered):
            print("[{}{}] : {}".format((lenOfStr(rLen) - lenOfStr(id)) * " ", id, register.__name__))

        n = input("\n> ")

        try:
            n = int(n)
            if n < rLen:
                selected = exercices.registered[n]()
                Pass = True
            else:
                print("Number entered exceeded")
        except ValueError:
            print("Didnt entered a number ")
            pressEnterToContinue()

    print("\n\n")
    clearTerm()

    Pass = False
    selectedFunc = None

    while not Pass:
        clearTerm()
        rLen = len(selected.registered.keys())
        for id, (name, function) in enumerate(selected.registered.items()):
            print("[{}{}] : {}".format((lenOfStr(rLen) - lenOfStr(id)) * " ", id, name))

        n = input("\n> ")

        try:
            n = int(n)
            if n < rLen:
                selectedFunc = selected.registered[[*selected.registered][n]]
                Pass = True
            else:
                print("Number entered exceeded")
        except ValueError:
            print("Didnt entered a number ")
            pressEnterToContinue()

    print("\n\n")

    print("Starting {}/{}".format(selected.__name__, [*selected.registered][n]))
    selectedFunc()
else:
    print("Args valid ... continuing for {}/{}\n".format(className, funcName))
    func()

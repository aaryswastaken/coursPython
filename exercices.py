# commons
def askForN(c="n", strict_min=0, default=None):
    n = None
    stop = False
    while not stop:
        n = input(f"{c}{ f'[{default}]' if default is not None else '' }= ")
        if default is not None and n == "":
            return default
        try:
            if len(n) == 0:
                int("a")  # throw error
            n = int(n)
            if n < strict_min:
                int("a")
            stop = True
        except ValueError:
            print("Provided number isn't correct")

    return n


class SI_Physique:
    __name__ = "SI Physique"

    def __init__(self):
        self.registered = {"Activité 3 - Exo 2": self.act3exo2}

    @staticmethod
    def act3exo2():
        import matplotlib.pyplot as plt
        x = [0.0, 0.01, 0.03, 0.07, 0.12, 0.19, 0.28, 0.38]
        y = [0, 0, 0, 0, 0, 0, 0, 0]
        vx = [0, 0.15, 0.31, 0.46, 0.61, 0.77, 0.92, 1.07]
        dt = 0.1
        Dt = dt * 2
        NbPas = len(x) - 1
        ech_v = 0.01
        # presentation du graphique
        plt.title("Vecteurs accélérations", color='green', fontsize=12)
        plt.xlabel('x (m)', color='grey')
        plt.ylabel('y (m)', color='grey')
        plt.xlim(0, 0.4)
        plt.ylim(-0.1, 0.1)
        # Calcul de l'accélération
        for i in range(1, NbPas):
            ax = (vx[i + 1] - vx[i - 1]) / Dt
            plt.arrow(x[i], 0, ax * ech_v, 0, head_width=0.01, color='g')
            plt.plot(x[i], 0, 'r')
        plt.plot(x, y, '.')
        plt.show()


class Arithmetic:
    __name__ = "Arithmetic"

    def __init__(self):
        self.registered = {"Exo3 bruteforce": self.exo3BruteForce, "Diviseurs de n": self.dividersUI,
                           "a, b amiables": self.sontAmiables, "Recherche de nombre parfaits": self.findPerfects,
                           "Clé de RIB": self.rib_key, "Codage Affine": self.codageAffineUI,
                           "Coefficient de Bezout": self.coefBezout}

    @staticmethod
    def exo3BruteForce():
        nMax = askForN()

        buffer = False
        for n in range(nMax):
            buffer = buffer or not ((n ** 7 + 6 * n) % 7 == 0)

        print("Searching for {} values, (n^7 + 6n) % 7 == 0 has been proven {}".format(nMax, not buffer))

    def dividers(self, a, b=[], c=1):
        return self.dividers(a, b=([*b, c] if (a % c == 0) else b), c=c + 1) if c < a else b

    def dividersUI(self):
        n = askForN()
        print(f'Les diviseurs de {n} sont {", ".join([str(x) for x in self.dividers(n)])}')

    def sontAmiables(self):
        a = askForN(c="a")
        b = askForN(c="b")

        print(
            f'Les nombres {a} et {b} {"sont" if (sum(self.dividers(a)) == b and sum(self.dividers(b)) == a) else "ne sont pas"} amiables')

    def findPerfects(self):
        n = askForN()
        r = []
        for x in range(1, n + 1):
            if sum(self.dividers(x)) == x:
                r.append(x)

        print(f'Les nombres perfets en dessous de {n} sont {", ".join([str(x) for x in r])}')

    @staticmethod
    def rib_key(c="n", len_min=None, len_max=None):
        t = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 1, "k": 2, "l": 3, "m": 4,
             "n": 5, "o": 6, "p": 7, "q": 8, "r": 9, "s": 2, "t": 3, "u": 4, "v": 5, "w": 6, "x": 7, "y": 8, "z": 9,
             "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        def waitEnter():
            input("Press enter to continue ...")

        while True:
            try:
                i = input(f"{c}= ")
                r = []
                if len_min is not None and len(i) < len_min:
                    raise ValueError("Not the right size (min)")
                if len_max is not None and len(i) > len_max:
                    raise ValueError("Not the right size (max)")
                r = [t[char.lower()] for char in i]
                break
            except ValueError as e:
                print(e)
                waitEnter()
            except KeyError as e:
                print("One of the values is not correct. Please follow the regex /[a-zA-Z0-9]*/")

        n = int("".join(str(y) for y in r))
        k = 97 - (n * 100) % 97

        print(f"The key for {n} is {k}")

    @staticmethod
    def codageAffine(x, a, b, n=26):
        return (a * x + b) % n

    def codageAffineUI(self):
        text = input("$ ").lower()

        out = [chr(self.codageAffine(ord(x)-97, 11, 8) + 65) for x in text]

        print("".join(out))

    @staticmethod
    def coefBezout():
        a = askForN("a")
        b = askForN("b")

        A, B = a, b

        q, r = a, b
        q1, r1 = 0, 0

        temp = []

        pgcd = 0

        while True:
            q1 = q // r
            r1 = q % r

            temp.append([q, r, q1, r1])

            q = r
            r = r1

            if r == 0:
                break

            pgcd = r

        # Init des coef de bezout
        a, b = 1, -1
        for step in temp[::-1][2:]:  # Iterations sur les étapes inversées (2 dernières exclues)
            q, r, q1, r1 = step
            # r1 = q - r*q1

            a += b*(0-q1)
            a, b = b, a

            # print(step)

        # print(temp[::-1])
        print(f"{A}*{a} + {B}*{b} = {pgcd}")


class SPEMathsRevisions:
    __name__ = "Revisions SPE Maths"

    def __init__(self):
        self.registered = {
            "Fiche 1 - Exercice1": self.exercice1,
            "Fiche 1 - Exercice2": self.exercice2,
            "Fiche 1 - Exercice3": self.exercice3,
            "Fiche 1 - Exercice4.3": self.exercice4Compute,
            "Fiche 1 - Exercice4.4": self.exercice4Optimize}

    @staticmethod
    def exercice1():
        nMax = askForN()
        u = 4
        for n in range(nMax):
            u *= 3
            u += 2

        print(f"La suite (Un) tel que n={nMax} est {u}")

    @staticmethod
    def exercice2():
        A = askForN(c="A", strict_min=3)
        n = 0
        u = 3
        while True:
            if u > A:
                break

            u = 2 * u + 5
            n += 1

        print(f"La suite (Un) a pour valeur U>A tel que A={A} pour n={n} et donc u(n) = {u}")

    def exercice3Nested(self, n, nMax, output):
        return self.exercice3Nested(n + 1, nMax, [*output, output[-1] * (2 / 3) + 2]) if n <= nMax else output

    def exercice3(self):
        n = askForN()
        S = sum(self.exercice3Nested(1, n, [9]))

        print(f"La somme S de la suite (Un) est de S={S} pour n={n}")

    @staticmethod
    def exercice4Compute():
        n = askForN(strict_min=0)  # n >= 1
        u = sum([1 / ((i + 1) ** 3) for i in range(n)])
        v = u + 1 / n

        print(f"Les suites (Un) et (Vn) ont pout valeur u={u}, v={v} pour n={n}")

    @staticmethod
    def exercice4ComputeDiff(n):
        # Oui j'ai fait une fonction pour ca ... je pensais que le contenu serait plus ... fourni x)
        return 1 / n  # u(n) - v(n) = u(n) - (u(n) + 1/n) = -1/n

    def exercice4Optimize(self):
        p = askForN(c="p", strict_min=0)
        n = 1
        while True:
            if self.exercice4ComputeDiff(n) < 10 ** (-p):
                break
            n += 1

        print(f"Le plus petit entier n où r = |v(n) - u(n)| < 10^-{p} est n={n} pour r={self.exercice4ComputeDiff(n)}")


class SPEMaths:
    __name__ = "SPE Maths"

    def __init__(self):
        self.registered = {
            "Taux d'équipement": self.tauxEQ
        }

    @staticmethod
    def tauxEQ():
        import math

        def p(x):
            return 1 / (1 + math.exp(-0.2 * x))

        step, maxVal = 1, 0.95
        n = 0
        while True:
            if p(n) >= maxVal:
                break
            n += step

        print("La valeur est atteinte en n={}\nAvec p(n-1)={:.2f} et p(n)={:.2f}".format(2000 + n, p(n - 1), p(n)))


class SI_Gonano:
    __name__ = "SI Gonano"

    def __init__(self):
        self.registered = {
            "Exercice 1.1": self.exo1_1,
            "Exercice 2.3": self.exo2_3,
            "Exercice 3.1": self.exo3_1,
            "Exercice 4.1": self.exo4_1_wrapper
        }

    @staticmethod
    def exo1_1():
        nKo = 536
        print(f'Le poids du fichier est de {nKo * (2 ** 10)}')

    @staticmethod
    def exo2_3():
        n = input("Entrez votre note :\n$ ")

        print()

        try:
            n = float(n)
        except ValueError:
            print("Entrez une valeur valide svp")
            return

        x = ""

        if n >= 16:
            x = "très bien"
        elif n >= 14:
            x = "bien"
        elif n >= 12:
            x = "assez bien"
        elif n >= 10:
            x = "pas de mention"
        else:
            x = "recalé mskn"

        print(f'Avec une note de {n}, votre mention est de {x}')

    @staticmethod
    def exo3_1():
        for s in range(3):
            for x in range(0, 13):
                for n in range(s*4+1, (s+1)*4+1):
                    if x == 0:
                        print(f' --{n}--', end="\t\t")
                    else:
                        print(f'{x}{" " if x < 10 else ""} : {n*x}{"  " if x < 10 else (" " if x < 100 else "")}', end="\t")

                print()
            print()

    @staticmethod
    def exo4_1(n):
        return n ** 2

    def exo4_1_wrapper(self):
        n = input("Please enter a number\n$ ")

        try:
            n = float(n)
        except ValueError:
            print("Please insert a correct value ...")
            return

        print(self.exo4_1(n))


registered = [Arithmetic, SI_Physique, SPEMathsRevisions, SPEMaths, SI_Gonano]


class HalloPythonOO:
    """

    Definition/Bauplan der Objekte diese Klasse

    Parameter: keine

   """

    def __init__(self):
        '''Definition des Hallo Textes'''
        self.halloWeltText = "Hallo Python wirklich Objekt-Orientiert !!!"

    def sagHalloWelt(self):
        '''Ausgabe des Hallo Textes'''
        print(self.halloWeltText)


if __name__ == "__main__":
    halloPython = HalloPythonOO()
    halloPython.sagHalloWelt()

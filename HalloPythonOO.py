
class HalloPythonOO:
  
    def __init__(self):
        self.halloWeltText = "Hallo Python wirklich Objekt-Orientiert !!!"
  
    def sagHalloWelt(self):
        print(self.halloWeltText)
 
 
if __name__ == "__main__":
    halloPython = HalloPythonOO()
    halloPython.sagHalloWelt()

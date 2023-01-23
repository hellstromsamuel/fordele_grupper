class Student:
    def __init__(self, brukernavn, kjonn, program) -> None:
        self._brukernavn = brukernavn
        self._kjonn = kjonn
        self._program = program

    def __str__ (self):
        return self._brukernavn + " - " + self._kjonn

    def hentBrukernavn(self):
        return self._brukernavn

    def hentKjonn(self):
        return self._kjonn

    def hentProgram(self):
        return self._program

    

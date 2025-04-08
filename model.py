import random

class Model(object):
    #solo la logica del gioco
    def __init__(self):
        self._NMax=100
        self._TMax=6
        self._T=self._TMax
        self._segreto=None

    def reset (self):
        #questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0,self._NMax)
        self._T=self._TMax
        print (self._segreto)

    def play(self,guess ):
        """
        funzione che esegue uno step del gioco
        :param guess: int
        :return: 0 se vinto, 2 se hai finito vite, -1 se il numero era più piccolo, 1 se il numero era più grande
        """
        # da fuori arriva il tentativo e lo confrontiamo con il _segreto
        self._T -=1
        if guess==self._segreto:
            return 0 #ho vinto

        if self._T==0:
            return 2 #ho perso definitivamente

        if guess<self._segreto:
            return 1 #il numero da indovinare è maggiore

        if guess>self._segreto:
            return -1 # il numero segreto è più piccolo

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto

if __name__ == '__main__':
    m = Model()
    m.reset()
    print(m.play(90))
    print(m.play(5))
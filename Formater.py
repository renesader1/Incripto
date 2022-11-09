import numpy as np

# responsavel por transformar strings em matrizes
class Formater:

    def __int__(self, value):
        self.value = value

    def WordToASCIIMatrix(self):

        word = self
        # Verifica o tamanho da palavra e se impar, adiciona um espaço vazio no final dela
        if len(word) % 2 != 0:
            word = word + " "

        listx = []
        listy = []
        x = 0
        # Atribuí a palavra nas matrizes
        for i in range(int(len(word) / 2)):
            while len(listy) < 2:
                listy.append(ord(word[x]))
                x = x + 1
            listx.append(listy)
            listy = []
        return listx

    def CryptedWordToMatrix(self):
        listx = np.array([])
        listy = np.array([])
        x = 0
        # Atribuí a palavra nas matrizes
        for i in range(int(len(self)/2)):
            while len(listy) < 2:
                listy.append((self[x]))
                x = x + 1
            listx.append(listy)
            listy = []
        return listx


    def MatrixToWord(self):
        ConcatenedMensage = np.concatenate(self)
        CryptedMessage = ''.join(str(x) for x in ConcatenedMensage)

        return CryptedMessage
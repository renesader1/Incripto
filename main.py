import numpy as np
from Formater import Formater

class Incripto(Formater):

    def __init__(self, word, key, method):
        self.method = method
        self.key = Formater.WordToASCIIMatrix(key)
        self.word = word

        if method == "1":
            self.word = Formater.WordToASCIIMatrix(word)
            Incripto.Encrypt(self)
            
        else:
            Incripto.Decrypt(self)
            
        Incripto.VerifyKey(self)

    def VerifyKey(self):
        if 2 == len(self.key):
            return
        raise ValueError("The key must be 4 characters length")

    def Encrypt(self):
        Matrix = np.matmul(self.word, self.key)
        print (Matrix)
        return Matrix
        
    def Decrypt(self):
        DecryptedMatrix = np.matmul((self.word), np.linalg.inv(self.key))
        print(DecryptedMatrix)
        return DecryptedMatrix

Method = input(" 1 - criptografar, 2 - descriptografar \n What do you want to do: ")
Message = np.array(input(" Insert your message: "))
Key = input(" insert you cryptography key: ")
A = Incripto(Message, Key, Method)


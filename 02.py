class Domino:
     def __init__(self, face_a=0, face_b=0):
         self.face_a = face_a
         self.face_b = face_b
 
     def mostrar_pontos(self):
         return f"lado A: {self.face_a} lado B: {self.face_b}"
 
     def valor(self):
         return self.face_a + self.face_b
 
     def __str__(self):
         return f"Dominó ({self.face_a}, {self.face_b})"
 
d1 = Domino(2, 6)
d2 = Domino(4, 3)
 
print(d1.mostrar_pontos())
print(d2.mostrar_pontos())
 
print("Total de pontos:", d1.valor() + d2.valor())
 
print(d1)
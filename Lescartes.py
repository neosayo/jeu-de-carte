Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Carte :
	def _init_(self,val,coul) :
		self.valeur = val
		self.couleur = coul

		
>>> from Lescartes import Carte
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    from Lescartes import Carte
ImportError: No module named 'Lescartes'
>>> from Lescartes import Carte
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    from Lescartes import Carte
ImportError: No module named 'Lescartes'
>>>  class Carte :
	def __init__(self,val,coul) :
		self.valeur = val
		self.couleur = coul
		
SyntaxError: unexpected indent
>>> class Carte :
	def __init__(self,val,coul) :
		self.valeur = val
		self.couleur = coul

		
>>> 
================ RESTART: D:/fauquet/POO_python/Lescartes2.py ================
>>> 
================ RESTART: D:/fauquet/POO_python/Lescartes2.py ================
>>> from Lescartes import Carte
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    from Lescartes import Carte
  File "D:/fauquet/POO_python\Lescartes.py", line 1
    Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
             ^
SyntaxError: invalid syntax
>>> from Lescartes2 import Carte
>>> C1 = Carte(6-"Coeur")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    C1 = Carte(6-"Coeur")
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> C1 = Carte(6,"Coeur")
>>> C1.couleur
'Coeur'
>>> c1.valeur
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c1.valeur
NameError: name 'c1' is not defined
>>> C1.valeur
6
>>> class Carte :
	def__iniy__(self,val,coul) :
		
SyntaxError: invalid syntax
>>> class Carte :
	def__init__(self,val,coul) :
		
SyntaxError: invalid syntax
>>> class Carte :
	def __init__(self,val,coul) :
		self.valeur = val

		
>>> class Carte :
	def __init__(self,val,coul) :
		self.valeur = val
def affiche(self) :
	
SyntaxError: invalid syntax
>>> class Carte :
	def __init__(self,val,coul) :
		self.valeur = val
 def affiche(self) :
	 
SyntaxError: unindent does not match any outer indentation level
>>> class Carte :
	def __init__(self,val,coul) :
		self.valeur = val
		def affiche(self) :
			print (self.valeur,'de',self.couleur)

			
>>> C1.affiche()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    C1.affiche()
AttributeError: 'Carte' object has no attribute 'affiche'
>>> C1.affiche()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    C1.affiche()
AttributeError: 'Carte' object has no attribute 'affiche'
>>> 
================ RESTART: D:/fauquet/POO_python/Lescartes2.py ================
>>> from Lescartes import Carte
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    from Lescartes import Carte
  File "D:/fauquet/POO_python\Lescartes.py", line 1
    Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
             ^
SyntaxError: invalid syntax
>>> from Lescartes import Carte
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    from Lescartes import Carte
  File "D:/fauquet/POO_python\Lescartes.py", line 1
    Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
             ^
SyntaxError: invalid syntax
>>> from Lescartes2 import Carte
>>> C1.affiche()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    C1.affiche()
NameError: name 'C1' is not defined
>>> C1 = Carte(6,"Coeur")
>>> C1.couleur
'Coeur'
>>> c1.valeur
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    c1.valeur
NameError: name 'c1' is not defined
>>> C1.valeur
6
>>> C1.affiche()
6 de Coeur
>>> C2 = Carte(Dame,Pique)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    C2 = Carte(Dame,Pique)
NameError: name 'Dame' is not defined
>>> C2 = Carte(Dame,"Pique")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    C2 = Carte(Dame,"Pique")
NameError: name 'Dame' is not defined
>>> C2 = Carte("Dame","Pique")
>>> C2.c
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    C2.c
AttributeError: 'Carte' object has no attribute 'c'
>>> C2.couleur
'Pique'
>>> C2.valeur
'Dame'
>>> 

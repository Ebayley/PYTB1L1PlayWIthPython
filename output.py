Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Elona')
Mijn naam is Elona
>>> naam = 'Elona'
>>> print(naam)
Elona
>>> print(naam.upper())
ELONA
>>> print(naam[0:2])
El
>>> print(naam[::-1])
anolE
>>> leeftijd = 20
>>> print('Hallo' + naam + 'ben je al' + str(leeftijd) + ' jaar?')
HalloElonaben je al20 jaar?
>>> print('Hallo ' + naam + ' ben je al' + str(leeftijd) + ' jaar?')
Hallo Elona ben je al20 jaar?
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Elona ben je al 20 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
21
>>> leeftijd-=1
>>> leeftijd
20
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Het is alweer 2 jaar geleden dat je 18 werd ;-)
>>> from random import radint
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'radint' from 'random' (C:\Users\elona\AppData\Local\Programs\Python\Python38-32\lib\random.py)
>>> from random import randint
>>> randint(0,1000)
936
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
616
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 616
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 616
>>> willekeurig_getal
616
>>> willekeurig_getal
616
>>> randint(0,1000)
231
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
758
>>> willekeurig_getal
758
>>> from fatetime import datetime
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fatetime'
>>> from datetime import datetime
>>> datum = fatetime.now()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fatetime' is not defined
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:31:43.834663
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>>

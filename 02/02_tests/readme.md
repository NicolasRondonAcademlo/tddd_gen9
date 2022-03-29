# Organizando los tests
Podemos crear un grupo de test y tenerlo
dentro de un folder
Estos test se ejecutaran atravez de 
**unittest discover** que buscara por todos
los test  que cumplan la conticion 
test*.py
python3 -m unittest discover 02_tests -v

Incluso podemos elegir que test correr con
-k  le añadismos el nombre que queremos
buscar en los tests
python3 -m unittest discover 02_tests -k sum -v
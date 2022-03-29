# aparte de clases, tests, modulos a veces queremos configurar algo
# que es necesario para all el proyecto
# Para eso necesitamos crear un archivo conftest.py
# esa fixture necesita ser declarada con  scope="session"
# y autouse=True para usarlo en todos los test


def test_1():
    pass
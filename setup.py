# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Systemy Wielowarstwowe Lab2 API",
    author_email="marcin.nowak1@edu.wsti.pl",
    url="",
    keywords=["Swagger", "Systemy Wielowarstwowe Lab2 API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    _08255 Nowak Marcin 7ION_  Opis API API powinno być spełniać wszystkie reguły REST (za wyjątkiem kodu na żądanie) oraz implementować HATEOAS. Będzie się ono składać się z następujących zasobów: projekty, zadania, komentarze do zadań oraz członkowie zespołu. Dla uproszczenia zakładamy, że API dostępne jest tylko wewnątrz prywatnej sieci i nie wymaga uwierzytelniania ani autoryzacji użytkowników.  Funkcjonalność do zaimplementowania Funkcjonalność, która powinna być udostępniona przez API została podzielona wg. zasobów w systemie. - Projekty   - Tworzenie nowego projektu. Podczas tworzenia nowego projektu użytkownik powinien podać podstawowe dane (jak np. nazwa, opis, data rozpoczęcia czy też planowana data zakończenia). W odpowiedzi klient powinien otrzymać identyfikator nowego projektu.   - Pobieranie listy wszystkich projektów.   - Pobieranie szczegółów na temat danego projektu.   - Aktualizacja szczegółów danego projektu.   - Usuwanie konkretnego projektu. - Zadania   - Dodawanie nowego zadania w ramach konkretnego projektu. Zadanie powinno zawierać takie informacje jak nazwa, opis, priorytet oraz szacowany termin wykonania.   - Listowanie zadań w ramach konkretnego projektu.   - Pobieranie szczegółów konkretnego zadania.   - Aktualizacja szczegółów konkretnego zadania.   - Usuwanie konkretnego zadania. - Członkowie zespołu   - Dodawanie nowego użytkownika do zespołu projektowego.   - Pobieranie listy członków zespołu danego projektu.   - Usuwanie użytkownika z zespołu. - Komentarze   - Możliwość dodawania nowego komentarza do konkretnego zadania.   - Możliwość pobierania listy komentarzy do konkretnego zadania.   - Usuwanie konkretnego komentarza.
    """
)

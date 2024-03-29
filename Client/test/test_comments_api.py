# coding: utf-8

"""
    Systemy Wielowarstwowe Lab2 API

    _08255 Nowak Marcin 7ION_  Opis API API powinno być spełniać wszystkie reguły REST (za wyjątkiem kodu na żądanie) oraz implementować HATEOAS. Będzie się ono składać się z następujących zasobów: projekty, zadania, komentarze do zadań oraz członkowie zespołu. Dla uproszczenia zakładamy, że API dostępne jest tylko wewnątrz prywatnej sieci i nie wymaga uwierzytelniania ani autoryzacji użytkowników.  Funkcjonalność do zaimplementowania Funkcjonalność, która powinna być udostępniona przez API została podzielona wg. zasobów w systemie. - Projekty   - Tworzenie nowego projektu. Podczas tworzenia nowego projektu użytkownik powinien podać podstawowe dane (jak np. nazwa, opis, data rozpoczęcia czy też planowana data zakończenia). W odpowiedzi klient powinien otrzymać identyfikator nowego projektu.   - Pobieranie listy wszystkich projektów.   - Pobieranie szczegółów na temat danego projektu.   - Aktualizacja szczegółów danego projektu.   - Usuwanie konkretnego projektu. - Zadania   - Dodawanie nowego zadania w ramach konkretnego projektu. Zadanie powinno zawierać takie informacje jak nazwa, opis, priorytet oraz szacowany termin wykonania.   - Listowanie zadań w ramach konkretnego projektu.   - Pobieranie szczegółów konkretnego zadania.   - Aktualizacja szczegółów konkretnego zadania.   - Usuwanie konkretnego zadania. - Członkowie zespołu   - Dodawanie nowego użytkownika do zespołu projektowego.   - Pobieranie listy członków zespołu danego projektu.   - Usuwanie użytkownika z zespołu. - Komentarze   - Możliwość dodawania nowego komentarza do konkretnego zadania.   - Możliwość pobierania listy komentarzy do konkretnego zadania.   - Usuwanie konkretnego komentarza.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: marcin.nowak1@edu.wsti.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.comments_api import CommentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self):
        self.api = CommentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_task_comments(self):
        """Test case for add_task_comments

        Add task comment  # noqa: E501
        """
        pass

    def test_get_task_comments(self):
        """Test case for get_task_comments

        List task comments  # noqa: E501
        """
        pass

    def test_remove_task_comments(self):
        """Test case for remove_task_comments

        Delete task comment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

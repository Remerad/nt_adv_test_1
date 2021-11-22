from main import *
import mock
import copy
from pathlib import Path


class TestCalculatePytest:

    def test_check_document_existance(self, user_doc_number):
        assert check_document_existance("10006") == True
        assert check_document_existance("11-2") == True
        assert check_document_existance("2207 876234") == True
        assert check_document_existance("2207") == False

    def test_get_doc_owner_name(self):
        with mock.patch('builtins.input', return_value="10006"):
            assert get_doc_owner_name() == "Аристарх Павлов"
        with mock.patch('builtins.input', return_value="2207 876234"):
            assert get_doc_owner_name() == "Василий Гупкин"
        with mock.patch('builtins.input', return_value="11-2"):
            assert get_doc_owner_name() == "Геннадий Покемонов"
        with mock.patch('builtins.input', return_value="11-2"):
            assert get_doc_owner_name() != "Алибаба Алибабаевич"

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == set(['Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'])
        assert get_all_doc_owners_names() != set(['Аристарх Павлов', 'Василий Гупкин', 'Алибаба Алибабаевич'])

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf("11-2")
        assert directories['1'] == ['2207 876234', '5455 028765']


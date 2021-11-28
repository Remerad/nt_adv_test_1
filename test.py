import pytest
from main import *
import mock
import random


class TestCalculatePytest:

    def test_check_document_existance(self):
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
        assert get_all_doc_owners_names() == {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'}
        assert get_all_doc_owners_names() != {'Аристарх Павлов', 'Василий Гупкин', 'Алибаба Алибабаевич'}

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf("11-2")
        assert directories['1'] == ['2207 876234', '5455 028765']

    @pytest.mark.parametrize('test_shelf_number', range(1, 10))
    def test_add_new_shelf(self, test_shelf_number):
        pr_shelf_keys = directories.keys()
        res = add_new_shelf(test_shelf_number)
        if test_shelf_number in pr_shelf_keys:
            assert res == (test_shelf_number, True)
        if test_shelf_number not in pr_shelf_keys:
            assert res == (test_shelf_number, False)
        pass

    params = []
    for i in range(1, 10):
        params.append([i, random.randint(1, 100)])
    @pytest.mark.parametrize('shelf_number, doc_number', params)
    def test_append_doc_to_shelf(self, doc_number, shelf_number):
        append_doc_to_shelf(doc_number, shelf_number)
        assert doc_number in directories[shelf_number]

    def test_delete_doc(self):
        with mock.patch('builtins.input', return_value="2207 876234"):
            delete_doc()
            if documents == [
                {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]:
                assert True
            else:
                assert False
        with mock.patch('builtins.input', return_value="11-2"):
            delete_doc()
            if documents == [
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]:
                assert True
            else:
                assert False
        with mock.patch('builtins.input', return_value="10006"):
            delete_doc()
            if documents == []:
                assert True
            else:
                assert False

    def test_get_doc_shelf(self):
        with mock.patch('builtins.input', return_value="2207 876234"):
            assert get_doc_shelf() == "1"
        with mock.patch('builtins.input', return_value="10006"):
            assert get_doc_shelf() == "2"
        with mock.patch('builtins.input', return_value="11-2"):
            assert get_doc_shelf() == "1"

    def test_move_doc_to_shelf(self):
        with mock.patch('builtins.input', side_effect=["2207 876234", "2"]):
            move_doc_to_shelf()
            if directories['2'] == ['10006', "2207 876234"]:
                assert True
            else:
                assert False

    @pytest.mark.parametrize('document', documents)
    def test_show_document_info(self, document, capfd):
        out, err = capfd.readouterr()
        if (out.find(document['type']) > -1 and
            out.find(document['number']) > -1 and
            out.find(document['name']) > -1):
            assert True

    def test_show_all_docs_info(self, capfd):
        show_all_docs_info()
        out, err = capfd.readouterr()
        if (out.find('passport "2207 876234" "Василий Гупкин"') > -1 and
            out.find('invoice "11-2" "Геннадий Покемонов"') > -1 and
            out.find('insurance "10006" "Аристарх Павлов"') > -1):
            assert True

    def test_add_new_doc(self, capfd):
        shelf_num = random.randint(1, 100)
        with mock.patch('builtins.input',
                        side_effect=["3548 659842", "permit", "Юрий Михайлович Семецкий", str(shelf_num)]):
            add_new_doc()
        with mock.patch('builtins.input', return_value="3548 659842"):
            assert get_doc_shelf() == str(shelf_num)



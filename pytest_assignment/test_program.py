import pytest
from program import divide_numbers, reverse_string, get_list_element

def test_divide_numbers_normal():
    assert divide_numbers(10, 3) == 3.33

def test_divide_numbers_edge():
    assert divide_numbers(50000000, 5) == 10000000.00
    assert divide_numbers(-98, 2.5) == -39.20
    assert divide_numbers(0, 10000) == 0.00

def test_divide_numbers_corner():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(2, 0)

def test_reverse_string_normal():
    assert reverse_string("JOHN CENA") == "anec nhoj"
    assert reverse_string("hello world") == "DLROW OLLEH"
    assert reverse_string("yOLo") == "OloY"

def test_reverse_string_edge():
    assert reverse_string("a") == "A"
    assert reverse_string("SupeRcalIfrAgilisTIcexpiaLidOciOUS") == "suoICoDIlAIPXECitSILIGaRFiLACrEPUs"
    assert reverse_string("") == ""

def test_reverse_string_corner():
   with pytest.raises(TypeError):
       reverse_string(-9000)
       reverse_string(0)
       reverse_string(3.87)

def test_get_list_element_normal():
    lst = [5, 4, 3]
    assert get_list_element(lst, 1) == 4

def test_get_list_element_edge():
    lst = [9,0,9]
    assert get_list_element(lst, 10) == "Not found"

def test_get_list_element_corner():
    lst =[]
    assert get_list_element(lst, 0) == "Not found"
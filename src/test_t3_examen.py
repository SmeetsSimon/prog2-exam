import pytest

from t3_examen import (
    benader_pi,
    faculteit,
    is_geldig_rijksregisternummer,
    is_isogram,
    rijksregisternummer_controlegetal,
    rijksregisternummer_geboortedag,
    rijksregisternummer_geboortejaar,
    rijksregisternummer_geboortemaand,
    rijksregisternummer_hoofdgetal,
    rijksregisternummer_is_vrouw,
    volume_kegel,
)


def test_faculteit():
    result = faculteit(1)
    assert result == 1


def test_faculteit_2():
    result = faculteit(2)
    assert result == 2


def test_faculteit_3():
    result = faculteit(3)
    assert result == 6


def test_faculteit_4():
    result = faculteit(4)
    assert result == 24


def test_faculteit_5():
    result = faculteit(5)
    assert result == 120


def test_faculteit_6():
    result = faculteit(6)
    assert result == 720


TESTDATA_FACULTEIT = [
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
]


@pytest.mark.parametrize("n,expected", TESTDATA_FACULTEIT)
def test_faculteit_numbers(n, expected):
    result = faculteit(n)
    assert result == expected


def test_rijksregisternummer_controlegetal_1():
    result = rijksregisternummer_controlegetal("42.01.22-051.81")
    assert result == 81


def test_rijksregisternummer_controlegetal_2():
    result = rijksregisternummer_controlegetal("64.10.16-123.35")
    assert result == 35


def test_rijksregisternummer_controlegetal_3():
    result = rijksregisternummer_controlegetal("28.03.08-944.07")
    assert result == 7


def test_rijksregisternummer_hoofdgetal_1():
    result = rijksregisternummer_hoofdgetal("58.08.12-175.60")
    assert result == 580812175


def test_rijksregisternummer_hoofdgetal_2():
    result = rijksregisternummer_hoofdgetal("64.10.16-123.35")
    assert result == 641016123


def test_rijksregisternummer_hoofdgetal_3():
    result = rijksregisternummer_hoofdgetal("28.03.08-944.07")
    assert result == 280308944


def test_rijksregisternummer_hoofdgetal_4():
    result = rijksregisternummer_hoofdgetal("55.02.16-497.95")
    assert result == 550216497


def test_rijksregisternummer_man_1():
    result = rijksregisternummer_is_vrouw("42.01.22-051.81")
    assert result is False


def test_rijksregisternummer_man_2():
    result = rijksregisternummer_is_vrouw("55.02.16-497.95")
    assert result is False


def test_rijksregisternummer_man_3():
    result = rijksregisternummer_is_vrouw("40.08.02-605.37")
    assert result is False


def test_rijksregisternummer_vrouw_1():
    result = rijksregisternummer_is_vrouw("28.03.08-944.07")
    assert result is True


def test_rijksregisternummer_vrouw_2():
    result = rijksregisternummer_is_vrouw("81.03.08-154.67")
    assert result is True


def test_rijksregisternummer_vrouw_3():
    result = rijksregisternummer_is_vrouw("89.02.16-326.10")
    assert result is True


TESTDATA_RR_NUMMERS = [
    ("42.01.22-051.81", 81, 420122051, 42, 1, 22),
    ("64.10.16-123.35", 35, 641016123, 64, 10, 16),
    ("85.02.01-002.00", 00, 850201002, 85, 2, 1),
]


@pytest.mark.parametrize("rrn,controle,hoofdgetal,year,month,day", TESTDATA_RR_NUMMERS)
def test_rrn_geboortejaren(rrn, controle, hoofdgetal, year, month, day):
    result = rijksregisternummer_geboortejaar(rrn)
    assert result == year


@pytest.mark.parametrize("rrn,controle,hoofdgetal,year,month,day", TESTDATA_RR_NUMMERS)
def test_rrn_geboortemaanden(rrn, controle, hoofdgetal, year, month, day):
    result = rijksregisternummer_geboortemaand(rrn)
    assert result == month


@pytest.mark.parametrize("rrn,controle,hoofdgetal,year,month,day", TESTDATA_RR_NUMMERS)
def test_rrn_geboortedagen(rrn, controle, hoofdgetal, year, month, day):
    result = rijksregisternummer_geboortedag(rrn)
    assert result == day


def test_rijksregisternummer_geldig1():
    result = is_geldig_rijksregisternummer("58.08.12-175.60")
    assert result is True


def test_rijksregisternummer_geldig2():
    result = is_geldig_rijksregisternummer("66.02.02-638.23")
    assert result is True


def test_rijksregisternummer_geldig3():
    result = is_geldig_rijksregisternummer("56.03.29-763.49")
    assert result is True


def test_rijksregisternummer_geldig4():
    result = is_geldig_rijksregisternummer("74.10.19-809.51")
    assert result is True


def test_rijksregisternummer_ongeldig1():
    result = is_geldig_rijksregisternummer("01.02.24-196.11")
    assert result is False


def test_rijksregisternummer_ongeldig2():
    result = is_geldig_rijksregisternummer("66.02.02-638.43")
    assert result is False


def test_rijksregisternummer_ongeldig3():
    result = is_geldig_rijksregisternummer("56.03.29-763.19")
    assert result is False


def test_rijksregisternummer_ongeldig4():
    result = is_geldig_rijksregisternummer("12.06.19-069.82")
    assert result is False


def test_is_isogram():
    result = is_isogram("opslagruimte")
    assert result is True


def test_is_geen_isogram():
    result = is_isogram("voorbeelden")
    assert result is False


TESTDATA_ANAGRAMS = [
    ("vier", True),
    ("veer", False),
    ("kleur", True),
    ("vlees", False),
    ("plagen", True),
    ("plegen", False),
    ("klagers", True),
    ("vijvers", False),
    ("landbouw", True),
    ("drinkfles", True),
    ("olifanten", False),
    ("polsbandje", True),
    ("vragenlijst", True),
]


@pytest.mark.parametrize("word,expected", TESTDATA_ANAGRAMS)
def test_are_isograms(word, expected):
    result = is_isogram(word)
    assert result is expected


def test_volume_kegel_2_3():
    v = volume_kegel(r=2, h=3)
    expected = 12.566
    assert abs(v - expected) < 0.01


def test_volume_kegel_8_12():
    v = volume_kegel(r=8, h=12)
    expected = 804.25
    assert abs(v - expected) < 0.01


def test_volume_kegel_1_1():
    v = volume_kegel(r=1, h=1)
    expected = 1.05
    assert abs(v - expected) < 0.01


def test_volume_kegel_1_10():
    v = volume_kegel(r=1, h=10)
    expected = 10.47
    assert abs(v - expected) < 0.01


def test_volume_kegel_10_1():
    v = volume_kegel(r=10, h=1)
    expected = 104.72
    assert abs(v - expected) < 0.01


def test_volume_kegel_10_10():
    v = volume_kegel(r=10, h=10)
    expected = 1047.2
    assert abs(v - expected) < 0.01


def test_volume_kegel_3_3():
    v = volume_kegel(r=3, h=3)
    expected = 28.27
    assert abs(v - expected) < 0.01


def test_volume_kegel_20_30():
    v = volume_kegel(r=20, h=30)
    expected = 12566.37
    assert abs(v - expected) < 0.01


def test_volume_kegel_2_35():
    v = volume_kegel(r=2, h=35)
    expected = 146.61
    assert abs(v - expected) < 0.01


def test_volume_kegel_11_21():
    v = volume_kegel(r=1.1, h=2.1)
    expected = 2.66
    assert abs(v - expected) < 0.01


def test_pi_2():
    result = benader_pi(2)
    assert abs(result - 2.66) < 0.1


def test_pi_11():
    result = benader_pi(11)
    assert abs(result - 3.2323) < 0.1


TESTDATA_PI = [
    (3, 3.466),
    (4, 2.8952),
    (5, 3.3396),
    (6, 2.9760),
    (7, 3.2837),
    (8, 3.01707),
    (9, 3.252369),
    (10, 3.041839),
]


@pytest.mark.parametrize("n,expected", TESTDATA_PI)
def test_benader_pi(n, expected):
    result = benader_pi(n)
    assert abs(result - expected) < 0.001

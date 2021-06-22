import math


def is_isogram(word):
    """Geef True terug als het woord een isogram is, anders False

    Een isogram is een woord waarin geen enkele letter dubbel voorkomt.

    Dus, "vier" is bijvoorbeeld een isogram, maar "veer" niet omdat
    de letter "e" er meer dan 1 keer in voorkomt.
    """
    return 0


def faculteit(n):
    """Bereken de faculteit van n

    De faculteit van n, is de faculteit van n-1 * n.
    Dus, de faculeit van 3 is 3 * de faculteit van 2.

    Oftewel de faculteit van 3 is:
    3 * 2 * 1 == 6

    De faculteit van 4 is:
    4 * 3 * 2 * 1 == 24

    De faculteit van 1 is 1.
    """
    return 0


def rijksregisternummer_controlegetal(rrn):
    """Geef het controlegetal terug gegeven een rijksregisternummer

    Het controlegetal is het getal gevormd door de laatste twee cijfers
    van het rijksregisternummer.
    """
    return 0


def rijksregisternummer_geboortejaar(rrn):
    """Geef het geboortejaar terug gegeven een rijksregisternummer

    De eerste twee cijfers van het rijksregisternummer vormen het
    geboortejaar.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is het geboortejaar 42 (1942).
    """
    return 0


def rijksregisternummer_geboortemaand(rrn):
    """Geef de geboortemaand terug gegeven een rijksregisternummer

    Het derde en vierde cijfer vormen samen de geboortemaand.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is het geboortemaand 1 (januari).
    """
    return 0


def rijksregisternummer_geboortedag(rrn):
    """Geef de geboortedag terug gegeven een rijksregisternummer

    Het vijfde en zesde cijfer vormen samen de geboortedag.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is het geboortedag 22.
    """
    return 0


def rijksregisternummer_is_vrouw(rrn):
    """Geef True terug als de persoon een vrouw is

    Als het getal na de spatie en voor het koppelteken
    vormen een volgnummer. Als deze nummer even is,
    is de persoon een vrouw, is de nummer oneven,
    dan is de persoon een man.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is de persoon dus een man.
    """
    return 0


def rijksregisternummer_hoofdgetal(rrn):
    """Geef het hoofdgetal terug

    De eerste 9 cijfers in het rijksregisternummer vormen
    het hoofdgetal.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is het hoofdgetal dus 420122051.
    """
    return 0


def is_geldig_rijksregisternummer(rrn):
    """Geef True terug als het rijksregisternummer geldig is.

    De eerste 9 cijfers in het rijksregisternummer vormen
    het hoofdgetal.
    Bereken de rest bij deling door 97 van dit getal.
    Trek dit getal van 97 af.
    Als dit resultaat gelijk is aan het controlegetal,
    is het een geldig rijksregisternummer.

    42.01.22 051-81
    YY.MM.DD NUM-CT

    In bovenstaand voorbeeld is het hoofdgetal 420122051.
    Het controlegetal is 81.
    Delen van 420122051 door 97 geeft als rest 16.
    97 - 16 is 81, dit komt overeen met het controlegetal,
    dus het rijksregisternummer is geldig.

    """
    return 0


def volume_kegel(r, h):
    """Return volume kegel met straal r en hoogte h

    Het volume van een kegel met straal r en hoogte h
    wordt berekend door:
    V = 1/3 * π * r^2 * h
    """

    return 0


def benader_pi(n):
    """Geef een benadering van π gebruik makend van de Gregory-Leibniz serie

    Als n == 1:
    π = 4/1

    Als n == 2:
    π = 4/1 - 4/3

    Als n == 3:
    π = 4/1 - 4/3 + 4/5

    Of in het algemeen, gebruik n termen (hier is n == 8),
    met het teken telkens wisselend, en de noemer
    telkens 2 hoger:
    π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15...

    Of, met de noemer die altijd 4 is buiten de haakjes:
    π = 4 * (1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15)
    """
    return 0

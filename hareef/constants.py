# coding: utf-8

"""
Constants that are used by all models
"""

import enum


class  ArabicDiacritics(enum.Enum):
    """All possible Arabic diacritics."""

    NO_DIACRITIC = ''
    SUKOON = 'ْ'
    SHADDA = 'ّ'
    DAMMA = 'ُ'
    FATHA = 'َ'
    KASRA = 'ِ'
    TANWEEN_DAMMA = 'ٌ'
    TANWEEN_FATHA = 'ً'
    TANWEEN_KASRA = 'ٍ'
    SHADDA_PLUS_DAMMA = 'ُّ'
    SHADDA_PLUS_FATHA = 'َّ'
    SHADDA_PLUS_KASRA = 'ِّ'
    SHADDA_PLUS_TANWEEN_DAMMA = 'ٌّ'
    SHADDA_PLUS_TANWEEN_FATHA = 'ًّ'
    SHADDA_PLUS_TANWEEN_KASRA = 'ٍّ'


BASIC_DIACRITICS = {
    diac.value
    for diac in {
        ArabicDiacritics.SUKOON,
        ArabicDiacritics.SHADDA,
        ArabicDiacritics.DAMMA,
        ArabicDiacritics.FATHA,
        ArabicDiacritics.KASRA,
        ArabicDiacritics.TANWEEN_DAMMA,
        ArabicDiacritics.TANWEEN_FATHA,
        ArabicDiacritics.TANWEEN_KASRA
    }
}


ARABIC_LETTERS = frozenset({chr(x) for x in (list(range(0x0621, 0x63B)) + list(range(0x0641, 0x064B)))})
PUNCTUATIONS = frozenset({".", "،", ":", "؛", "-", "؟", "!"})
WORD_SEPARATOR = ' '
ALL_POSSIBLE_DIACRITICS = {m.value for m in ArabicDiacritics}
VALID_ARABIC_CHARS = {WORD_SEPARATOR, *ARABIC_LETTERS, *BASIC_DIACRITICS, *PUNCTUATIONS}
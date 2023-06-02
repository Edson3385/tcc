from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = ['booke', 'chemp', 'celender','berthday']
for word in misspelled:
    print("original word: "+ word)
    print("corrected word: "+ spell.correction(word))
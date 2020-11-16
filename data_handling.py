#%%
from lxml import etree
import pandas as pd
import xml.etree.ElementTree as ET

#%%
root = ET.parse("data/Words.xml").getroot()
languages = [lang.text for lang in root.iter('L')]
word_english = [lang.text for lang in root.iter('M')]
word_original = [lang.text for lang in root.iter('T')]
words = pd.DataFrame({
    "language" : languages, 
    "word" : word_english,
    "translation" : word_original
})

#%%
words[['family_1l', "family_2l", "language"]]  = words.language.str.split(".", expand=True)
words.head()

#%%
words.to_csv("data/words.csv", index=False)

#%%

root = etree.parse("data/Phonetics.xml")
c1 = root.xpath('/Phonetics/ConsonantEquivalence/Consonant/text()')
c2 = root.xpath('/Phonetics/ConsonantEquivalence/Equivalence/text()')
# points = [lang.text for lang in root.iter('M')]
points = root.xpath('/Phonetics/ConsonantEquivalence/Points/text()')
freq = root.xpath('/Phonetics/ConsonantEquivalence/Frequency/text()')
mean = root.xpath('/Phonetics/ConsonantEquivalence/Mean/text()')
var = root.xpath('/Phonetics/ConsonantEquivalence/Variance/text()')

sm = pd.DataFrame({
    "c1" : c1, 
    "c2" : c2,
    "points" : list(map(int, points)),
    "freq" : list(map(float, freq)),
    "mu" : list(map(float, mean)),
    "var" : list(map(float, var)),
})

sm.head()

#%%
sm.to_csv("data/phonetics.csv", index=False)
# %%

sm.loc[0]["points"]
# %%

from pkgbibliotheque.GestionPersonne_lu import *
from pkgbibliotheque.FoctionsFichier_lu import *

import csv
liste_doc = lire_Documents('abc.csv')

for x in liste_doc:
    print(x)

save_Documents('abcd.csv', liste_doc)
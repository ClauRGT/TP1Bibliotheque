from pkgbibliotheque.GestionPersonne_lu import *
from pkgbibliotheque.FoctionsFichier_lu import *
from pkgbibliotheque.GestionBiblio_lu import *

from datetime import datetime, timedelta
var = datetime.now().date()
print(var)
var2 = var + timedelta(days =15)
print(var2)

a= Emprunt('abs','aaa','bbb','2022-01-01','2022-02-01')
print(a)



liste= [1,2,3,4]
pos = liste.index(2)
 a= bool(False)
print(pos)
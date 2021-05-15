#!/usr/bin/env python
# coding: utf-8

# In[4]:


x = open ("odev.txt")
birinciListe = list()
ikinciListe=["=","+","?","-","(",")",]
for a in x :
    y = a.rstrip()
    birinciListe.append(y)
for any in birinciListe :
    temizHali = ""
    for i in range(len(any)):
        if any[i].isdigit():
            continue
        elif any[i] in ikinciListe :
            continue
        else:
            temizHali += any[i]
    temizHali += ""
    print(temizHali)


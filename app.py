"""Sei uno sviluppatore e devi creare una piccola applicazione Python che lavori con file di testo e gestirla correttamente con Git.
Fase 1 – Creazione applicazione 
Crea una cartella di progetto. 
- Crea un’app Python che: Legga un file chiamato input.txt 
- Conti quante righe contiene 
- Stampi a schermo il numero totale di righe
- Crea il file input.txt con del contenuto di esempio.
"""

with open("input.txt", "r")as f:
    righe = f.readlines()


print(len(righe))

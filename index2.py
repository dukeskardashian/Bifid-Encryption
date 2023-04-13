# Bifid-Entschlüsselung in Python

# Polybius-Quadrat definieren
polybius_quadrat = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'K'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']]

# Eingabeverschlüsselter Text
eingabeverschluesselt = "MWOBBHFRSHCIIIOUUKTXDCUQNVHUC"

# Funktion zur Entschlüsselung der Bifid-Verschlüsselung
def bifid_entschluesselung(verschluesselt, polybius_quadrat):
    # Umwandlung der verschlüsselten Zeichenkette in Koordinatenpaare
    koordinaten = []
    for buchstabe in verschluesselt:
        for i in range(len(polybius_quadrat)):
            if buchstabe in polybius_quadrat[i]:
                zeile = i + 1
                spalte = polybius_quadrat[i].index(buchstabe) + 1
                koordinaten.append((zeile, spalte))
    # Entfernen der Trennzeichen
    koordinaten = [i for pair in koordinaten for i in pair]
    # Aufteilen der Koordinaten in zwei Hälften
    halbe_laenge = len(koordinaten) // 2
    koordinaten_1 = koordinaten[:halbe_laenge]
    koordinaten_2 = koordinaten[halbe_laenge:]
    # Neuordnung der Koordinatenpaare
    neue_koordinaten = []
    for i in range(halbe_laenge):
        neue_koordinaten.append((koordinaten_1[i], koordinaten_2[i]))
    # Konvertierung der Koordinatenpaare zurück in Buchstaben
    entschluesselt = ""
    for paar in neue_koordinaten:
        zeile = paar[0] - 1
        spalte = paar[1] - 1
        buchstabe = polybius_quadrat[zeile][spalte]
        entschluesselt += buchstabe
    return entschluesselt

# Anwenden der Bifid-Entschlüsselung auf die Eingabezeichenkette
entschluesselt = bifid_entschluesselung(eingabeverschluesselt, polybius_quadrat)

# Ausgabe des entschlüsselten Textes
print("Entschlüsselter Text:", entschluesselt)

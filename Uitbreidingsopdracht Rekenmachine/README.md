Vooraleer aan deze opdracht te beginnen. Maak in de folder `4_LIJSTEN` een nieuwe map aan met de naam `Uitbreidingsopdracht`. In deze map moet je twee bestanden zetten. De eerste heet `rekenmachine.py`, de tweede `main.py`. Deze twee bestanden staan ook op deze GitHub pagina. Deze bezitten reeds een kleine hoeveelheid code waarmee je mag starten. Kopieer deze code naar de bestanden die jij zelf hebt aangemaakt.

# Opdracht-omschrijving
Leerlingen op de lagere school rangschikken rekenkundige problemen vaak verticaal om ze gemakkelijker op te lossen. Bijvoorbeeld, "235 + 52" wordt:

```
  235
+  52
-----

```

## De functie *rekenmachine*
Het doel van deze opdracht is om een functie met de naam *rekenmachine* te maken. Dit gebeurt in het bestand `rekenmachine.py`. Deze accepteert als eerste parameter een lijst van Strings. Deze lijst bevat een aantal rekenkundige problemen. De functie zal deze problemen verticaal en langs elkaar opstellen. 

### Een voorbeeld
Functie oproep:

```
rekenmachine(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Naast de lijst bezit de functie *rekenmachine* nog een tweede parameter, namelijk toon_oplossing. Deze heeft een standaard (default) waarde False. Wanneer deze naar True wordt gezet, toont de functie ook de oplossingen van de problemen. Let op! De parameter toon_oplossing is een Boolean, geen String.

### Een voorbeeld
Functie oproep:

```
rekenmachine(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Opmaak
Hou met volgende zaken rekening wanneer je de lijst converteert naar de output.
* Er moet een enkele spatie staan tussen de operator (+ of -) en de langste van de twee nummers, de operator staat op dezelfde regel als het tweede nummer, beide nummers staan in dezelfde volgorde als opgegeven (de eerste is de bovenste en de tweede de onderste.
* Nummers moeten rechts uitgelijnd zijn.
* Er moeten vier spaties tussen elk probleem staan.
* Er moeten streepjes onderaan elk probleem staan. De streepjes moeten over de hele lengte van elk probleem afzonderlijk lopen. (Het voorbeeld hierboven laat zien hoe dit eruit moet zien.)

## Foutmeldingen
Je moet bij het maken van de functie er ook mee rekening houden dat mensen een verkeerde input kunnen geven. Indien dit gebeurt moet de functie vroegtijdig stoppen. De functie **returnt** nu een **String** die de gebruiker aangeeft wat hij fout gedaan heeft.

Volgende situaties moeten leiden tot een foutmelding:
* Als er teveel rekenkundige problemen worden meegegeven. De limiet is **vijf**. Indien de lijst meer problemen bevat returnt dit tot de fout: ```Error: Te veel problemen```
* De functie *rekenmachine* kan enkel optellen en aftrekken. Het gebruikt hiervoor respectievelijk + en -. Indien een ander symbool in een probleem voorkomt returnt de functie: ```Error: Kan enkel optellen en aftrekken```
* Elk nummer mag enkel cijfers bevatten. Indien dit toch het geval is leidt dit tot: ```Error: Nummers mogen enkele cijfers bevatten```
* Elk nummer mag maximum uit **vier** cijfers bestaan. Anders returnt de functie: ```Error: Nummers mogen maximaal vier cijfers bevatten```

## Tips
Deze opdracht is niet eenvoudig. Hier alvast enkele tips om jullie op weg te helpen. Twijfel ook zeker niet om vragen te stellen.

De lijst bestaat uit een aantal Strings. Iedere String stelt een rekenkundig probleem voor. Het is mogelijk om deze String te splitsen (de functie hiervoor hebben jullie reeds gezien)

Omdat de problemen naast elkaar getoond worden is het niet mogelijk om ze een voor een te printen (dan zouden ze onder elkaar verschijnen). De output bestaat uit vier (of drie) regels. Sla iedere regel in een aparte variabele op en print deze variabelen op het einde van de functie.

**return** stopt het programma meteen. Zorg ervoor dat je op een logisch moment controleert of er een fout is. Ga bijvoorbeeld niet kijken of er meer dan vijf rekenkundige problemen zijn gegeven wanneer je deze al allemaal verwerkt hebt. Doe dit meteen als je de functie binnenkomt!

Maak gebruik van `main.py`. Deze geeft een aantal voorbeelden om te controleren of je goed bezig bent.
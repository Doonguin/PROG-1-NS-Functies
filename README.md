# PROG-1-NS-Functies
De NS heeft standaardtarieven voor treinreizen, maar onder sommige omstandigheden krijgen reizigers korting. Bijvoorbeeld omdat ze in een bepaalde leeftijdscategorie vallen. In deze opdracht maak je twee functies: ```standaardprijs(...)``` en ```ritprijs(...)```. De eerste functie bepaalt het standaardbedrag voor een bepaalde rit. De tweede functie maakt hier gebruik van, maar bepaalt zelf ook nog welke kortingen van toepassing zijn en levert als return-waarde de definitieve prijs.

## De functie standaardprijs:
Functie ```standaardprijs(afstandKM)``` heeft 1 parameter. Iedere treinrit kost 80 cent per kilometer, maar als de rit langer is dan 50 kilometer betaal je een vast bedrag van €15,- plus 60 cent per kilometer. Ga bij invoer van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

## De functie ritprijs:
De functie ```ritprijs(leeftijd, weekendrit, afstandKM)``` heeft 3 parameters. De parameter weekendrit is een boolean die aangeeft of de rit in het weekend plaats zal hebben (True) of niet (False). Het eerste wat de functie ```ritprijs(...)``` moet doen, is het aanroepen van de functie ```standaardprijs(...)```, waarbij de afstand in kilometers doorgegeven moet worden, om de standaardprijs voor de rit op te vragen. Aan de hand van de return-waarde kan de ritprijs worden berekend. De regels zijn als volgt:
- Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting.
- In het weekend reist deze groep met 35% korting.
- De overige leeftijdsgroepen betalen de gewone prijs, behalve in het weekend, dan reist deze leeftijdsgroep met 40% korting.

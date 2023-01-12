# nmea-serial

Utilitaire pour générer des trames NMEA à 1 Hz et les transmettre sur une liaison série.
Une sortie est correcte si elle commence par `$GPRMC`.

## Utilisation

Ouvrir le fichier python `nmea-serial.py`, changer les valeurs de `COM_PORT` et `COM_SPEED`.
Taper la commande suivante :
`python nmea-serial.py`

* Appuyer sur la touche `c` pour changer la sortie correcte ou incorrecte.
* Appuyer sur la touche `q` pour quitter.

## Installation

Taper la commande suivante dans le Terminal :

`pip install -r requirements.txt`
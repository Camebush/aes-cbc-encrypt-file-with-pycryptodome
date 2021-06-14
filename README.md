# aes-cbc-encrypt-file-with-pycryptodome
Ce script permet de chiffrer vos fichiers à l'aide du protocole **AES 256** avec le mode **CBC (Cipher block Chaining)**
Nous utilisons ici la librairie **Pycryptodome** pour l'implémentation du protocole AES

## Prérequis
*Installer la librairie pycryptodome*
>pip install pycryptodome

## Execution du script
Entrez la commande suivante pour le chiffrement
>python aes-encryption.py -eF "motdepasse" "chemin vers le fichier"

Entrez la commande suivante pour le déchiffrement
>python aes-encryption.py -dF "motdepasse" "chemin vers le fichier"

La vidéo ci-dessous vous explique en détails comment fonctionne le script et le **protocole AES**

**[Vidéo de présentation](https://youtu.be/CRfRyqLMfhw)**

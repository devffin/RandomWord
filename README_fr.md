# RandomWord 1.0.1

RandomWord est une petite application de bureau pour Windows qui affiche **un mot aléatoire à chaque lancement**. Cliquez sur **OK**, appuyez sur la touche **Entrée** ou **Échap**, ou fermez la fenêtre pour quitter. Relancez l'application pour obtenir un autre mot. Il est possible qu'un même mot soit tiré lors de lancements successifs.

## Exécution de l'application sous Windows

Extrayez l'intégralité du contenu de l'archive avant d'exécuter `RandomWord.exe`. Veillez à conserver le fichier `words.txt` à côté de l'exécutable, ainsi que le dossier `_internal` si vous utilisez le script de compilation fourni. L'application fonctionne même lorsqu'elle est lancée depuis un répertoire de travail différent (par exemple, via un raccourci).

## Exécution depuis le code source

Utilisez Python 3.9 (ou une version ultérieure) avec Tkinter installé :

```console
python main.py
```

Placez le fichier `words.txt` dans le même répertoire que `main.py`. Aucun paquet Python tiers n'est requis pour exécuter le code source. Sous Linux, il peut être nécessaire d'installer Tkinter séparément via le gestionnaire de paquets de votre distribution. L'application est conçue principalement pour Windows ; un accès à une interface graphique (bureau) est indispensable.

## Liste de mots

La liste est fournie sous forme de fichier texte externe encodé en UTF-8 (avec ou sans BOM), contenant une entrée par ligne. Les lignes vides sont ignorées et les espaces superflus sont supprimés. Si le fichier est absent, illisible, mal encodé ou vide, une boîte de dialogue d'erreur (en anglais) s'affiche, évitant ainsi une interruption brutale du programme due à une erreur de chargement de fichier.

La liste originale est conservée telle quelle : elle inclut des abréviations, des nombres, des noms propres et des termes composés avec trait d'union. Cette version n'applique aucun filtrage ni aucune déduplication des entrées. Chaque ligne non vide a une probabilité identique d'être sélectionnée.

## Compilation sous Windows

Installez Python 3.9 (ou une version ultérieure), en incluant Tkinter et le lanceur Python, puis exécutez le fichier `build_windows.bat` depuis le dossier contenant le code source extrait. Le script installe
PyInstaller dans un environnement virtuel local nommé `.build-venv` et génère :

```text
dist/RandomWord/
RandomWord.exe
words.txt
LICENSE
README.md
_internal/
```

Distribuez l'intégralité du dossier `dist/RandomWord`, par exemple sous forme d'archive ZIP.
Effectuez la construction (build) sous Windows pour générer un exécutable Windows. Le script nécessite un accès à Internet lors de la première exécution afin d'installer PyInstaller. Les dépendances nécessaires à la construction sont listées dans `requirements-build.txt` ; les versions effectivement installées sont consignées dans `dist/RandomWord/build-requirements.txt`.

## Tests

```console
python -m unittest discover -s tests -v
```

Les tests couvrent le chargement des mots, la gestion des chemins vers les ressources et la règle selon laquelle un seul mot est tiré à chaque lancement. Les tests de l'interface utilisateur (UI) utilisent des objets de substitution (doubles) ; ils ne vérifient donc ni le rendu sous Windows ni le résultat d'une véritable construction via PyInstaller. Avant de publier un exécutable Windows, vérifiez le comportement avec des mots longs, la mise à l'échelle de l'affichage, les raccourcis utilisant un répertoire de travail différent, les boîtes de dialogue d'erreur, ainsi que toutes les méthodes de fermeture de l'application.

## Crédits pour la liste de mots

Ce projet a pu voir le jour grâce aux projets de listes de mots suivants :

- [devffin/LeMotDuJour](https://github.com/devffin/LeMotDuJour)
- [Taknok/French-Wordlist](https://github.com/Taknok/French-Wordlist)

## Notater
Min samling notater i fag ved NTNU.
For mer info og kompilerte pdf-er: [haved.no/notater](https://haved.no/notater)

#### Kompilering
Alle notatene er skrevet i latex, og bruker en god del pakker.
Utover det er det vanlig latex, kompilert med `latexmk`.
De kompileres av GitHub workflow i et docker-bilde med texlive-full.

For å kompilere selv kan du kjøre
``` bash
./build ls # Printer ut mulige pdf-er
./build latex matte3.pdf
```
Output legges i mappen `publish/`. Kompilerte pdf-er legges i `publish/notater`.








# My Zootopia - Tier-Webseiten-Generator

Dieses Projekt ist ein Python-Skript, das dynamisch eine Webseite mit Informationen über Tiere generiert. Der Benutzer wird aufgefordert, einen Tiernamen einzugeben, woraufhin das Skript Daten von der [API-Ninjas Animals API](https://api-ninjas.com/api/animals) abruft und eine `animals.html`-Datei mit den Ergebnissen erstellt.

Das Projekt ist modular aufgebaut und trennt die Datenbeschaffung (`data_fetcher.py`) von der Logik zur Webseitenerstellung (`animals_web_generator.py`).

## Setup & Installation

Um dieses Projekt lokal auszuführen, folgen Sie bitte diesen Schritten.

**1. Klonen Sie das Repository**

```shell
git clone https://github.com/shokeijin/My-Zootopia.git
cd My-Zootopia
```

**2. Installieren Sie die Abhängigkeiten**

Das Projekt verwendet externe Python-Pakete, die in der `requirements.txt`-Datei aufgelistet sind. Installieren Sie diese mit `pip`:

```shell
pip install -r requirements.txt
```

**3. Konfigurieren Sie den API-Schlüssel**

Das Skript benötigt einen gültigen API-Schlüssel von API-Ninjas, um zu funktionieren.

*   Erstellen Sie eine neue Datei im Hauptverzeichnis des Projekts mit dem Namen `.env`.
*   Fügen Sie Ihren persönlichen API-Schlüssel in diese Datei im folgenden Format ein:

    ```
    API_KEY="HIER_IHREN_PERSÖNLICHEN_API_SCHLÜSSEL_EINFÜGEN"
    ```

## Verwendung

Führen Sie das Hauptskript über Ihr Terminal aus:

```shell
python animals_web_generator.py
```

Das Skript wird Sie dann auffordern, den Namen eines Tieres einzugeben. Nach der erfolgreichen Ausführung wird eine neue Datei mit dem Namen `animals.html` im Projektverzeichnis erstellt. Wenn das angefragte Tier nicht gefunden wird, enthält die HTML-Datei eine entsprechende Benachrichtigung.

## Beitragende

Beiträge sind herzlich willkommen! Wenn Sie Ideen für Verbesserungen haben oder einen Fehler finden, zögern Sie bitte nicht, ein "Issue" zu öffnen oder einen "Pull Request" zu stellen.
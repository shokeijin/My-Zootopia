import json


def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


# --- Schritt 1: Inhalt der Vorlage lesen ---
with open("animals_template.html", "r", encoding="utf-8") as file:
    template_content = file.read()

# Lade die Tierdaten aus der JSON-Datei
animals_data = load_data('animals_data.json')

# --- Schritt 2: Einen HTML-String mit dem finalen Design erzeugen ---
animals_html_string = ""

# Iteriere durch jedes Tier in der Liste
for animal in animals_data:
    # Beginne das Listenelement
    animals_html_string += '    <li class="cards__item">\n'

    # Füge den Titel in einem <div> hinzu, falls vorhanden
    if "name" in animal:
        animals_html_string += f'      <div class="card__title">{animal["name"]}</div>\n'

    # Beginne den Text-Paragraphen
    animals_html_string += '      <p class="card__text">\n'

    # Füge die Details hinzu, mit <strong> für die Labels
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_html_string += f'        <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        animals_html_string += f'        <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_html_string += f'        <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    # Schließe den Text-Paragraphen
    animals_html_string += '      </p>\n'

    # Schließe das Listenelement
    animals_html_string += '    </li>\n'

# --- Schritt 3: Platzhalter durch den erzeugten HTML-String ersetzen ---
final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html_string)

# --- Schritt 4: Den neuen HTML-Inhalt in eine Datei schreiben ---
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(final_html)

print("Die finale 'animals.html' wurde erfolgreich erstellt!")
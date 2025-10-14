import json


def load_data(file_path):
    """ Lädt eine JSON-Datei """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


# --- Schritt 1: Inhalt der Vorlage lesen ---
with open("animals_template.html", "r", encoding="utf-8") as file:
    template_content = file.read()

# Lade die Tierdaten aus deiner JSON-Datei
animals_data = load_data('animals_data.json')

# --- Schritt 2: Einen String mit den Tierdaten erzeugen ---
animals_info_string = ""

# Iteriere durch jedes Tier in der Liste
for animal in animals_data:
    # Füge den Namen hinzu, falls vorhanden
    if "name" in animal:
        animals_info_string += f"Name: {animal['name']}\n"

    # Füge die Diät hinzu, falls vorhanden
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_info_string += f"Diet: {animal['characteristics']['diet']}\n"

    # Füge den ersten Ort hinzu, falls vorhanden
    if "locations" in animal and animal["locations"]:
        animals_info_string += f"Location: {animal['locations'][0]}\n"

    # Füge den Typ hinzu, falls vorhanden
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_info_string += f"Type: {animal['characteristics']['type']}\n"

    # Füge eine zusätzliche Leerzeile nach jedem Tier hinzu
    animals_info_string += "\n"

# --- Schritt 3: Platzhalter durch den erzeugten String ersetzen ---
final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

# --- Schritt 4: Den neuen HTML-Inhalt in eine Datei schreiben ---
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(final_html)

print("Die Datei 'animals.html' wurde erfolgreich erstellt!")
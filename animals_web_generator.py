import json


def load_data(file_path):
    """
    Lädt Tierdaten aus einer JSON-Datei.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_unique_skin_types(animals_data):
    """
    Extrahiert eine sortierte Liste von einzigartigen skin_type-Werten.
    """
    skin_types = set()
    for animal in animals_data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return sorted(list(skin_types))


def serialize_animal(animal):
    """
    Wandelt ein einzelnes Tier-Objekt in einen formatierten HTML-String um.
    """
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})

    html_string = '    <li class="cards__item">\n'
    if "name" in animal:
        html_string += f'      <h2 class="card__title">{animal["name"]}</h2>\n'
    if "scientific_name" in taxonomy:
        html_string += f'      <span class="card__scientific-name">{taxonomy["scientific_name"]}</span>\n'

    html_string += '      <div class="card__details">\n        <ul>\n'
    if "diet" in characteristics:
        html_string += f'          <li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if "locations" in animal and animal["locations"]:
        html_string += f'          <li><strong>Location:</strong> {animal["locations"][0]}</li>\n'
    if "lifespan" in characteristics:
        html_string += f'          <li><strong>Lifespan:</strong> {characteristics["lifespan"]}</li>\n'
    if "type" in characteristics:
        html_string += f'          <li><strong>Type:</strong> {characteristics["type"]}</li>\n'
    html_string += '        </ul>\n      </div>\n'

    if "slogan" in characteristics:
        html_string += f'      <p class="card__slogan">{characteristics["slogan"]}</p>\n'
    html_string += '    </li>'

    return html_string


def main():
    """
    Hauptfunktion: Zeigt dem Benutzer eine Auswahl an skin_type-Werten,
    filtert die Daten entsprechend und generiert die Webseite.
    """
    animals_data = load_data('animals_data.json')
    unique_types = get_unique_skin_types(animals_data)

    print("Bitte wählen Sie einen Hauttyp (skin_type) aus der Liste:")
    for i, skin_type in enumerate(unique_types):
        print(f"  {i + 1}: {skin_type}")

    try:
        # --- HIER IST DIE KORREKTUR ---
        # Der Backslash vor "Geben" wurde entfernt.
        choice_index = int(input("Geben Sie die Nummer Ihrer Wahl ein: ")) - 1

        if not 0 <= choice_index < len(unique_types):
            print("\nFehler: Ungültige Nummer. Bitte starten Sie das Skript erneut.")
            return
        selected_skin_type = unique_types[choice_index]
    except ValueError:
        print("\nFehler: Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        return

    print(f"\nFiltere nach Tieren mit dem Hauttyp: '{selected_skin_type}'...")

    filtered_animals = [
        animal for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type") == selected_skin_type
    ]

    if not filtered_animals:
        print("Keine Tiere mit diesem Hauttyp gefunden. Es wird keine Webseite erstellt.")
        return

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_content = file.read()

    all_animals_html = [serialize_animal(animal) for animal in filtered_animals]
    animals_html_block = "\n".join(all_animals_html)

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html_block)

    output_filename = f"animals_{selected_skin_type.lower().replace(' ', '_')}.html"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(final_html)

    print(f"Erfolg! Die Datei '{output_filename}' wurde mit {len(filtered_animals)} Tier(en) erstellt.")


if __name__ == "__main__":
    main()
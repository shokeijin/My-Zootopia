import data_fetcher  # NEU: Importiert unser neues Modul

# Die Funktion 'get_animals_data' wurde entfernt.

def serialize_animal(animal):
    """
    Wandelt ein einzelnes Tier-Objekt in einen formatierten HTML-String um.
    (Diese Funktion bleibt unverändert)
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
    Hauptfunktion: Fragt den Benutzer nach einem Tiernamen, ruft die Daten über den
    data_fetcher ab und generiert eine entsprechende Webseite.
    """
    animal_name = input("Geben Sie den Namen eines Tieres ein: ")
    if not animal_name:
        print("Es wurde kein Tiername eingegeben.")
        return

    # --- GEÄNDERT: Ruft die Daten jetzt aus dem data_fetcher-Modul ab ---
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data is None:
        print("Die Webseite konnte nicht erstellt werden.")
        return

    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_content = file.read()

    output_filename = "animals.html"

    if not animals_data:
        error_message = f'<h2>Das Tier "{animal_name}" existiert nicht.</h2>'
        final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", error_message)
        print(
            f'Das Tier "{animal_name}" wurde nicht gefunden. Eine entsprechende Nachricht wird in der HTML-Datei angezeigt.')
    else:
        all_animals_html = [serialize_animal(animal) for animal in animals_data]
        animals_html_block = "\n".join(all_animals_html)
        final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html_block)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(final_html)

    print(f"Erfolg! Die Webseite wurde erfolgreich in der Datei '{output_filename}' generiert.")


if __name__ == "__main__":
    main()
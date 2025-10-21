import os
import requests
from dotenv import load_dotenv

# Lädt die Umgebungsvariablen aus der .env-Datei.
# Das Skript sucht automatisch nach einer .env-Datei im selben Verzeichnis.
load_dotenv()

def fetch_data(animal_name):
  """
  Ruft Tierdaten für den Tiernamen 'animal_name' von der API-Ninjas API ab.
  """
  # Holt den API-Schlüssel sicher aus den Umgebungsvariablen.
  # os.environ.get() ist die Methode, um auf die geladenen Variablen zuzugreifen.
  api_key = os.environ.get("API_KEY")

  if not api_key:
      print("Fehler: API_KEY nicht in der .env-Datei gefunden oder die Datei fehlt.")
      print("Bitte erstellen Sie eine .env-Datei mit dem Inhalt: API_KEY=\"IHR_SCHLÜSSEL\"")
      return None

  api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  headers = {"X-Api-Key": api_key}

  try:
      response = requests.get(api_url, headers=headers)
      response.raise_for_status()
      return response.json()
  except requests.exceptions.RequestException as e:
      print(f"Fehler bei der API-Anfrage: {e}")
      if 'response' in locals() and response is not None:
          print(f"Server-Antwort: {response.text}")
      return None
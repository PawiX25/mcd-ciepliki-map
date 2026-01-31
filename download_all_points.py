import urllib.request
import os

BASE_URL = "https://cdn.mcdonalds.pl/drwal2025/points/points_{}.csv"

print("Rozpoczynam pobieranie plików CSV (1-4)...")

for i in range(1, 5):
    url = BASE_URL.format(i)
    filename = f"points_{i}.csv"
    print(f"Pobieranie: {url} ...", end=" ", flush=True)
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                content = response.read()
                with open(filename, 'wb') as f:
                    f.write(content)
                print(f"Zapisano {filename}")
            
    except urllib.error.HTTPError as e:
        print(f"Błąd HTTP: {e.code}")
    except Exception as e:
        print(f"Błąd: {e}")
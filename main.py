import os

def scal_plik_wejscie_do_jednego():
    folder_pytania = os.path.join(os.getcwd(), "input")  # ./pytania/
    plik_wyjsciowy = "output.txt"

    with open(plik_wyjsciowy, "w", encoding="utf-8") as output_file:
        for i in range(1, 580):  # od 001.txt do 579.txt
            nazwa_pliku = f"{i:03}.txt"
            sciezka_pliku = os.path.join(folder_pytania, nazwa_pliku)
            try:
                with open(sciezka_pliku, "r", encoding="utf-8") as input_file:
                    zawartosc = input_file.read()
                    output_file.write(zawartosc)
                    output_file.write("\n")  # dodaj pustą linię między plikami
                print(f"✅ Added: {nazwa_pliku}")
            except FileNotFoundError:
                print(f"⚠️ Plik {nazwa_pliku} Doesn`t exist – skip.")
            except Exception as e:
                print(f"❌ Error {nazwa_pliku}: {e}")

if __name__ == "__main__":
    scal_plik_wejscie_do_jednego()

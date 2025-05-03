import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Nomi delle cartelle predefiniti
DEFAULT_FOLDER_NAMES = [
    "RIPRESE",
    "PROGETTO",
    "MUSICA",
    "AUDIO",
    "FX",
    "GRAFICA",
    "ANIMAZIONI",
    "MATERIALE CLIENTE",
    "EXPORT"
]

def create_folders():
    # Recupera il percorso selezionato
    directory = folder_path.get()
    if not directory:
        messagebox.showwarning("Attenzione", "Seleziona una cartella di destinazione!")
        return
    
    # Recupera il codice progetto (se esiste)
    project_code = project_code_entry.get().strip()
    if project_code:
        project_code = f"{project_code}_"

    # Creazione delle cartelle
    created, skipped = 0, 0
    for folder_name in DEFAULT_FOLDER_NAMES:
        full_folder_name = f"{project_code}{folder_name}"
        folder = os.path.join(directory, full_folder_name)
        try:
            os.makedirs(folder, exist_ok=False)
            created += 1
        except FileExistsError:
            skipped += 1
    
    # Mostra un messaggio con il risultato
    messagebox.showinfo(
        "Completato",
        f"Cartelle create: {created}\nCartelle già esistenti: {skipped}"
    )

def select_directory():
    # Apri il selettore di cartelle
    folder = filedialog.askdirectory()
    folder_path.set(folder)

# Configurazione interfaccia grafica
root = tk.Tk()
root.title("Creazione Cartelle Progetto")

# Variabile per il percorso della cartella
folder_path = tk.StringVar()

# Label e campo per selezionare la cartella di destinazione
tk.Label(root, text="Seleziona cartella di destinazione:").pack(pady=5)
folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)
tk.Entry(folder_frame, textvariable=folder_path, width=50).pack(side=tk.LEFT, padx=5)
tk.Button(folder_frame, text="Sfoglia", command=select_directory).pack(side=tk.LEFT, padx=5)

# Campo per inserire il codice progetto
tk.Label(root, text="Codice Progetto (facoltativo):").pack(pady=5)
project_code_entry = tk.Entry(root, width=50)
project_code_entry.pack(pady=5)

# Bottone per creare le cartelle
tk.Button(root, text="Crea Cartelle", command=create_folders).pack(pady=20)

# Avvio dell'interfaccia grafica
root.mainloop()

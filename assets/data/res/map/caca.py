from pathlib import Path

folder = Path.cwd()

count = 0

for txt_file in folder.rglob("*.txt"):
    txt_file.unlink()
    print(f"Supprimé : {txt_file.relative_to(folder)}")
    count += 1

print(f"\n{count} fichier(s) .txt supprimé(s).")
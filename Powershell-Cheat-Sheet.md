# PowerShell Cheat Sheet

## Dateien und Verzeichnisse
- **`Get-ChildItem` (alias `ls`, `dir`)**: Listet Dateien und Ordner auf.
  ```powershell
  Get-ChildItem -Path C:\Users\Username
  ```
  
- **`New-Item`**: Erstellt Dateien oder Verzeichnisse.
  ```powershell
  New-Item -Path C:\Temp\newfile.txt -ItemType File
  ```

- **`Remove-Item` (alias `del`, `rm`)**: Löscht Dateien oder Verzeichnisse.
  ```powershell
  Remove-Item -Path C:\Temp\newfile.txt
  ```
  
- **`Copy-Item` (alias `cp`)**: Kopiert Dateien oder Verzeichnisse.
  ```powershell
  Copy-Item -Path C:\Temp\file.txt -Destination C:\Backup
  ```

- **`Move-Item` (alias `mv`)**: Verschiebt Dateien oder Verzeichnisse.
  ```powershell
  Move-Item -Path C:\Temp\file.txt -Destination C:\Backup
  ```

- **`Rename-Item`**: Benennt Dateien oder Verzeichnisse um.
  ```powershell
  Rename-Item -Path C:\Temp\file.txt -NewName newfile.txt
  ```
### Navigation

- **`Get-Location` (alias `pwd`)**: Zeigt den aktuellen Pfad an.

- **`Set-Location` (alias `cd`)**: Wechselt das Verzeichnis.
  ```powershell
  Set-Location C:\Users\Username
  ```
### Informationen und Inhalte

- **`Get-Content` (alias `cat`, `type`)**: Zeigt den Inhalt einer Datei an.
  ```powershell
  Get-Content -Path C:\Temp\file.txt
  ```
- **`Set-Content`**: Überschreibt den Inhalt einer Datei.
  ```powershell
  Set-Content -Path C:\Temp\file.txt -Value "Neuer Inhalt"
  ```
- **`Add-Content`**: Fügt Text zu einer Datei hinzu.
  ```powershell
  Add-Content -Path C:\Temp\file.txt -Value "Zusätzlicher Inhalt"
  ```

- **`Get-Help`**: Zeigt Hilfe zu einem Befehl an.
  ```powershell
  Get-Help Get-Process
  ```
- **`Update-Help`**: Aktualisiert die Hilfedateien.
  ```powershell
  Update-Help
  
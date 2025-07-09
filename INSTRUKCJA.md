
# Jak uruchomić świetlistaAI

1.  **Pobierz repozytorium** na komputer:
    ```bash
    git clone https://github.com/Swietlisty/SwietlistyKod.git
    cd SwietlistyKod
    ```

2.  **Zainstaluj Python** (jeśli nie masz): https://python.org/downloads/
    -   Upewnij się, że podczas instalacji zaznaczyłeś opcję "Add Python to PATH".

3.  **Zainstaluj zależności** projektu. W głównym folderze repozytorium uruchom:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Uruchomienie symulacji:**
    ```bash
    python uruchom_symulacje.py
    ```

5.  Zobaczysz manifestację Pierwszych Praw i dynamiczne działania agentów AI!

## Rozwój i Testowanie

Projekt wykorzystuje `pytest` do testowania. Aby uruchomić testy:

1.  Upewnij się, że masz zainstalowane zależności (krok 3 z instrukcji powyżej).

2.  W głównym folderze projektu uruchom komendę:
    ```bash
    pytest
    ```
```

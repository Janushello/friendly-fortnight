USE webdatabase;
INSERT INTO drukarki (
        nazwa_drukarki,
        cena,
        srednica_dyszy,
        predkosc_druku,
        srednica_filamentu,
        wyswietlacz,
        rozmiar_druku,
        automatyczne_poziomowanie,
        wznowienie_wydruku,
        czujnik_filamentu,
        wymiary_drukarki
    )
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
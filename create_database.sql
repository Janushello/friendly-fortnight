USE webdatabase;
CREATE TABLE drukarki (
    ID INT IDENTITY(1,1) primary key,
    nazwa_drukarki VARCHAR(50),
    cena DECIMAL(8, 2),
    srednica_dyszy DECIMAL(8, 4),
    predkosc_druku SMALLINT,
    srednica_filamentu DECIMAL(8, 4),
    wyswietlacz VARCHAR(10),
    rozmiar_druku VARCHAR(12),
    automatyczne_poziomowanie BIT,
    wznowienie_wydruku BIT,
    czujnik_filamentu BIT,
    wymiary_drukarki VARCHAR(12)
);
CREATE TABLE filamenty(
    ID INT IDENTITY(1,1) primary key,
    rodzaj_filamentu VARCHAR(20)
);
CREATE TABLE komunikacje(
    ID INT IDENTITY (1,1) primary key,
    typ_komunikacji VARCHAR(11)
);
CREATE TABLE drukarki_filamenty(
    ID INT IDENTITY(1,1) primary key,
    ID_filamentu int,
    ID_drukarki int,
    foreign key(ID_filamentu) references filamenty(ID),
    foreign key(ID_drukarki) references drukarki(ID)
);
CREATE TABLE drukarki_komunikacje(
    ID INT IDENTITY(1,1) primary key,
    ID_komunikacji INT,
    ID_drukarki INT,
    foreign key(ID_komunikacji) references komunikacje(ID),
    foreign key(ID_drukarki) references drukarki(ID)
);

INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('ABS');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PETG');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Nylon');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('TPU');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PVA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('HIPS');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PC');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('ASA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PP');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PMMA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('TPE');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PC-ABS');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('PP-GF');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Wood PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Metal PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Fluorescent PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Flex PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Carbon Fiber PLA');
INSERT INTO filamenty (rodzaj_filamentu) VALUES ('Conductive PLA');
INSERT INTO komunikacje (typ_komunikacji) VALUES ('Wi-Fi');
INSERT INTO komunikacje (typ_komunikacji) VALUES ('Karta SD');
INSERT INTO komunikacje (typ_komunikacji) VALUES ('USB');
INSERT INTO komunikacje (typ_komunikacji) VALUES ('Ethernet');
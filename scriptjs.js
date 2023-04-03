window.addEventListener('load', function () {
    const navbar = document.querySelector('.navbar');
    const aside = document.querySelector('aside');

    function showNavbar() {
        navbar.classList.add('active');
        aside.style.paddingLeft = '220px';
    }

    function hideNavbar() {
        aside.style.paddingLeft = '100px';
        navbar.classList.remove('active');
    }

    aside.addEventListener('mouseover', (event) => {
        const x = event.clientX;
        if (x <= 100 && x > 0) {
            showNavbar();
        }
    });
    navbar.addEventListener('mouseleave', () => {
        hideNavbar();
    });
    document.getElementById("myButton").addEventListener("click", function () {
        //response zawiera informacje o bazie danych w formacie json
        //dodaj tabelkę z informacjami z bazy danych
        $.ajax({
            url: "/data.json",
            type: "GET",
            success: function (response) {
                console.log(response);
                var aside = document.querySelector("aside");
                const kolumny = ["id",
                    "nazwa",
                    "cena",
                    "predkosc_druku",
                    "rozmiar_druku",
                    "srednica_dyszy",
                    "srednica_filamentu",
                    "wymiary_drukarki",
                    "wyswietlacz",
                    "czujnik_filamentu",
                    "automatyczne_poziomowanie",
                    "wznowienie_wydruku"]
                const dlugoscTablicy = kolumny.length;
                var table = document.createElement("table");
                table.style.width = '100%';
                table.setAttribute('border', '1');
                var tbody = document.createElement("tbody");
                const products = response.data;
                var tr = document.createElement('tr');
                for (var i = 0;i<dlugoscTablicy;i++){
                        const td = document.createElement('td');
                        td.appendChild(document.createTextNode(kolumny[i]));
                        tr.appendChild(td);
                        
                }
                tbody.appendChild(tr);
                table.appendChild(tbody);
                aside.appendChild(table);
                products.forEach((product) => {
                    var tr = document.createElement('tr');
                    for (var i = 0;i<dlugoscTablicy;i++){
                        const td = document.createElement('td');
                        td.appendChild(document.createTextNode(product[kolumny[i]]));
                        tr.appendChild(td);
                    }
                    tbody.appendChild(tr);
                });
                table.appendChild(tbody);
                aside.appendChild(table);
            }
        });
    });
});


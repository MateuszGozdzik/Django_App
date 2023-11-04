# Django App

## [VISIT](https://web-production-7a75.up.railway.app/)

Użytkownik **staff** z hasłem **zaq1@WSX** z możliwością wglądu wszystkich danych. Także [panelu admina](https://web-production-7a75.up.railway.app/admin).

Mój pierwszy większy projekt w Django.
Hostowany na stronie [Railway](https://railway.app/).

Dużo funkcji nie jest dokończonych (między innymi cały front jest na absolutnym minimum), jest możliwość wystąpnienia jeszcze błędów, traktowałem to bardziej jako projekt do nauki i testowania funkcji niż pełnoprawną aplikację.

## Funkcje:

1. System Logowania Użytkowników, możliwość przywracania hasła za pomocą email
   ![Obraz z logowania](readme-images/image.png)
   - Dla każdego użytkownika jest tworzony awatar, jest możliwość zmiany danych
     ![Alt text](readme-images/image-8.png)
   - Możliwość dodania innego użytkownika (ustawionego jako publiczny) do znajomych, dostanie on wtedy powiadomienie
     ![Alt text](readme-images/image-9.png)
1. Wyświetlanie zdjęć:
   - [kotów](https://thecatapi.com/) i [psów](https://dog.ceo/dog-api/) za pomocą API
     ![Obraz Kotka](readme-images/image-1.png)
   - Wyłączona funkcja wyświetlania zdjęć z folderu z Google Drive
     ![Zakomentowy kod dla wyświetlania zdjęc z google drive](readme-images/image-2.png)
1. System cytatów
   - Można przeglądać cytaty dodane przez admina, dodane przez innych użytkowników (wymagane jest zatwierdzenie ich przez admina), oraz dodanych przez siebie samego.
     ![strona z cytatami](readme-images/image-3.png)
   - Możliwość sortowania cytatów przez tytuł, tekst, autora (regex), wybór języka, filtrowanie ulubionych i dodanych przez obecnego użytkownika. Jest też moliwe wyświetlenie losowego cytatu, bez żadnych filtrów.
     ![Filtrowanie cytatów](readme-images/image-4.png)
   - Możliwość dodania cytatu za pomocą edytora [tinymce](https://www.tiny.cloud/)
     ![Dodanie cytatu](readme-images/image-5.png)
   - W przypadku zaznaczenia cytatów jako publiczny zostanie wysłane powiadomienie do admina z uprawnieniami zatwierdzania.
     ![Powiadomienie dla admina o nowym cytacie](readme-images/image-6.png)
     ![Możliwość zatwierdzenia cytatu przez admina](readme-images/image-7.png)
1. System powiadomien (pokazany w poprzednich punktach)
   - jest możliwość wysyłania powiadomień w emailu
     ![Alt text](readme-images/image-10.png)
     ![Alt text](readme-images/image-11.png)

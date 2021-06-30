# Instrukcja budowania i uruchamiania REST API
Projekt został wykonany w języku Python z użyciem frameworku Flask. Aplikacja zawiera 6 endpointów i funkcji umożliwiających komunikację z serwerem. Podczas tworzenia projektu wykorzystano 3 metody, odpowiednio: GET, POST, DELETE. Testowanie endpointów odbywa się poprzez REST Client w Visual Studio Code.
1.	Pierwszy endpoint wraz z funkcją get_words() umożliwia wyświetlanie wszystkich słów z kolekcji. Wykorzystuje metodę GET.
2.	Kolejno funkcja get_word() umożliwia wyświetlenie słowa o podanym indexie i również zastosowano metodę GET.
3.	Następny endpoint wraz z funkcją create_word() pozwala na dodawanie nowych słów do kolekcji i wykorzystuje metodę POST.
4.	Wykorzystano także metodę DELETE i funkcję delete_word() w celu usunięcia wybranego słowa o danym indexie.
5.	Aplikacja umożliwia również sprawdzenie liczby wystąpień danego słowa w kolekcji. W tym celu wykorzystano funkcję get_amount() i metodę GET.
6.	Ostatni endpoint wraz z funkcją get_unique_words() umożliwia wyświetlenie wszystkich unikalnych słów z kolekcji. W tym przypadku również wykorzystano metodę GET.

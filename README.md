# Simple REST API
This project allows adding, removing and displaying all or unique words from collection. It also gives possibility to check number of occurrences of given word in collection. The project contains 6 endpoints and functions to communicate with the server. During the development of the project, 3 methods were used, respectively: GET, POST, DELETE. Testing of the endpoints is done via REST Client using HTTP protocol.

## Endpoints
1. The first endpoint with get_words() function allows to display all the words in the collection. It uses the GET method.
2. Next endpoint with get_word() function enables to display the word with given index and also GET method has been used.
3. Endpoint with create_word() function allows adding new words to the collection. It uses POST method.
4. DELETE method and delete_word() function was used to delete the selected word with given index.
5. The application also allows to check the number of occurrences of a given word in the collection. The get_amount() function and the GET method were used for this purpose.
6. Last endpoint with get_unique_words() function allows to display all unique words from the collection. In this case also GET method was used.

## Used Technologies 
- Language: Python
- Libraries: flask, numpy

# A demo of the Python Module "connexion"
This demo was made to show a colleague how the
[Zalando-made connexion-module](https://connexion.readthedocs.io/en/latest/) enables protyping an API very, very,
_very_ simple. I'm sure there are several similar tools for both Python and other languages out there, but I was very
impressed when I stumbled upon connexion during my "trying to learn more Python"-summer of code. And I managed to make
the demo within reasonable time, which really says a lot about how easy it is :-)

The demo contains six "levels" of an API and its documentation. In the first part it is only about getting the
Swagger-UI for your API up and running, and then gradually adding functionality to the API.

To run the demo, you (obviously) need to have the connexion-module
[installed](https://connexion.readthedocs.io/en/latest/quickstart.html#installing-it):

```commandline
pip install connexion[swagger-ui]
```

To run the demo:
```commandline
python main.py
```
Then, go to http://localhost:8080/ui/ for the Swagger-UI of the API, and http://localhost:8080/bikes for the API-itself. 

In the file main.py there are six lines starting with ```app.add_api()``` of which five are commented out. Each of these
lines creates an API based on the OpenAPI Specification file given as parameter. 

There are six different OAS-files (.yaml). Each yaml-file adds more functionality to
the API. The first one, connexion-demo1.yaml, only has a get that does nothing. Then functionality, validation etc is
added in the other '.yaml'-files. In the last one, connexion-demo5.yaml, there is both a get and a post, and validation
of both input and output.

To see the different APIs, just comment out the uncommented-line, and un-comment the one you would like to look at, save
the file and the server will reload. Remember to refresh your browser to see the changes.

In each '.yaml'-file with the API-specifications, the operations have an "operationId" which corresponds to the name of 
a python-function in a .py-file. As you will see, there is no validation or transformation of input and output-data in
these functions. The functions use standard Python datastructures, and the connexion module does all the magic of
handling the transformation between these and JSON. I also handles validation and ensures meaningful error-messages
if the API-is created with either of these parameters (in main.py when calling add.api())
```python
strict_validation=True
validate_responses=True
```
Try for instance to give a bike a score higher than 10 when running the API connexion-demo5.yaml.
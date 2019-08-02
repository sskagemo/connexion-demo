"""
A demonstration of connexion and "Swagger first" (i.e. "OAS first")
Part 1: Running the API with documentation through swagger-ui and an empty GET-operation
Part 2: Adding a response to the GET-operation
Part 3: Adding specification of schema
Part 3-fail: Fails when respons does not comply with schema
Part 4: Adding a POST-operation
Part 5: Adding validation of POST-input
"""
import connexion

app = connexion.App(__name__)

# Uncomment relevant line for the different stage of the demo.
# NB! Only one of the lines can be uncommented - or else you will get an error when starting the app
app.add_api('connexion-demo1.yaml')
#app.add_api('connexion-demo2.yaml')
#app.add_api('connexion-demo3.yaml')
#app.add_api('connexion-demo3-fail.yaml', validate_responses=True)
#app.add_api('connexion-demo4.yaml')
#app.add_api('connexion-demo5.yaml', strict_validation=True, validate_responses=True)


application = app.app


if __name__ == '__main__':
    app.run(port=8080, debug=True)


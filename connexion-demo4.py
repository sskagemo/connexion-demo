"""Defining the methods as listed in connexion-demo4.yaml"""

data = { 'landeveissykkel': 5,
         'cyclo-cross': 6,
         'christiania-sykkel': 7,
         'long-tail': 8,
         'Tern HSD': 9,
         }

def get_data():
    return data

def post_data(body):
    if body['bike'] in data.keys():
        return "The URL is already registered", 409
    else:
        data.update({ body['bike']: body['score']})
        return "You've added: {}".format(body), 201


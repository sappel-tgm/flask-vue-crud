## Report File for Testverbesserung-Appel Flask-Vue-Crud + Flask-Vue-Spa

#### Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren?
```app.run(host='127.0.0.1', port=80)```

#### Implementieren Sie eine TODO-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
-> Books mit Todos ersetzen  
-> Book zu Todo  
Nicht benötigte FUnktionen entfernen (Charge)  
JSON Struktur umstellen auf:  
```
'id': uuid.uuid4().hex,
'todo': 'On the Road2',
'assignee': 'Jack Kerouac2',
'done': True
```


#### Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
Books.vue zu Todos.vue renamen  
-> In JS, das neue File importieren
Route ändern:  
```path: '/',
   name: 'Todos',
   component: Todos,
```

#### Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen.
Damit das möglich ist muss man nichts ändern.  
Für personenbezogene TODO's kann man einfach nach der Zuweisung filtern.  

#### Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!
Authentifizierung einerseits mit Flask: Flask-HTTPAuth, Token Based Authentication  
[https://blog.miguelgrinberg.com/post/restful-authentication-with-flask](Flask-Auth)  
Außerdem Authentifizierung mit Vue: Login functions, mit Username+Password labels  
[https://blog.sqreen.io/authentication-best-practices-vue/](Vue-Auth)  

#### Implementieren Sie einen Client in Python, der sich mit der vorhandenen Server-Einheit verbindet und die Daten in eine eigene JSON Struktur lädt.
```
if __name__ == "__main__":
    getInput = requests.get("http://localhost:8080/ping")
    data = json.loads(getInput.text)
    if data != None:
      print(data)
    else:
      print("Data Null")
```
#### Was würden Sie bei der Server-API anders definieren, damit verschiedene Clients auf die angebotenenen Funktionen zugreifen könnten?
Der Rest-Teil ist von überall zugänglich.  
Jedoch braucht es ein Resource Sharing Modul (CORS), damit andere CLient Cross-Origin-Requests durchführen können.  
[CORS](https://flask-cors.readthedocs.io/en/latest/)

### Teil 2
#### Welche Tools würden Sie einsetzen, und wie würden die entsprechenden Konfigurationsdateien aussehen? Erstellen Sie ein Konzept!
Cypress:  grafische Tests  
Travis: für Continious Integration -> yml -> language: python  
Py-Tests:  um Code zu testen  

Wichtige tox.ini Elemente:  
```
[tox]
envlist = py36

[testenv]
deps =
    pytest
    pytest-cov
    pytest-html
    flask
    flask_cors
    ..
    
 [pytest]
testpaths = src/Testing
python_files = test_*.py
python_classes = Tests
```

#### Bereiten Sie einen einfachen Test für den Aufruf der Random Funktion vor. Wie würden Sie diesen starten?
@pytest.fixture  
random Number test - pytest - asserts + setup/teardown
#### Implementieren Sie einen einfachen grafischen Test. Worauf achten Sie dabei?
Grafischer Test -> Cypress -> Simple Test Cypress.js  

Test mittels Aufruf der Ping Seite:  
```
describe('Test Grafisch', function() {
  it('Random', function() {
    cy.visit('http://localhost:8080/ping')
  })
})
```
#### Definieren Sie eine Konfiguration mit TravisCI für eine kontinuierliche Integration. Was müssen Sie dabei für die Python Tests und was für die grafischen Tests vorsehen?
Travis.yml muss alle notwendigen Schnittstellen laden.  

Wichtige travis Elemente:  
```
matrix:  
  include:  
    - language: python  
      python:  
        - "2.7"
        - "3.4"
      install: pip install tox-travis  
      script: tox  
    - language: node_js  
    ....
```

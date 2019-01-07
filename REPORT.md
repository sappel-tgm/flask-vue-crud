## Report File for Testverbesserung-Appel Flask-Vue-Crud + Flask-Vue-Spa

#### Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren?
```app.run(host='127.0.0.1', port=80)```

#### Implementieren Sie eine TODO-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
-> Books mit TODO ersetzen  

#### Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
CRUD Implementieren, Methoden erstellen

#### Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen.
Erweiterung von Vue, change der Routes in js  
Neue Komponenten durch components in der View

#### Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!
Authentifizierung einerseits mit Flask: Flask-HTTPAuth, Token Based Authentication  
[https://blog.miguelgrinberg.com/post/restful-authentication-with-flask](Flask-Auth)  
Außerdem Authentifizierung mit Vue: Login functions, mit Username+Password labels  
[https://blog.sqreen.io/authentication-best-practices-vue/](Vue-Auth)  

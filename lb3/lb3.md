# M300 LB3 - Dokumentation

## Autor
Sukash Sugumaran

## Inhaltsverzeichnis

- [Service Beschreibung](#beschrieb)
    - [Python Flask](#pythonflask)
- [Service Anwendung](#serviceanwendung)
- [Grafische Übersicht](#grafiken)
- [Befehle](#befehle)
    - [Befehle Images](#befehleimages)
    - [Befehle Container](#befehlecontainer)
- [Code Beschreibung](#code)
- [Service Testen](#testen)
- [Quellenverzeichnis](#quellenverzeichnis)

<a name="beschrieb"></a>
## Service Beschreibung
In einem Dreierteam (Sven Scheuss, Sukash Sugumaran und Thomas Mägerle) haben wir dieses Projekt durchgeführt. Wir haben uns überlegt eine Website zu hosten. Wir haben mit dem Tool Python Flask gearbeitet, da Sven Scheuss viel Erfahrung damit hat. Zusätzlich verwenden wir noch MySQL.
<a name="pythonflask"></a>
### Python Flask
Flask ist ein vom österreichischen Programmierer Armin Ronacher in Python geschriebenes Webframework. Der Fokus von Flask liegt auf Erweiterbarkeit und guter Dokumentation. Die einzigen Abhängigkeiten sind Jinja2, eine Template-Engine, und Werkzeug, eine Bibliothek zum Erstellen von WSGI-Anwendungen.

<a name="serviceanwendung"></a>
## Service Anwendung
Das Aufsetzen der VM ist sehr simpel. Als erstes muss das Repository heruntergeladen werden. Dies wird mit folgendem Befehl gemacht:

    `git clone https://github.com/sxkash10/M300-Services.git`

Als nächstes öffnet man eine GIT-Bash im Folder M300-Services/lb3
Anschliessend muss nur noch der Befehl `vagrant up` ausgeführt werden.
Danach 

<a name="grafiken"></a>
## Grafische Übersicht

<a name="befehle"></a>
## Befehle

<a name="befehleimages"></a>
### Befehle Images
Bei Docker Images folgt der jeweilige Befehl nach "docker image"
| Befehl            | Funktion                                             |  
| -------------     | ---------------------------------------------------- |  
| ```build```       | Erstellt ein Image.                                  |  
| ```push```        | Schiebt ein Image auf eine Remoteregistrierung.      |  
| ```pull ```       | Zieht ein Image oder ein Repository von einer Registry.|    
| ```ls```          | Listet alle vorhandenen Images auf.                  |  
| ```history```     | Zeigt alle Informationen eines Intermediate Image an. |  
| ```inspect```     | Zeigt detaillierte Informationen zu einem Image an, inkl. den einzelnen Layern.                                     |  
| ```rmi```         | Löscht ein Image.                                     |  

<a name="befehlecontainer"></a>
### Befehle Container
Bei Docker Container folgt der jeweilige Befehl nach "docker container"
| Befehl            | Funktion                                             |  
| -------------     | ---------------------------------------------------- |  
| ```create```      | Erstellt einen Container aus einem Image.            |  
| ```start```       | Startet einen existierenden Container.               |  
| ```run```         | Baut eine SSH-Verbindung zur gewünschten VM auf.     |  
| ```ls```          | Zeigt den aktuellen Status der VM an.                |  
| ```inspect```     | Zeigt detaillierte Informationen über einen Container an. |  
| ```logs```        | Druckt logs aus.                                     |  
| ```stop```        | Stoppt einen laufenden Container.                    |  
| ```kill```        | Stoppt den Hauptprozess in einem Container abrupt.   |  
| ```rm```          | Löscht einen gestoppten Container.                   |  

<a name="code"></a>
## Code Beschreibung
Hier sieht man den verwendeten Code und die erklärung zu dem jeweiligen Command.

Welche Version verwendet werden soll

    `version: "3"`

Netzwerk angeben

    `networks:
     lb3_network:`

Volumes angeben

    `volumes:
        app:
        database:`

flask-app Container wird ertsellt und konfiguriert

    `services:
    flask-app:
        container_name: lb3_py
        build: app
        restart: always
        ports:
            - '5000:5000'
        volumes:
            - ./app:/app
        networks:
            - lb3_network`

mysql-db Container wird erstellt und konfiguriert

        `mysql-db:
                container_name: lb3_db
                image: mysql:latest
                restart: always
                environment:
                    MYSQL_ROOT_PASSWORD: root
                    MYSQL_DATABASE: lb3
                ports:
                    - '3306:3306'
                volumes:
                    - ./database:/var/lib/mysql
                networks:
                    - lb3_network`

<a name="testen"></a>
## Service Testen
Um zu Testen ob das erstellen der VM mithilfe von Vagrant funktioniert hat, muss im Browser die seite localhost:100 aufgerufen werden.
Wenn folgende Seite zusehen ist hat alles funktioniert.

<a name="quellenverzeichnis"></a>
## Quellenverzeichnis
[Python Flask](https://flask.palletsprojects.com/en/2.1.x/)  
[Markdown Guide](https://www.markdownguide.org/)

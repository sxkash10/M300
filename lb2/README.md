# M300 - LB2
M300 - Sukash Sugumaran  
Webserver mit Apache2 und PHP

## Inhaltsverzeichnis

- [Einführung](#einfuehrung)
  - [Was ist Apache?](#wasistapache)
  - [Was ist PHP?](#wasistphp)
- [Code](#Code)
- [Anleitung](#anleitung)
- [Quellenverzeichnis](#quellenverzeichnis)

<a name="einfuehrung"></a>
### Einführung
Anhand dem Vagrantfile werden die zwei Webserver Apache2 und PHP installiert.

<a name="wasistapache"></a>
#### Was ist Apache?
Apache ist ein beliebter Open-Source, plattformübergreifender Webserver, der nach den Zahlen der beliebteste Webserver überhaupt ist.

Da die Funktionsweise eines Webservers sehr komplex ist, besteht die grundlegende Aufgabe aller Webserver darin, Anfragen von Clients anzunehmen (z.B. den Webbrowser eines Besuchers) und dann die Antwort auf diese Anfrage zu senden (z.B. die Komponenten der Seite, die ein Besucher sehen möchte).


<a name="wasistphp"></a>
#### Was ist PHP?
PHP ist eine Abkürzung für „Personal Home Page Tool“ oder auch „Hypertext Preprocessor“. PHP ist eine Skript-Sprache. Eine Skript-Sprache ist eine Programmier-Sprache, die meistens nur für kleinere Programme genutzt wird.

Sie verwenden zum Beispiel PHP für ein Kontakt-Formular auf Ihrer Webseite. PHP überprüft ob die Eingaben, die ein Webseiten-Besucher macht vollständig sind. PHP versendet dann das Kontakt-Formular als E-Mail.

<a name="Code"></a>
### Code
Unten sieht man den verwendeten Code für die Installation von Apache und PHP  



`Vagrant.configure("2") do |config|`

 Welche Ubnutu Version verwendet wird.  
  `config.vm.box = "ubuntu/bionic64"`  

  Virtualbox Version  
  `config.vm.box_version = "20220317.0.0"`  

  Änderungen in den Netzwerkeinstellungen. Hier wird die vorgegebene IP-Adresse verwendet.  
  `config.vm.network "private_network", ip: "192.168.11.22"`    

  `config.vm.synced_folder "www/", "/var/www/html", create: true`  

  Virtualbox wird hier verwendet  
  `config.vm.provider "virtualbox"`  


  `config.vm.provision "shell", inline: <<-SHELL`  

  Auf der Maschine werden Update ausgeführt  
  `sudo apt-get update`  

  Apache installation  
  `sudo apt-get install apache2 -y`  

  Der Server-Name "localhost" wird in das Konfigurationsfile geschrieben  
  `echo 'ServerName localhost' >> /etc/apache2/apache2.conf`

  Der Aapche Service wird neugestartet   
  `sudo service apache2 restart`  


  `sudo apt-add-repository ppa:ondrej/php`  
  `sudo apt-add-repository ppa:ondrej/apache2`  
  `sudo apt-get update`  

  PHP Installation  
  `sudo apt-get install php7.1 -y`  


  `sudo service apache2 restart`  
`SHELL`  
`end`  

<a name="anleitung"></a>
### Anleitung
Als erstes einen Shell aufmachen.  

Die Repository kann mit dem folgenden Link heruntergeladen werden.  
`git clone https://github.com/sxkash10/M300-Services.git`  

Danach mit `vagrant up` das Vagrantfile ausführen.  

Virtualbox öffnen und schauen, ob die VM läuft.

Einen Browser öffnen und die IP-Adresse "192.168.11.22" eingeben. Danach sollte man die Startseite von Apache sehen.  

Um zu testen, ob PHP funktioniert, kann man mit den folgenden URL prüfen "192.168.11.22/test.php"

<a name="quellenverzeichnis"></a>
### Quellenverzeichnis

- Was ist Apache? (https://kinsta.com/de/wissensdatenbank/was-ist-apache-web-server/)
- Mehr über Apache: (https://httpd.apache.org/)  
- Was ist PHP? (https://blog.zeta-producer.com/php/)  
- Mehr über PHP: (https://www.php.net/manual/de/intro-whatis.php)

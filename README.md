# beder-library
Hapat per zhvillimin e projektit:
1)	Instalimi i Dependency-ve
C:\Users\User>python -m venv beder_library_env
C:\Users\User>cd beder_library_env
C:\Users\User\beder_library_env>Scripts\activate
(beder_library_env) C:\Users\User\beder_library_env>pip install Django==4.2.7
(beder_library_env) C:\Users\User\beder_library_env>pip install djongo==1.3.6
(beder_library_env) C:\Users\User\beder_library_env>pip install pymongo==3.12.3
(beder_library_env) C:\Users\User\beder_library_env>pip install dnspython==2.3.0
(beder_library_env) C:\Users\User\beder_library_env>pip install Pillow==9.5.0
(beder_library_env) C:\Users\User\beder_library_env>pip install sqlparse==0.4.2

2)	Krijimi i Projektit Django
(beder_library_env) C:\Users\User\beder_library_env>django-admin startproject beder_library
(beder_library_env) C:\Users\User\beder_library_env>cd beder_library
(beder_library_env) C:\Users\User\beder_library_env\beder_library>python manage.py startapp library
(beder_library_env) C:\Users\User\beder_library_env\beder_library>code .

3)	Konfigurimi i Settings.py
Përmban të gjitha konfigurimet thelbësore për funksionimin e aplikacionit Django.
•	Konfigurimi i aplikacioneve (INSTALLED_APPS):
•	Konfigurimi i databazës:
•	Konfigurimi i gjuhës dhe kohës
•	Media dhe static files
•	Mesazhet e suksesit dhe errorit:
•	DEBUG dhe ALLOWED_HOSTS
4)	Krijimi i Model-it (library/models.py)
Modeli Book përfaqëson një libër në databazë. Ai përmban fushat kryesore si titulli, autori, ISBN, përshkrimi, kategoria, gjuha, data e publikimit, disponueshmëria dhe imazhi i librit.
5)	Krijimi i Forms (library/forms.py) 
Formë e personalizuar për të shtuar apo përditësuar një libër me inpute të dizajnuara.
Ofron opsione kërkimi dhe filtrimi për librat sipas titullit, autorit, kategorisë ose disponueshmërisë.
6)	Krijimi i Views (library/views.py)
Funksionet që menaxhojnë logjikën e aplikacionit. Ato përfshijnë:
•	book_list: shfaq listën e librave me filtër/kërkim dhe faqe.
•	book_detail: shfaq detajet e një libri.
•	book_create: lejon shtimin e një libri të ri.
•	book_update: lejon modifikimin e një libri ekzistues.
•	book_delete: fshin një libër.
•	dashboard: shfaq statistika të përgjithshme të bibliotekës.

7)	Konfigurimi I URL-ve
-	library/urls.py
-	beder_library/urls.py
Konfiguron rrugët e URL-ve për secilën pamje të aplikacionit. Kjo lejon lëvizjen midis faqeve si dashboard-i, lista e librave, shtimi dhe përditësimi i librave.

8)	Krijimi i Template-ve
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir templates
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir "templates/library"
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir static
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir "static/css"
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir "static/js"
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir media
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mkdir "media/books"
-	base.html
-	dashboard.html
-	book_list.html
-	book_detail.html
-	book_form.html
-	book_confirm_delete.html
Është struktura themelore HTML për të gjitha faqet e aplikacionit. Përfshin navbar-in, footer-in, mesazhet e sistemit dhe ngarkon stilizimet me Bootstrap dhe Font Awesome për një dizajn modern dhe responsiv.

9)	Konfigurimi I Admin-it (library/admin.py)
Konfiguron paraqitjen dhe menaxhimin e librave në panelin administrativ të Django. Lejon filtrimin, kërkimin dhe modifikimin e të dhënave të librave në mënyrë të strukturuar.

10)	Instalimi dhe Konfigurimi
(beder_library_env) C:\Users\User\beder_library_env\beder_library>mongosh
(beder_library_env) C:\Users\User\beder_library_env\beder_library>python manage.py makemigrations
(beder_library_env) C:\Users\User\beder_library_env\beder_library>python manage.py migrate
(beder_library_env) C:\Users\User\beder_library_env\beder_library>python manage.py runserver 127.0.0.1:8001

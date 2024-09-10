1.  - Buat direktori project baru dengan nama Storee.
    - Aktifkan virtual environment dengan nama venv.
    - Buat .gitignore agar venv dan cache tidak perlu di-push ke github.
    - Buat file bernama requirements.txt dan menambahkan dependencies lib-lib yang diperlukan.
    - Install dependencies melalui terminal dengan run "pip install -r requirements.txt".
    - Run "django-admin startproject storee . " untuk membuat project django, titik berguna agar project dijalankan di dalam folder ini, tidak membuat folder baru.
    - Run "python manage.py startapp main" untuk membuat main di folder ini.
    - Push ke github dan pws.
    - Tambahkan allowed hosts agar dapat diakses oleh server lokal dan pws.
    - Tambahkan "main" ke dalam installed apps dan menambahkan path('', include('main.urls')) ke      urlpatterns untuk mengatur routing proyek dengan app main, sehingga Django dapat mengakses urls.py di dalam app main (yang belum ada saat ini).
    - Tambahkan BASE_DIR / "templates" agar template di app main dapat meng-extend template base.html.
    - Buat urls.py di dalam app main untuk memetakan tampilan proyek utama dengan menggunakan views.py.
    - Buat model sesuai dengan spesifikasi dan melakukan migrasi untuk memperbarui struktur database.
    - Buat folder templates yang berisi file .html untuk menampilkan antarmuka web.
    - Buat views.py untuk mengatur tampilan HTML agar tidak statis.
    - Buat forms.py untuk menangkap input yang kemudian akan dikirim ke database.
    - Jalankan server.
    
2.  
    ![alt text](https://github.com/abdul-zacky/storee/blob/master/bagan.png?raw=true)

2. Membuat aplikasi dengan nama main pada proyek tersebut.
- Pada direktori saya me-run " python3 manage.py startapp main " untuk membuat aplikasi main, dan pada setting.py saya tambahkan 'main' pada 'ALLOWED APPS'
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Setelah saya sudah memberikan template dan attribute yang diingikan saya membuat file urls.py dalam direktori main
- Saya meng-import path django.urls untuk mendefinisikan pola URL
- Saya juga meng-import main.views dengan fungsi show.main untuk menampil URL
- Lalu pada direktori utama saya mengakses urls.py, disana saya meng-import fungsi include, dari django,urls
- Pada urls.py didalamnya ada variable urlpatterns dan saya menambahkan path(' ', include('main.urls')). Dibiarkan string kosong agar halaman aplikasi dapat diakses secara langsung
4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut: name, price, description
- Pada aplikasi main saya mengakses file models.py
- Lalu saya membuat class GiggleCatalogue dan menambahkan attribut name, price, description, dan, giggle level
- Lalu saya membuat migrasi model dengan me-run " python3 manage.py makemigrations "
- Lalu saya mengaplukasi migrasi model dengan me-run " python3 manage.py migrate "
5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Pada file views.py saya membuat fungai show_main yang memberikan context ke main.html yang berisikan nama app, nama saya, dan kelas saya
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Seperti yang saya sudah lalukan tadi saya membuat file urls.py dalam aplikasi main
- Saya meng-import path django.urls untuk mendefinisikan pola URL
- Saya juga meng-import main.views dengan fungsi show.main untuk menampil URL
7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Saya mendeploy ke PWS yang sebelumnua sudah saya buat sebelumnya
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
    Alur permintaan pada aplikasi web Django dimulai ketika klien mengirimkan permintaan HTTP ke server. urls.py menerima permintaan tersebut dan mengarahkan ke fungsi yang sesuai di views.py. Views kemudian memproses permintaan itu dan, jika diperlukan, berinteraksi dengan models.py untuk membaca atau menulis data. Setelah proses selesai, view akan merender template HTML dengan data yang sudah diproses. Hasilnya kemudian dikirim kembali ke klien sebagai respons HTTP melalui server Django.

3.  
    Git berfungsi untuk mengelola versi suatu proyek dengan perintah git add (untuk melacak perubahan),    commit (untuk menyimpan snapshot secara lokal), dan push (untuk mengunggah snapshot ke server Git). Kita dapat menyimpan snapshot proyek dan mendapatkan snapshot dengan git pull (untuk mengambil dan menggabungkan versi terbaru ke proyek yang sedang dikerjakan) atau git clone (untuk mengganti seluruh isi proyek dengan versi snapshot tertentu).

4. 
    Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena mudah digunakan dan dipahami, fitur yang tersedia cukup lengkap, memiliki arsitektur dengan pola yang jelas, dan beberapa perusahaan besar sudah mengimplementasikan Django di aplikasi mereka.

5. 
    Model di Django disebut ORM (Object Relational Mapper) karena data yang disimpan di database menggunakan tipe Object Oriented, dihubungkan dan dipetakan dengan objek Python. 
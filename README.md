Tugas 2
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



Tugas 3
1.  
    Dalam mengimplementasikan sebuah platform, data delivery diperlukan agar data dapat disampaikan secara cepat dan akurat. Data delivery juga bikin user experience lebih mulus dan platform jadi lebih efisien.

2. 
    Json lebih populer dibandingkan XML karena Json memiliki struktur yang lebih simpel, lebih mudah dibaca, ukurannya yang lebih kecil, dan gampang diintegrasikan dengan berbagai API modern. Dan menurut saya, walaupun XML juga memiliki kelebihan seperti mampu meng-handle data yang sangat kompleks, Json tetap lebih baik daripada XML dengan memperhatikan kelebihan-kelebihan yang ditawarkan oleh Json sendiri.

3. 
    Method is_valid() pada form Django berfungsi untuk melakukan pengecekan terhadap data yang di-submit lewat form Django apakah sudah sesuai standar dan aturan yang ditentukan atau belum. Method ini penting karena dapat melakukan validasi form lebih mudah.

4. 
    csrf_token dibutuhkan di form Django untuk melakukan proteksi dari serangan Cross-Site Request Forgery atau juga biasa disebut CSRF yang mana dapat mengirim request berbahaya atas nama pengguna tanpa sepengetahuannya. Jika tidak ada csrf_token, penyerang bisa mengubah data atau melakukan aksi berbahaya saat pengguna melakukan sesi login, contohnya melakukan transaksi finansial atau mengganti kata sandi. csrf_token memastikan setiap request form valid hanya jika token yang dikirim sesuai dengan yang dihasilkan oleh server, sehingga dapat mencegah serangan CSRF ini.

5. 
    - Pertama, saya mengimplementasikan skeleton sebagai kerangka views dengan membuat file baru bernama base.html dan menambahkannya ke list TEMPLATES di settings.py. Skeleton berguna untuk memastikan konsistensi desain situs web dan memperkecil kemungkinan terjadinya redundansi kode.
    - Lalu, saya mengubah primary key yang awalnya merupakan integer menjadi UUID untuk meningkatkan keamanan situs web yang sedang dikerjakan.
    - Setelah itu, saya membuat file bernama forms.py untuk membuat struktur form yang dapat menerima data Product baru. Lalu, saya menambahkan fungsi baru bernama create_product di file views.py untuk menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form. Dan tidak lupa, saya juga menambahkan path URL ke dalam variabel urlpatterns di file urls.py
    - Lalu, saya membuat file bernama create_product.html
    - Lanjut, saya melakukan import HttpResponse dan serializers untuk dapat mengembalikan data dalam bentuk XML. Saya juga membuat method show_xml di file views.py dan menambahkan path URL ke urlpatterns.
    - Setelah itu, saya membuat method show_json di file views.py untuk dapat mengembalikan data dalam bentuk json dan tidak lupa saya juga menambahkan path URL ke urlpatterns.
    - Tidak ketinggalan, saya membuat method show_xml_by_id dan show_json_by_id di file views.py agar dapat mengembalikan data berdasarkan id dalam bentuk XML dan JSON. Saya juga menambahkan url path nya.
    - Lalu, saya melakukan run "python3 manage.py runserver"
    - Terakhir, saya melakukan add, commit, dan push ke github dan pws.

Response XML
![alt text](https://github.com/abdul-zacky/storee/blob/master/response_xml.png?raw=true)

Response Json
![alt text](https://github.com/abdul-zacky/storee/blob/master/response_json.png?raw=true)

Response XML by ID
![alt text](https://github.com/abdul-zacky/storee/blob/master/response_xml_by_id.png?raw=true)

Response Json by ID
![alt text](https://github.com/abdul-zacky/storee/blob/master/response_json_by_id.png?raw=true)
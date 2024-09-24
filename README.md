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



Tugas 4
1. 
    HttpResponseRedirect() dan redirect() adalah dua metode untuk mengalihkan pengguna ke URL lain dalam aplikasi Django, tetapi keduanya digunakan dalam situasi yang berbeda. HttpResponseRedirect() adalah kelas yang secara langsung membuat respons HTTP untuk pengalihan dan mengharuskan kita untuk secara manual menyertakan URL. Meskipun memberikan kontrol lebih detail, cara ini memerlukan lebih banyak kode untuk menangani pengalihan.

    Sementara itu, redirect() adalah fungsi pembantu yang lebih mudah digunakan. Dengan redirect(), kita bisa memasukkan URL, nama view, atau bahkan ID objek, menjadikannya lebih fleksibel dan user-friendly. Fungsi ini secara otomatis menangani pengalihan berdasarkan nama view, yang mengurangi risiko kesalahan dari penulisan URL secara manual. Oleh karena itu, redirect() seringkali lebih dianjurkan karena meningkatkan keterbacaan kode dan efisiensi pengalihan.

2. 
    Untuk menghubungkan model Product dengan model User dalam Django, kita bisa menggunakan relasi satu-ke-banyak.

    Definisi Model: Model Product memiliki atribut seperti nama, deskripsi, dan harga. Hubungan dengan model User dilakukan melalui ForeignKey, yang menunjukkan bahwa setiap produk dimiliki oleh satu pengguna.

    Pengaturan ForeignKey: Dengan menambahkan ForeignKey(User, on_delete=models.CASCADE), kita menentukan bahwa ketika pengguna dihapus, semua produk yang terkait juga akan dihapus, menjaga konsistensi data.

    Atribut related_name: Dengan related_name='products', kita dapat mengakses produk-produk milik pengguna dengan lebih mudah, misalnya menggunakan user.products.all() untuk mendapatkan semua produk dari pengguna tersebut.

    Pembuatan Data: Saat membuat produk baru, kita dapat langsung menetapkan pengguna yang memilikinya, sehingga mempermudah pengelolaan data.

    Pengambilan Data: Relasi yang terhubung memungkinkan pengambilan produk milik seorang pengguna secara efisien, mendukung manajemen dan analisis data yang lebih baik.

3. 
    Authentication dan authorization adalah dua konsep penting dalam keamanan aplikasi, namun memiliki perbedaan yang jelas.

    1. Authentication adalah proses memverifikasi identitas pengguna, memastikan bahwa mereka adalah yang mereka klaim. Misalnya, ketika pengguna memasukkan username dan password untuk login, sistem akan memeriksa validitas kredensial tersebut.

    2. Authorization adalah proses menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya atau melakukan tindakan tertentu. Contohnya, setelah login, sistem menentukan apakah pengguna memiliki hak untuk melihat halaman tertentu atau mengedit data.

    3. Ketika pengguna login, langkah pertama adalah autentikasi, di mana pengguna memasukkan kredensial (username dan password), dan sistem memverifikasinya. Jika kredensial valid, pengguna dianggap terautentikasi. Setelah itu, otorisasi dilakukan untuk menentukan akses berdasarkan peran atau izin yang diberikan. Dalam Django, Authentication diimplementasikan melalui sistem autentikasi bawaan, yang memudahkan pengembang dalam menangani login dan logout. Ini melibatkan model User dan fungsi seperti authenticate() untuk memverifikasi kredensial. Sedangkan untuk Authorization, Django menggunakan sistem izin dan grup. Pengembang dapat menetapkan izin untuk model atau tampilan dan menggunakan dekorator seperti @login_required dan @permission_required untuk membatasi akses pengguna.

4. 
    Django menyimpan informasi pengguna yang telah login menggunakan session cookies. Setelah pengguna berhasil login, Django membuat sebuah session yang berisi data pengguna dan menyimpannya di basis data, memori, atau file, bergantung pada konfigurasi. Django kemudian mengirimkan session ID dalam bentuk cookie kepada pengguna. Setiap kali pengguna mengajukan permintaan baru, cookie tersebut dikirim kembali ke server untuk memverifikasi identitas pengguna yang telah login, sehingga mereka tidak perlu login ulang selama sesi aktif.

    Penggunaan Lain Cookies Selain mengingat pengguna yang login, cookies memiliki beberapa fungsi lain, antara lain:

    1. Menyimpan Preferensi Pengguna: Misalnya, bahasa atau tema yang dipilih oleh pengguna.
    2. Melacak Aktivitas Pengguna: Cookies dapat digunakan untuk melacak halaman yang dikunjungi atau produk yang dilihat, sehingga memungkinkan personalisasi konten.
    3. Membantu Analitik: Cookies dapat digunakan untuk melacak perilaku pengguna secara anonim, memberikan data untuk analisis website.
    4. Mengelola Keranjang Belanja: Pada situs e-commerce, cookies digunakan untuk menyimpan informasi sementara terkait barang-barang yang ditambahkan ke keranjang belanja.

    - Apakah Semua Cookies Aman Digunakan? Tidak semua cookies aman, terutama jika tidak dikelola dengan benar. Beberapa potensi risiko adalah:
    - Cookies Tanpa Enkripsi: Jika cookies yang berisi informasi sensitif dikirim tanpa enkripsi (melalui HTTP, bukan HTTPS), mereka dapat disadap oleh pihak ketiga.
    - Session Hijacking: Penyerang dapat mencuri cookies session dan berpura-pura menjadi pengguna yang sah jika cookies tidak dijaga dengan baik.
    - Third-Party Cookies: Cookies dari pihak ketiga dapat digunakan untuk melacak aktivitas pengguna di berbagai situs, yang dapat menimbulkan masalah privasi. Untuk meningkatkan keamanan, Django mendukung Secure Cookies (hanya dikirim melalui HTTPS) dan HttpOnly Cookies (tidak dapat diakses oleh JavaScript), mengurangi risiko pencurian dan eksploitasi cookies.

5. 
    Berikut adalah langkah-langkah yang saya lakukan untuk menyelesaikan checklist Tugas Individu 4:

    1. Di file views.py, saya menambahkan import untuk UserCreationForm dan messages.
    2. Kemudian, saya membuat fungsi register, yang nantinya akan diimport ke urls.py, dan membuat file register.html di dalam folder templates pada direktori main.
    3. Selanjutnya, saya membuat fungsi login dengan membuka views.py dan menambahkan import untuk authenticate, login, dan AuthenticationForm. Saya juga membuat fungsi login_user yang akan diimport ke urls.py, serta membuat file login.html di dalam folder templates pada direktori main.
    4. Saya juga membuat fungsi logout dengan mengimport fungsi logout, menambahkan tombol logout ke main.html, dan mengimport fungsi logout ke urls.py pada direktori main.
    5. Kemudian, saya membatasi akses ke halaman utama (main) bagi pengguna yang belum login, dengan menambahkan import login_required dan menambahkan dekorator @login_required(login_url='/login') di atas fungsi show_main.
    6. Setelah itu, saya menambahkan penggunaan cookies dengan mengimport HttpResponseRedirect, reverse, dan datetime. Pada file yang sama, saya menambahkan fungsionalitas cookies bernama last_login ke fungsi login_user. Di fungsi show_main, saya menambahkan 'last_login': request.COOKIES['last_login'] ke bagian context, dan mengedit main.html untuk menampilkan sesi login terakhir.
    7. Saya menghubungkan model Product dengan User di file models.py, dengan mengimport User, lalu mengubah fungsi create_giggle_entry dengan menambahkan field user yang menggunakan objek User dari request.user yang sedang login, menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang terotorisasi.
    8. Selanjutnya, saya mengubah nilai giggle_entries dan context pada fungsi show_main agar nama yang ditampilkan di menu utama adalah nama pengguna yang telah login.
    9. Saya menjalankan makemigrations dan migrate.
    9. Saya juga mengimport os pada settings.py dan mengubah konfigurasi debug.
    10. Terakhir, saya menyimpan semua file, melakukan add, commit, dan push.
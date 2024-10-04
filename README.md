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



Tugas 5
1.  
    Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

    a. Urutan Spesifisitas (Specificity)
    Prioritas CSS didasarkan pada tingkat spesifisitas dari masing-masing selector. Spesifisitas dihitung menurut empat kategori:
    - Inline styles (gaya langsung diterapkan pada elemen HTML) memiliki prioritas tertinggi.
    - ID selector (#id) berada di peringkat kedua.
    - Class selector, attribute selector, dan pseudo-class (seperti .class, [type="text"], atau :hover) berada di bawah ID.
    - Tag selector (misalnya p, div) dan pseudo-element (seperti ::before, ::after) memiliki prioritas terendah.

    b. Menghitung Spesifisitas  
    Setiap selector diberi poin berdasarkan kategorinya:
    - Inline styles: Mendapat 1 poin untuk elemen inline (spesifisitas tertinggi).
    - ID selector: Mendapat 1 poin per ID (#contoh).
    - Class selector, attribute selector, pseudo-class: Mendapat 1 poin per item (misalnya .class, [type="text"], :hover).
    - Tag selector dan pseudo-element: Mendapat 1 poin per item (misalnya div, p, ::before).
    Contoh perhitungan spesifisitas:
    - Inline style: style="color: red" (Spesifisitas: 1000)
    - ID selector: #id (Spesifisitas: 0100)
    - Class selector: .class (Spesifisitas: 0010)
    - Tag selector: p (Spesifisitas: 0001)
    Selector dengan spesifisitas tertinggi akan diprioritaskan jika elemen terpengaruh oleh beberapa selector.

    c. Urutan Sumber CSS  
    Selain spesifisitas, urutan penulisan CSS juga berpengaruh pada prioritas:
    - Urutan penulisan: Jika dua selector memiliki spesifisitas yang sama, yang ditulis paling akhir akan digunakan.
    - !important: Properti dengan deklarasi !important akan mengesampingkan semua aturan di atas, kecuali jika ada deklarasi !important lain dengan spesifisitas yang lebih tinggi.
    Dengan demikian, urutan prioritas CSS ditentukan oleh spesifisitas, urutan penulisan, dan deklarasi !important. Selector dengan spesifisitas tertinggi akan selalu diterapkan terlebih dahulu.

2. 
    Desain responsif penting karena memungkinkan aplikasi web menyesuaikan tampilannya dengan berbagai perangkat, seperti smartphone, tablet, atau desktop. Ini memberikan pengalaman pengguna yang konsisten, meningkatkan SEO, dan mempermudah proses pengembangan serta pemeliharaan.
    Contoh aplikasi yang sudah menggunakan desain responsif: LinkedIn, Youtube
    Contoh aplikasi yang belum menggunakan desain responsif: Website SD saya, Website tugas 2 saya

3. 
    Berikut adalah penjelasan perbedaan antara margin, border, dan padding, serta cara mengimplementasikannya:

    a. Margin:
    - Margin adalah ruang di luar elemen, yang mengatur jarak antara elemen dengan elemen lainnya di sekitarnya.
    - Contoh implementasi:
        ```
        div {
            margin: 15px;
        }
        ```
        Contoh ini memberikan jarak 15px di semua sisi elemen `div` dari elemen lainnya di sekitarnya.

    b. Border:
    - Border adalah garis yang mengelilingi elemen. Border terletak di antara margin dan padding.
    - Contoh implementasi:
        ```
        div {
            border: 5px solid black;
        }
        ```
        Contoh ini memberikan garis hitam dengan ketebalan 5px di sekitar elemen `div`.

    c. Padding:
    - Pengertian: Padding adalah ruang di dalam elemen, yang mengatur jarak antara konten elemen dan border elemen tersebut.
    - Contoh implementasi:
        ```
        div {
            padding: 30px;
        }
        ```
        Contoh ini memberikan jarak 30px di dalam elemen `div`, antara konten dan border.

    Perbedaan:
    - Margin: Mengatur jarak di luar elemen.
    - Border: Garis di sekitar elemen yang terletak di antara margin dan padding.
    - Padding: Mengatur jarak di dalam elemen, antara konten dan border.

4.  
    Flexbox dan Grid Layout adalah dua teknik tata letak dalam CSS yang memungkinkan kita mengatur elemen secara responsif.

    a. Flexbox (Flexible Box Layout):
    - Flexbox digunakan untuk menyusun elemen dalam satu dimensi, baik dalam baris (horizontal) atau kolom (vertikal). Elemen di dalam *flex container* secara otomatis menyesuaikan ukurannya dengan ruang yang tersedia. Grid layout sangat cocok digunakan untuk mengatur elemen yang perlu disejajarkan secara horizontal atau vertikal, seperti menu navigasi, tampilan produk, atau galeri gambar.
    - Contoh implementasi:
        ```
        .container {
            display: flex;
            justify-content: space-around;
        }
        ```
        Contoh ini menyusun elemen dalam *container* secara horizontal dengan ruang yang rata di antara mereka.

    b. Grid Layout:
    - Grid Layout memungkinkan pembuatan tata letak dua dimensi, yaitu dengan baris dan kolom. Grid memberikan kontrol yang lebih presisi dalam menempatkan elemen di berbagai area dalam tata letak. Grid layout cocok untuk tata letak yang lebih kompleks, seperti halaman dengan banyak kolom dan baris, seperti dashboard atau tata letak halaman utama.
    - Contoh implementasi:
        ```
        .container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
        }
        ```
        Contoh ini membagi *container* menjadi tiga kolom dengan lebar yang sama.

    Perbedaan:
    - Flexbox berfungsi untuk tata letak satu dimensi (hanya baris atau kolom).
    - Grid digunakan untuk tata letak dua dimensi (baris dan kolom).

5. 
    Berikut adalah langkah-langkah implementasi checklist yang dilakukan secara bertahap:

    a. Membuat Fungsi `edit_product` dan `delete_product` di `views.py`
    - Saya memulai dengan membuat dua fungsi di `views.py` yang menangani permintaan untuk mengedit dan menghapus produk. Masing-masing fungsi menerima parameter berupa request dan ID produk. Ini memungkinkan aplikasi untuk mengenali produk mana yang sedang diedit atau dihapus.
    - Selanjutnya, saya menambahkan URL untuk kedua fungsi ini di `urls.py`, sehingga mereka dapat diakses melalui URL yang tepat.

    b. Membuat Template untuk `edit_product` dan Memperbarui Template Lain
    - Saya merancang template untuk halaman edit produk, memastikan pengguna dapat melihat dan mengubah informasi produk seperti nama, harga, dan deskripsi.
    - Selain itu, saya memperbarui beberapa template lain agar tampilannya lebih menarik dan sesuai dengan tema keseluruhan aplikasi.

    c. Mengedit `main.html` untuk Menampilkan Pesan Ketika Tidak Ada Produk
    - Di `main.html`, saya menambahkan kondisi di mana jika tidak ada produk yang tersedia, maka akan muncul pesan yang menjelaskan bahwa produk tidak tersedia. Ini dilakukan untuk meningkatkan pengalaman pengguna saat halaman kosong.

    d. Membuat `card_product.html` untuk Menampilkan Informasi Produk
    - Saya membuat file `card_product.html` yang bertugas untuk menampilkan informasi detail produk, seperti nama, harga, deskripsi, serta menyediakan tombol untuk edit dan delete.
    - Template ini kemudian saya hubungkan ke `main.html` agar dapat ditampilkan di halaman utama.

    e. Mengatur Layout `card_product` Menggunakan Grid
    - Saya menggunakan grid layout di CSS untuk menampilkan informasi produk di dalam kartu secara rapi. Ini membantu menampilkan produk secara responsif dan terstruktur di berbagai perangkat.

    f. Membuat Template Navbar yang Responsif
    - Saya merancang sebuah template navbar yang responsif dan menempatkannya di direktori luar agar dapat digunakan oleh halaman lain. Setiap elemen di navbar dihubungkan dengan link yang sesuai, sehingga pengguna dapat dengan mudah menavigasi situs.

    g. Menambahkan Script untuk Responsivitas Mobile
    - Terakhir, saya menambahkan script agar situs lebih ramah untuk perangkat mobile, memastikan tata letak dan elemen-elemen berfungsi dengan baik di berbagai ukuran layar.
    - Setelah semua selesai, saya melakukan langkah-langkah akhir dengan `git add`, `commit`, dan `push` untuk menyimpan dan mengunggah perubahan ke repository.



Tugas 6
1. 
    Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web: Javascript penting buat bikin aplikasi web yang interaktif dan responsif. Dengan javascript, kita bisa refresh konten halaman web tanpa perlu reload seluruh halaman. Selain itu, kita bisa bikin aplikasi yang lebih dinamis dan interaktif, seperti validasi data langsung di browser pengguna atau interaksi yang menarik. Javascript juga memungkinkan komunikasi asinkron dengan server lewat AJAX, jadi aplikasi terasa lebih cepat dan responsif.

2.  
    Fungsi Penggunaan await pada fetch() dan Dampaknya Jika Tidak Digunakan: await dipakai supaya Javascript nunggu hasil dari fetch() dulu sebelum lanjut ke baris berikutnya. Jadi, kalau pakai await, aplikasi akan nunggu sampai fetch() selesai dan dapat respons dari server. Kalau nggak pakai await, Javascript bakal langsung lanjut tanpa nunggu, yang bisa bikin aplikasi error karena respons belum siap dipakai.

3.  
    Kegunaan @csrf_exempt untuk AJAX POST: Django pakai token CSRF buat melindungi aplikasi dari serangan csrf, tapi kadang pas pakai AJAX POST, kita nggak kirim token CSRF dari frontend dan django bakal tolak permintaan itu. @csrf_exempt di view bikin django nggak ngecek CSRF buat permintaan itu, jadi AJAX POST bisa jalan tanpa token csrf.

4. 
    Kenapa Pembersihan Data Input Harus di Backend Juga, Bukan Cuma di Frontend: Walaupun di frontend bisa dicegah input yang nggak sesuai, pembersihan di backend tetap penting buat jaga keamanan dan integritas data. Soalnya, pengguna masih bisa kirim data yang nggak sesuai atau bahkan berbahaya kalau mereka tahu cara manipulasi permintaan. Jadi, backend tetap harus validasi dan bersihkan data sebelum diolah atau disimpan di database, buat menghindari serangan kayak SQL injection atau cross-site scripting (XSS).

5. 
    a. Menambahkan Pesan Error di login_user pada views.py
    - Saya menambahkan pesan error dengan menggunakan messages.error(request, "Invalid username or password. Please try again.") ketika login gagal. Ini memungkinkan pengguna mendapatkan notifikasi langsung di halaman login apabila username atau password tidak cocok.
    - Setelah itu, saya memastikan bahwa pesan ini akan tampil di template login.html agar pengguna dapat melihatnya ketika login gagal.
    b. Membuat Fungsi add_mood_entry_ajax di views.py
    - Saya memulai dengan menambahkan fungsi add_mood_entry_ajax yang berfungsi untuk menambah data mood ke dalam basis data menggunakan AJAX. Fungsi ini menerima data yang dikirim melalui metode POST, seperti mood, feelings, dan mood intensity.
    - Untuk menghindari pengecekan CSRF dan membatasi metode yang diizinkan, saya menggunakan dekorator @csrf_exempt dan @require_POST. Ini memastikan bahwa fungsi hanya dapat diakses dengan metode POST dan tidak perlu token CSRF.
    c. Menambahkan Path Baru di urls.py
    - Selanjutnya, saya menambahkan path baru di urls.py agar fungsi add_mood_entry_ajax bisa diakses melalui URL tertentu, misalnya /create-mood-entry-ajax. Ini mempermudah akses AJAX ke fungsi tersebut.
    d. Menggunakan AJAX untuk Menampilkan Data Mood
    - Saya menggunakan fungsi fetch() untuk mengambil data mood dari endpoint JSON secara asinkronus. Dengan cara ini, saya bisa memuat data secara dinamis di halaman tanpa perlu reload seluruh halaman.
    - Saya menambahkan fungsi getMoodEntries dan refreshMoodEntries di dalam main.html. Kedua fungsi ini bekerja sama untuk mengambil data mood dan memperbarui tampilan halaman secara real-time.
    e. Membuat dan Menambahkan Modal untuk Form Penambahan Mood
    - Saya merancang modal menggunakan Tailwind CSS di main.html sebagai form untuk menambah mood. Modal ini bisa ditampilkan dengan mengklik tombol, dan dilengkapi dengan form input untuk mood, feelings, dan mood intensity.
    - Di dalam modal, saya tambahkan tombol submit yang akan memanggil fungsi JavaScript addMoodEntry untuk mengirim data ke server.
    f. Menambahkan Fungsi addMoodEntry untuk Mengirim Data dengan AJAX
    - Di dalam <script> pada main.html, saya membuat fungsi addMoodEntry untuk menangani submit form secara asinkronus. Data dari form dikirim ke server menggunakan AJAX POST tanpa perlu reload halaman.
    - Setelah data dikirim, modal akan otomatis tertutup dan form akan di-reset, sehingga aplikasi langsung siap untuk menambah mood baru lagi tanpa gangguan.
    g. Menghubungkan Tombol di Modal ke Fungsi addMoodEntry
    - Saya menambahkan event onclick pada tombol submit di modal agar langsung menjalankan fungsi addMoodEntry ketika tombol tersebut diklik. Hal ini memudahkan proses submit data mood entry tanpa reload halaman.
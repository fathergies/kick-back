Nama : Angelique Natasya Braveina Chelsey Siagian
NPM : 2406496006
Kelas : PBP F

Nama aplikasi yang dibuat : Kick Back
Penjelasan : Aplikasi Kick Back adalah platform marketplace untuk membeli dan menjual perlengkapan football (seperti jersey, sepatu bola, dan aksesoris lainnya) dalam kondisi preloved.

https://angelique-natasya-kickback.pbp.cs.ui.ac.id
https://pbp.cs.ui.ac.id/angelique.natasya/footballnews

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Saat membuat project Django baru, saya membuat folder baru bernama kick-back dan mengaktifkan virtual environment supaya semua package terisolasi. Setelah itu saya membuat file requirements.txt berisi dependency kayak Django, gunicorn, whitenoise, dan lain-lain, lalu saya install semua package yang ada di situ.

Setelah sudah, saya membuat project Django dengan nama kick_back. Di tahap ini saya juga nambahin file .env buat development (isinya PRODUCTION=False) dan .env.prod buat production yang berisi konfigurasi database yang dikirim dari email. Supaya Django bisa baca environment variable, saya load file .env di settings.py. Di file yang sama saya atur ALLOWED_HOSTS agar bisa diakses dari localhost, dan saya ubah konfigurasi database.

Setelah konfigurasi selesai, saya jalanin migrasi database terus runserver buat ngecek. Kalau dibuka di browser, muncul halaman default Django tanda project berhasil dibuat. Langkah terakhir saya inisialisasi git repo, bikin .gitignore, commit semua file penting, terus push ke GitHub. Dengan begitu project ini udah siap dipakai dan bisa dilanjut ke tahap deployment ke PWS. Setelah deployment ke PWS berhasil, https://angelique-natasya-kickback.pbp.cs.ui.ac.id sudah bisa diakses.


b. Membuat aplikasi dengan nama main pada proyek tersebut.
Saya membuat app baru bernama 'main' dan mendaftarkannya ke installed apps di settings.py. Caranya dengan perintah python manage.py startapp main. Perintah ini otomatis bikin struktur folder khusus untuk aplikasi, yang di dalamnya sudah ada file bawaan seperti models.py, views.py, urls.py, dan lain lain. Saya membuat folder templates dan mengisinya dengan main.html yang didalamnya berisi keterangan nama app, nama saya, npm, dan kelas. 


c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Saya menambahkan routing pada urls.py yang ada di folder proyek agar aplikasi main dapat dijalankan. Pada bagian ini, saya menggunakan fungsi include() untuk menghubungkan URL di level proyek dengan urls.py milik aplikasi main. Dengan begitu, ketika pengguna mengakses alamat yang sesuai, Django akan meneruskan request tersebut ke routing yang sudah saya definisikan di dalam aplikasi main.


d.  Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
Setelah itu, saya memasukkan models.py yang sesuai dengan aplikasi saya.

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)


e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya membuat sebuah fungsi pada views.py dengan nama show_main. Di dalam fungsi ini, saya menyiapkan sebuah context dictionary yang berisi data berupa nama aplikasi, nama saya, serta kelas saya. Context ini kemudian saya kirimkan ke template main.html menggunakan fungsi render. Saya juga mengubah format pada file HTML agar data yang dikirim dari context bisa ditampilkan dengan lebih rapi dan terstruktur. Dengan perubahan ini, halaman main.html tidak hanya menampilkan teks biasa, tetapi sudah diformat menggunakan elemen-elemen HTML sehingga informasi seperti nama aplikasi, nama, dan kelas saya terlihat lebih jelas ketika ditampilkan di browser.


f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Saya membuat sebuah routing pada urls.py di aplikasi main untuk memetakan fungsi show_main yang sebelumnya telah dibuat pada views.py. Pada bagian ini, saya menggunakan path('', show_main, name='show_main') sehingga ketika pengguna mengakses URL utama dari aplikasi main, secara otomatis akan diarahkan ke fungsi show_main. Dengan begitu, halaman main.html yang sudah saya atur akan ditampilkan sesuai dengan context yang telah saya kirimkan melalui fungsi tersebut.

g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Sebelum melakukan deployment, saya menjalankan aplikasi secara lokal menggunakan perintah python manage.py runserver. Aplikasi kemudian dapat diakses melalui alamat http://127.0.0.1:8000/. Hal ini memastikan bahwa seluruh konfigurasi, routing, dan template sudah berjalan dengan benar di komputer saya. Setelah git add, commit dan push master & pws, https://angelique-natasya-kickback.pbp.cs.ui.ac.id sudah bisa diakses.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://drive.google.com/file/d/1Vs4Dtjb3aPEkEMw_i_oIWOcXVK3wf8Wg/view?usp=sharing

Alur request–response di Django dimulai ketika client (browser) mengirim request melalui internet menuju server Django. Request ini pertama kali diproses oleh urls.py, yang berperan sebagai router untuk mencocokkan URL dengan fungsi yang sesuai di views.py. Setelah diarahkan, views.py menjalankan logika aplikasi. Jika dibutuhkan data, views akan berinteraksi dengan models.py yang berhubungan langsung dengan database. Data hasil query kemudian dikembalikan ke views, lalu views merender template HTML (misalnya index.html) dengan menyisipkan data tersebut. Hasil render berupa halaman HTML utuh dikirimkan sebagai response kembali melalui internet ke client, dan akhirnya ditampilkan di browser untuk user.


3. Jelaskan peran settings.py dalam proyek Django!
settings.py adalah file konfigurasi utama dalam proyek Django. Semua pengaturan penting yang mengontrol jalannya aplikasi disimpan di sini, mulai dari pengaturan database, daftar aplikasi yang digunakan, middleware, template, sampai pengaturan keamanan seperti SECRET_KEY dan ALLOWED_HOSTS. settings.py memastikan aplikasi berjalan sesuai kebutuhan baik di development maupun production.

4. Bagaimana cara kerja migrasi database di Django?
Migrasi database di Django adalah proses untuk menerjemahkan perubahan yang kita buat pada model di models.py menjadi struktur tabel di database. Ketika saya membuat atau mengubah model, saya perlu menjalankan perintah makemigrations agar Django mencatat perubahan tersebut dalam bentuk file migrasi. File migrasi ini berisi instruksi tentang apa yang harus dilakukan pada database, misalnya menambahkan tabel baru atau mengubah kolom. Setelah itu, saya menjalankan perintah migrate untuk benar-benar menerapkan perubahan tersebut ke dalam database. Dengan cara ini, struktur database akan selalu selaras dengan model yang saya definisikan dalam kode Django.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sudah menyediakan banyak fitur bawaan yang cukup memudahkan bagi saya, pemula yang belum pernah mencoba webdev, seperti user auth, manajemen database, hingga panel admin. Dengan begitu, saya tidak perlu membangun semuanya dari nol dan bisa langsung fokus memahami konsep inti dalam pengembangan web, seperti model, view, template, serta interaksi dengan database. Django juga menggunakan bahasa Python yang sudah sempat dipelajari di DDP1, sehingga transisi dari pembelajaran terakhir ke membangun aplikasi masih familiar. Selain itu, Django sudah banyak dipakai orang sehingga memudahkan saya untuk menemukan contoh, referensi, maupun solusi ketika mengalami kendala.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak, kebetulan asdos saya Ka Fahri sangat baik dan membantu ketika saya kesusahan. Ka Fahri juga mengingatkan kalau project yang saya buat masih ada kesalahan.


------------------------------------------------TUGAS 3---------------------------------------------------
7. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan karena menjadi mekanisme utama untuk mengirimkan data antar komponen dalam platform, baik dari server ke pengguna maupun antar sistem. Tanpa data delivery yang baik, informasi tidak akan sampai secara cepat, akurat, dan konsisten sehingga platform tidak bisa berfungsi sesuai kebutuhan.

8. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, baik XML maupun JSON sebenarnya sama-sama digunakan untuk pertukaran data, tetapi JSON lebih populer karena lebih sederhana dan ringkas dibandingkan XML. Struktur XML cenderung verbose dengan banyak tag pembuka dan penutup, sehingga membuat ukuran data lebih besar dan agak sulit dibaca manusia. JSON memiliki format yang lebih ringan dan mudah dipahami karena mirip dengan struktur objek di banyak bahasa pemrograman modern. Selain itu, JSON juga lebih cepat diproses dan sudah didukung secara luas oleh hampir semua bahasa pemrograman serta framework web yang ada sekarang. Karena itu, JSON lebih banyak digunakan dalam pengembangan aplikasi web dan API modern, sementara XML lebih sering dipertahankan untuk kebutuhan tertentu atau sistem lama yang masih bergantung pada format tersebut.

9. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk mengecek apakah data yang diinput pengguna sudah sesuai dengan aturan validasi yang ditentukan di form. Kalau valid, kita bisa langsung gunakan datanya, kalau tidak valid maka akan muncul error yang bisa ditampilkan kembali ke pengguna. Method ini penting supaya data yang masuk ke sistem tetap konsisten, bersih, dan aman.

10. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token pada form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa setiap permintaan POST benar-benar berasal dari pengguna yang sah dan bukan dari pihak luar. Kalau tidak ditambahkan, aplikasi jadi rentan terhadap serangan CSRF, di mana penyerang bisa membuat pengguna tanpa sadar mengirimkan request berbahaya (misalnya transfer uang, ganti password, atau hapus data) hanya dengan mengklik link atau membuka halaman berisi script berbahaya. Jadi tanpa csrf_token, penyerang bisa memanipulasi sesi pengguna dan menjalankan aksi penting di aplikasi seolah-olah berasal dari pengguna tersebut.

11. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, aku membuat kerangka dasar base.html di folder templates dan menyesuaikan settings.py supaya template bisa dikenali. Setelah itu, aku buat main.html yang extend dari base.html untuk menampilkan identitas dan daftar produk.

Selanjutnya, aku definisikan model Product di models.py dengan field seperti title, content, category, thumbnail, is_featured, serta tambahan specification, price, dan product_views. Lalu aku bikin forms.py dengan ProductForm untuk input data produk.

Di views.py, aku buat fungsi show_main (tampilkan semua produk), create_product (form tambah produk), dan show_product (detail produk + increment views). Aku juga menambahkan fungsi untuk menampilkan data dalam format XML/JSON, termasuk berdasarkan id, lengkap dengan try-except agar lebih aman.

Untuk tampilan, aku atur urutannya: nama produk → specification → thumbnail → price → description. Tombol Read More mengarahkan ke detail produk, sementara produk duplikat aku hapus lewat Django Admin.

Terakhir, aku jalankan server, coba tambah produk, cek detail (views bertambah), dan akses endpoint /xml/ serta /json/. Semua sudah berjalan sesuai yang diharapkan meski sempat ada error kecil karena lupa migrate model.

12.  Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada, Ka Fakhri sudah baikk

Link Postman : https://drive.google.com/drive/folders/1da5nmbIka5vAdV5VBieGnO8ewMJClPAa?usp=drive_link


------------------------------------------------TUGAS 4---------------------------------------------------
13.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
django authenticationform adalah form bawaan django yang digunakan untuk proses autentikasi atau login pengguna. form ini sudah menyediakan field username dan password serta dilengkapi dengan validasi dasar, seperti memeriksa apakah akun pengguna terdaftar, apakah kata sandi sesuai, dan apakah akun dalam keadaan aktif. 

kelebihan dari authenticationform adalah praktis karena tidak perlu membuat form login dari awal, aman karena menggunakan sistem validasi django yang sudah teruji, serta mudah diintegrasikan dengan view bawaan seperti loginview. selain itu, form ini juga tetap bisa dikustomisasi sesuai kebutuhan, misalnya untuk menambahkan tampilan atau field tambahan. 

kekurangannya adalah kurang fleksibel apabila sistem login yang dibutuhkan berbeda (misalnya login menggunakan email atau nomor telepon), tampilan default yang sangat sederhana sehingga memerlukan penyesuaian desain, serta tidak mendukung fitur autentikasi modern seperti recaptcha atau two-factor authentication tanpa penambahan manual. dengan demikian, authenticationform sangat berguna untuk kebutuhan login standar, namun untuk kebutuhan yang lebih kompleks biasanya perlu dilakukan pengembangan lebih lanjut.

14.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
autentikasi adalah proses memastikan identitas pengguna (contoh: login dengan username dan password), sedangkan otorisasi adalah proses menentukan hak akses pengguna setelah login (contoh: boleh tambah data atau hanya lihat data).

di django, autentikasi diatur lewat authentication framework yang mengurus login, logout, dan session. sedangkan otorisasi diatur lewat permission dan group, ditambah decorator seperti @login_required atau @permission_required untuk membatasi akses halaman sesuai izin pengguna.

15. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
kelebihan cookies adalah bisa disimpan langsung di browser pengguna, mudah digunakan, dan tidak membebani server. tapi kekurangannya data bisa dilihat atau dimodifikasi oleh user, kapasitasnya kecil, dan rawan masalah keamanan kalau tidak dienkripsi.

kelebihan session adalah data disimpan di server sehingga lebih aman, bisa menyimpan informasi lebih besar dan kompleks, serta sulit dimanipulasi oleh user. kekurangannya butuh resource server lebih banyak karena harus menyimpan data tiap user, dan biasanya bergantung pada cookies atau mekanisme lain untuk menyimpan session id di browser.

16. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
penggunaan cookies tidak sepenuhnya aman secara default karena ada beberapa risiko seperti cookie theft (dicuri lewat xss), session hijacking, atau manipulasi data kalau cookie tidak diamankan. secara bawaan, django sudah punya beberapa mekanisme untuk mengurangi risiko ini, misalnya ada SESSION_COOKIE_HTTPONLY biar cookie tidak bisa diakses lewat javascript, SESSION_COOKIE_SECURE biar cookie hanya dikirim lewat https, serta CSRF tokens untuk cegah serangan cross-site request forgery. tapi pengembang tetap harus hati-hati dengan konfigurasi dan memastikan cookie penting seperti session id selalu dienkripsi dan ditandai secure.

17. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
pertama, aku mulai buat fungsi registrasi supaya pengguna bisa bikin akun baru. di sini pengguna isi username dan password, lalu sistem bakal simpan ke database. begitu akun berhasil dibuat, user bisa login pakai akun tersebut.terus untuk login kurang lebih sama dengan regis tetapi aku menambahkan cookie last_login untuk mencatat kapan terakhir kali pengguna berhasil masuk. fungsi logout kemudian dibuat untuk menghapus session tersebut dan sekaligus menghapus cookie last_login agar tidak ada data sisa setelah keluar.

terus aku ngehubungin product ke user lewat foreignkey, jadi setiap produk harus tahu keterangan authornya siapa. caranya, di tabel product ditambahkan kolom yang mengacu ke tabel user. nah relasi ini disebut foreign key. jadinya, 1 user bisa punya banyak produk, tapi 1 produk hanya bisa punya 1 user sebagai author.

terakhir, aku memperbaiki template detail produk untuk show informasi penulis dengan benar. jika produk memiliki user, maka username pemilik ditampilkan, sedangkan jika tidak, ditampilkan sebagai "anonymous". selain itu, aku juga menambahkan informasi last_login di halaman utama untuk menunjukkan kapan pengguna terakhir kali masuk.
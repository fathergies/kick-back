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

    def __str__(self):
        return self.name


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
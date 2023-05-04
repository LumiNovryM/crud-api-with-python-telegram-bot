## Python Bot Telegram

### Admin Bot
Admin Bot adalah bot admin yang mengatur `Role` dari `Pino Bot`

Berikut adalah Command Dari Admin Bot

1.Start : Perintah /start akan memulai Admin Bot dan Menyalakan Koneksi Server & Database 
```sh
/start

```
<br>

2.Stop : Perintah /stop akan menghentikan Admin Bot dan Memutuskan Koneksi Server & Database
```sh
/stop
```

<br>

3.Profile : Perintah /profile adalah perintah yang digunakan untuk melihat profile Telegram yang terdiri dari Username Telegram & ID Telegram
```sh
/profile
```

<br>

4.Daftar : Perintah /daftar adalah perintah yang digunakan untuk melakukan pendaftaran untuk mendapatkan `Role` `Admin` pada Pino Bot (Pino Bot dan Admin adalah dua bot yang berbeda), Adapun Format pendaftaran terdiri dari `nama-lengkap`, `email`, `status-di-sekolah`. Penulisan nama yang diberi spasi harus disambungkan dengan tanda `-`
```sh
/daftar Lumi-Novry-M luminovrymekel@gmail.com Guru
``` 

<br>

5.List-Admin : Perintah /list-admin adalah perintah yang hanya dapat digunakan oleh `Developer`, yang dimana akan menampilkan list Para Guru yang menjadi `Admin`
```sh
/list-admin
```
<br>
<hr>
<hr>
<hr>

### Pino Bot 
`Pino Bot` adalah `bot` yang akan membantu kegiatan layanan informasi `SMK Taruna Bhakti`

Berikut adalah Command Dari Admin Bot

1.Start : Perintah /start berguna untuk memulai bot 
```sh 
/start
```

<br>

2.List-Kelas : Perintah /list-kelas adalah perintah yang digunakan untuk menampilkan `list-kelas` terdaftar di `SMK Taruna Bhakti`
```sh
/list-kelas
```

<br>

3.List-Guru : Perintah /list-guru adalah perintah yang digunakan untuk menampilkan `list-guru` yang mengajar di `SMK Taruna Bhakti`
```sh 
/list-guru
```

<br>

4.Check-Absensi : Perintah /check-absensi adalah perintah yang digunakan untuk menampilakan absensi kelas berdasarkan 3 `parameter` : `kelas`, `mata-pelajaran`, `tanggal` 
```sh
/check-absensi XI-PPLG-1 Basis-Data 2022-12-24
```

<br>

5.Check-Absensi-Alpha : Perintah /check-absensi adalah perintah yang digunakan untuk menampilkan abseni kelas yang berstatus `Alpha` berdasarkan 3 `parameter` : `kelas`, `mata-pelajaran`, `tanggal` 
```sh
/check-absensi-alpha XI-PPLG-1 Basis-Data 2022-12-24
```


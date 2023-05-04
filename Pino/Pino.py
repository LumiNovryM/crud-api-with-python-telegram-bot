import requests
import json
from Api import Pinobot


# Check If Admin Bot Command Work Successfully
print("Pino Bot Running Successfully")

# Bot Command
@Pinobot.message_handler(commands=['start'])
def start(message):
    Pinobot.reply_to(message, "Halo👋!  Saya Pino Yang Akan Membantu Kegiatan Layanan Informasi Pendidikan SMK Taruna Bhakti")

# List Kelas
@Pinobot.message_handler(commands=['list-kelas'])
def list_kelas(message):
    # Check Status Admin
    # Tele ID
    user_id = message.from_user.id
    # API URL
    url = "http://127.0.0.1:8000/api/list_admin"
    # Melakukan request GET untuk mengambil data dari APi
    response = requests.get(url)
    # Mengubah Data menjadi format JSON
    data = json.loads(response.text)
    # Packing
    data = data['data']
    # Lakukan perulangan untuk cek variabel user_id
    for item in data:
        if item['id_telegram'] == user_id:
            # API URL
            url = "http://127.0.0.1:8000/api/list_kelas"
            # Melakukan request GET untuk mengambil data dari APi
            response = requests.get(url)
            # Mengubah Data menjadi format JSON
            data = json.loads(response.text)
            # Membuat variable untuk hasil final pesan balasan
            final = ""
            for index, kelas in enumerate(data['data'], start=1):
                # Setup Pesan Balasan
                final = final + str(index) + '.)' + 'Kelas : ' + str(kelas['kelas']) + '\n     ' + 'Nama Group : ' + str(kelas['nama_grup']) + '\n     ' + 'Wali Kelas : ' + str(kelas['nama_walas']) + '\n     ' + 'ID Telegram : ' + str(kelas['chat_id']) + '\n' + '\n'
            Pinobot.reply_to(message, "Berikut Adalah List Kelas Yang Terdaftar Di Pino Bot :\n\n" + final)
            break
    else:
        Pinobot.reply_to(message, "Command Ini Hanya Tersedia Untuk Admin")

# List-Guru
@Pinobot.message_handler(commands=['list-guru'])
def list_guru(message):
    # Check Status Admin
    # Tele ID
    user_id = message.from_user.id
    # API URL
    url = "http://127.0.0.1:8000/api/list_admin"
    # Melakuka request GET untuk mengambil data dari APi
    response = requests.get(url)
    # Mengubah Data menjadi format JSON
    data = json.loads(response.text)
    # Packing
    data = data['data']
    # Lakukan perulangan untuk cek variabel user_id
    for item in data:
        if item['id_telegram'] == user_id:
            # API URL
            url = "http://127.0.0.1:8000/api/list_guru"
            # Melakukan request GET untuk mengambil data dari APi
            response = requests.get(url)
            # Mengubah Data menjadi format JSON
            data = json.loads(response.text)
            if not(data):
                Pinobot.reply_to(message, "Data Tidak Ditemukan")
                break
            else:
                # Membuat variable untuk hasil final pesan balasan
                final = ""
                for index, guru in enumerate(data['data'], start=1):
                    # Setup Pesan Balasan
                    final = final + str(index) + '.)' + 'Nama : ' + str(guru['name']) + '\n     ' + 'NIP : ' + str(guru['nip']) + '\n     ' + 'Jenis Kelamin : ' + str(guru['jenis_kelamin']) + '\n     ' + 'E-Mail : ' + str(guru['email']) + '\n     ' + 'No HP : ' + str(guru['no_hp']) +'\n' + '\n'
                Pinobot.reply_to(message, "Berikut Adalah List Guru Yang Terdaftar Di Pino Bot :\n\n" + final)
                break
    else :
        Pinobot.reply_to(message, "Command Ini Hanya Tersedia Untuk Admin")


# Absensi By Hadir
@Pinobot.message_handler(commands=['check-absensi-hadir'])
def check_absensi_hadir(message):
    # Check Status Admin
    # Tele ID
    user_id = message.from_user.id
    # API URL
    url = "http://127.0.0.1:8000/api/list_admin"
    # Melakukan request GET untuk mengambil data dari APi
    response = requests.get(url)
    # Mengubah Data menjadi format JSON
    data = json.loads(response.text)
    # Packing
    data = data['data']
    # Lakukan perulangan untuk cek variabel user_id
    for item in data:
        if item['id_telegram'] == user_id:
            texts = message.text.split(' ')
            kelas = str(texts[1])
            kelas_for_final = kelas.replace('-',' ')
            mapel = str(texts[2])
            mapel_for_final = mapel.replace('-',' ')
            tanggal = str(texts[3])
            # API URL
            url = "http://127.0.0.1:8000/api/absen_siswa_hadir/{}/{}/{}"
            formated_url = url.format(kelas, mapel, tanggal)
            # Melakukan request GET untuk mengambil data dari APi
            response = requests.get(formated_url)
            # Mengubah Data menjadi format JSON
            data = json.loads(response.text)
            if data['data'] is None:
                Pinobot.reply_to(message, "Data Tidak Ditemukan")
                break
            else :
                # Membuat variable untuk hasil final pesan balasan
                final = ""
                for index, absen in enumerate(data['data'], start=1):
                    # Setup Pesan Balasan
                    final = final + str(index) + '.)' + 'Nama : ' + str(absen['nama']) + '\n     ' + 'Jam Masuk : ' + str(absen['jam_masuk']) + '\n     ' + 'Jam Pulang : ' + str(absen['jam_pulang']) + '\n     ' + 'Keterangan : ' + str(absen['kehadiran']) +'\n' + '\n'
                pesan_balasan = "Detail Absensi :\nTanggal : {}\nKelas : {}\nMata Pelajaran : {}\n==================\nDaftar Absensi Siswa:\n{}".format(tanggal, kelas_for_final, mapel_for_final, final)
                Pinobot.reply_to(message, pesan_balasan)
                break
    else :
        Pinobot.reply_to(message, "Command Ini Hanya Tersedia Untuk Admin")

# Absensi By Tidak Hadir
@Pinobot.message_handler(commands=['check-absensi-not-hadir'])
def check_absensi_hadir(message):
    # Check Status Admin
    # Tele ID
    user_id = message.from_user.id
    # API URL
    url = "http://127.0.0.1:8000/api/list_admin"
    # Melakukan request GET untuk mengambil data dari APi
    response = requests.get(url)
    # Mengubah Data menjadi format JSON
    data = json.loads(response.text)
    # Packing
    data = data['data']
    # Lakukan perulangan untuk cek variabel user_id
    for item in data:
        if item['id_telegram'] == user_id:
            texts = message.text.split(' ')
            kelas = str(texts[1])
            kelas_for_final = kelas.replace('-',' ')
            mapel = str(texts[2])
            mapel_for_final = mapel.replace('-',' ')
            tanggal = str(texts[3])
            # API URL
            url = "http://127.0.0.1:8000/api/absen_siswa_not_hadir/{}/{}/{}"
            formated_url = url.format(kelas, mapel, tanggal)
            # Melakukan request GET untuk mengambil data dari APi
            response = requests.get(formated_url)
            # Mengubah Data menjadi format JSON
            data = json.loads(response.text)
            if data['data'] is None:
                Pinobot.reply_to(message, "Data Tidak Ditemukan")
                break
            else :
                # Membuat variable untuk hasil final pesan balasan
                final = ""
                for index, absen in enumerate(data['data'], start=1):
                    # Setup Pesan Balasan
                    final = final + str(index) + '.)' + 'Nama : ' + str(absen['nama']) + '\n     ' + 'Jam Masuk : ' + str(absen['jam_masuk']) + '\n     ' + 'Jam Pulang : ' + str(absen['jam_pulang']) + '\n     ' + 'Keterangan : ' + str(absen['kehadiran']) +'\n' + '\n'
                pesan_balasan = "Detail Absensi :\nTanggal : {}\nKelas : {}\nMata Pelajaran : {}\n==================\nDaftar Absensi Siswa:\n{}".format(tanggal, kelas_for_final, mapel_for_final, final)
                Pinobot.reply_to(message, pesan_balasan)
                break
    else :
        Pinobot.reply_to(message, "Command Ini Hanya Tersedia Untuk Admin")

# Keep Update
Pinobot.polling(none_stop=True)

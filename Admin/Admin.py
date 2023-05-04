# Dependency
import requests
import json
from Api import Adminbot
from datetime import date, datetime


# Bot Command
# Start Bot
@Adminbot.message_handler(commands=['start'])
def start(message):
    Adminbot.send_chat_action(message.chat.id, 'typing')
    if(message.chat.id == 6222136051):
        Adminbot.reply_to(message, "Selamat Datang Kembali Admin")
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

# Stop Server & Databse 
@Adminbot.message_handler(commands=['stop'])
def stop(message):
    Adminbot.send_chat_action(message.chat.id, 'typing')
    if(message.chat.id == 6222136051):
        Adminbot.reply_to(message, "Terima Kasih Sudah Menggunakan Admin Pino Bot🤖")
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

# Profile
@Adminbot.message_handler(commands=['profile'])
def profile(message):
    nama = message.from_user.first_name
    id = message.from_user.id
    Adminbot.reply_to(message, "Berikut Profile Telegram Kamu : \nUsername Telegram : {}\nID Telegram : {}".format(nama, id))

# List Admin
@Adminbot.message_handler(commands=['list-admin'])
def list_admin(message):
    if(message.chat.id == 6222136051):
        # API URL
        url = "http://127.0.0.1:8000/api/list_admin"
        # Melakukan request GET untuk mengambil data dari APi
        response = requests.get(url)
        # Mengubah Data menjadi format JSON
        data = json.loads(response.text)
        # Membuat variable untuk hasil final pesan balasan
        if data is not None and len(data['data']) > 0:
            final = ""
            for index, admin in enumerate(data['data'], start=1):
                # Setup Pesan Balasan
                final = final + str(index) + '.)' + 'Nama : ' + str(admin['nama']) + '\n     ' + 'E-Mail : ' + str(admin['email']) + '\n     ' + 'Status : ' + str(admin['status']) + '\n     ' + 'ID Telegram : ' + str(admin['id_telegram']) + '\n' + '\n'
            Adminbot.reply_to(message, "Berikut Adalah List Admin Yang Terdaftar Di Pino Bot :\n\n" + final)
        else:
            Adminbot.reply_to(message, "Belum ada admin yang terdaftar")
    else :
        Adminbot.reply_to(message, "Command Ini Hanya Untuk Developer\nDeveloper Saya Adalah @lumi_novry")

# Daftar 
@Adminbot.message_handler(commands=['daftar'])
def daftar(message):
    # Tele ID
    user_id = message.chat.id
    # API URL
    url = "http://127.0.0.1:8000/api/list_admin"
    # Melakukan request GET untuk mengambil data dari APi
    response = requests.get(url)
    # Mengubah Data menjadi format JSON
    data = json.loads(response.text)
    # Packing
    data = data['data']
    # print(data)

    # Lakukan perulangan untuk cek variabel user_id
    found = False
    for item in data:
        if user_id in item.values():
            found = True
            break

    if found:
        print("User ID Telegram Pendaftar Sudah Ditemukan")
        Adminbot.reply_to(message, "Maaf, Anda Sudah Terdaftar Menjadi Admin\nGunakan @starbhak_pino_bot Sekarang")
    else:
        print("User ID Telegram Pendaftar Tidak Ditemukan")
        texts = message.text.split(' ')
        chat_id = message.chat.id
        nama = texts[1]
        nama = nama.replace('-', ' ')
        email = texts[2]
        status = texts[3]
        # Setup Data & API
        # URL API Tujuan
        url = "http://127.0.0.1:8000/api/daftar_admin"
        # Mengirimkan data menggunakan request.post()
        response = requests.post(url, {
            "nama" : nama,
            "email" : email,
            "status" : status,
            "id_telegram" : chat_id
        })
        print(response.status_code)
        Adminbot.reply_to(message, "Pendaftaran Berhasil, Sekarang Anda Sudah Menjadi Admin Pino Bot\nGunakan @starbhak_pino_bot Sekarang")




# Keep Update
Adminbot.polling(none_stop=True)
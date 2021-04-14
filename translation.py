class Translation(object):
    START_TEXT = """Halo Kawan
Mau nyari App ID sama Api HASH kah? 🐝
Masukin nomer Telegram mu disini kawan, pake +62 didepannya.

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """Berhasil Kawan🐝
Kirim kesini kode yang telah dikirim oleh pihak telegramnya!

kode ini hanya digunakan untuk tujuan mendapatkan App Id & Api Hash dari my.telegram.org
kalau kamu gak percaya sama bot ini, ke my.telegram.org saja kawan, tapi disana lebih ribet hehe.


/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "Mendapatkan code. Scarpping web page ..."
    ERRED_PAGE = "Terjadi error. Gagal untuk mendapatkan app id. \n\n@BluueBlueSky"
    CANCELLED_MESG = "Dadah! Mohon re /start bot untuk memulai ulang"
    IN_VALID_CODE_PVDED = "Maaf kawan, kode dari telegram yang kamu masukkan tidak valid"
    IN_VALID_PHNO_PVDED = "Maaf kawan, Masukkan nomor dengan awalan kode negara, seperti +62"

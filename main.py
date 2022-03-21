from selenium import webdriver
from datetime import *
from mydata import *
from logger import *
import schedule


def eksekusi(fMatkul, fPertemuan):

    web = webdriver.Chrome()
    web.get(formAbsen)
    today = date.today()

    time.sleep(2)

    nama_field = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nama_field.send_keys(Nama)

    nim_field = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nim_field.send_keys(Nim)

    Matkul_field = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    Matkul_field.send_keys(fMatkul)

    pertemuan_field = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pertemuan_field.send_keys(fPertemuan)

    Tanggal = today.strftime("%m/%d/%y")
    Tanggal_field = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    Tanggal_field.send_keys(Tanggal)

    Kirim = web.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Kirim.click()

    time.sleep(2)

    get_confirm_text = web.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[3]')
    status = get_confirm_text.text
    print(status)
    logging.info(
        'Data:{} - {} - {} - {}, Status: {}'.format(Nama, Nim, fMatkul, fPertemuan, status))
    web.quit()


def getMatkul():
    thisday = datetime.today().strftime('%A')
    if thisday in jadwalkelas:
        # print('ada')
        listmatkul = jadwalkelas[thisday].split(",")
        for x in listmatkul:
            return x
    else:
        return 'tidak ada kelas'


def absen():
    # cek hari apa ini
    thisday = datetime.today().strftime('%A')
    # cek apakah hari ini ada kelas
    if thisday in jadwalkelas:
        # jika ada, ambil kelas di hari itu, submit satu per satu
        listmatkul = jadwalkelas[thisday].split(",")
        for x in listmatkul:
            logging.info(
                'Mensubmisi kelas hari ini: {}'.format(x))
            eksekusi(fMatkul=x, fPertemuan=getPertemuan())
            # print(x)
    else:
        print('tidak ada kelas')


# welcome message
print("Halo, skrip ini akan berjalan setiap hari pukul 20:00")
print("Matkul Hari ini : {}, Pertemuan Minggu Ke: {}".format(
    getMatkul(), getPertemuan()))

# DEBUG Mode
schedule.every(1).minutes.do(absen)

# LIVE mode
# schedule.every().day.at("20:00").do(absen)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    print("Status skrip aktif")
    time.sleep(30)

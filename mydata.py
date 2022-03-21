from cmath import nan
from platform import architecture
import time

Nama = "Aldian Kahfi"
Nim = "2122.02.0003"

# Pertemuan = input("Sebutkan pertemuan Minggu ini dalam angka : ")

# linkabsen
formAbsen = 'https://docs.google.com/forms/d/e/1FAIpQLScHQaUlrLmb06RrClimI_eLv1pCXY38ZmtQHC6zX1gMr2Hocg/viewform?usp=sf_link'

# list matkul

jadwalkelas = {
    "Monday": "Analisa Algoritma",
    "Tuesday": "Data Mining,Social and Interpersonal Skill II ",
    "Wednesday": "Manajemen dan Strategi Bisnis",
    "Thursday": "Sistem operasi",
    "Friday": "Computer Architecture",
    "Saturday": "Struktur Data",
    "Sunday": "Tidak ada Matkul"
}

# Jadwal pertemuan konversi ke EPOCH time. silahkan edit yang di dalam range


def getPertemuan():
    wEpoch = int(time.time())
    # print(wEpoch)
    if wEpoch in range(1647190800, 1647795599):
        return 1
    elif wEpoch in range(1647795600, 1648400399):
        return 2
    elif wEpoch in range(1648400400, 1649005199):
        return 3
    elif wEpoch in range(1649005200, 1649609999):
        return 4
    elif wEpoch in range(1649610000, 1650214799):
        return 5
    elif wEpoch in range(1650214800, 1650819599):
        return 6
    elif wEpoch in range(1650819600, 1651424399):
        return 7
    else:
        return None

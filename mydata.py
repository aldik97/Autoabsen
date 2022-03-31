from cmath import nan
from platform import architecture
import time

import csv


jadwalkelas = {}
with open('jadwal.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (len(row) > 2):
            jadwalkelas[row[0]] = str(row[1]+','+row[2])
        else:
            jadwalkelas[row[0]] = str(row[1])

    # print(jadwalkelas)

akun = {}
with open('akun.csv') as csv_akun:
    csv_reader = csv.reader(csv_akun, delimiter=',')
    for row in csv_reader:
        akun['Nama'] = row[0]
        akun['Nim'] = row[1]
    # linkabsen
formAbsen = 'https://docs.google.com/forms/d/e/1FAIpQLSeopV8HIRIp0BBTgAvESDsbTAcGI7n5_0ksxDXROhWU4wwRgg/viewform'


# Jadwal pertemuan telah dikonversi ke EPOCH time. silahkan edit yang di dalam range (bila perlu)


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

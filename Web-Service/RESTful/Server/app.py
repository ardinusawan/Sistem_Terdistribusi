__author__ = 'DePut'
from flask import Flask, jsonify
import math
import re
import collections
import json
import urllib2

app = Flask(__name__)
temp3 = []
tempc = []
tempoftemp = []
tempoftimec = []
hit = 0
flag = 0



nama_server = "WAWAN_SERVER"

def count(ofile):
    global folder_hasil_computasi, flag, temp3, hit, tempc, tempoftemp, tempoftimec
    temp1 = []
    buka = open(ofile)
    for i, line in enumerate(buka):
        lol = re.split("\W+", line, 8)
        temp1.append('(' + lol[8])
    f = open("cron-copy.txt", 'wb')
    f.writelines(temp1)
    buka.close()
    temp2 = []
    temp_count = []
    with open("cron-copy.txt") as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        temp2.append(line)
        temp_count.append(count)
        # return line, count
    infile.close()
    f.close()

    if hit == 0:
        temp3 = temp2
        tempc = temp_count
        hit = hit + 1
    else:
        tempoftemp = temp2
        tempoftempc = temp_count
        hit = hit + 1


    if hit > 1:
        lentemp = len(tempoftemp)
        lentemp3 = len(temp3)
        cek = 0
        for i in range(lentemp):
            for j in range(lentemp3):
                cek += 1
                if tempoftemp[i] == temp3[j]:
                    tempc[j] += tempoftempc[i]
                    cek = -10;
                if cek == lentemp3 - 1:
                    temp3.append(tempoftemp[i])
                    tempc.append(tempoftempc[i])
            cek = 0

    buka2 = open(ofile)
    fmt = '%-8s%-20s%s'
    fole = open(nama_server, 'w')
    for i, (name, grade) in enumerate(zip(tempc, temp3)):
        data3 = fmt % (i, name, grade)
        fole.write(data3 + "\n")

    buka2.close()
    fole.close()
    coba = str(tempc)
    coba2 = str(temp3)
    coba3 = coba + coba2
    return coba3

tasks = [
    {
        'hasil': count("cron"),
        'hasil2': count("cron.1"),
        'hasil3': count("cron.2"),
        'hasil4': count("cron.3"),
        'hasil5': count("cron.4"),
        'hasil6': count("cron.5"),
        'hasil7': count("cron.6"),
        'hasil8': count("cron.7"),
        'hasil9': count("cron.8"),
        'hasil10': count("cron.9"),
        'hasil11': count("cron.10"),
        'hasil12': count("cron.11"),
        'hasil13': count("cron.12"),
        'hasil14': count("cron.13"),
        'hasil15': count("cron.14"),
        'hasil16': count("cron.15"),
        'hasil17': count("cron.16")

    }
]

tasks2 = [
    {
        'hasil': count("cron.17"),
        'hasil2': count("cron.18"),
        'hasil3': count("cron.19"),
        'hasil4': count("cron.20"),
        'hasil5': count("cron.21"),
        'hasil6': count("cron.22"),
        'hasil7': count("cron.23"),
        'hasil8': count("cron.24"),
        'hasil9': count("cron.25"),
        'hasil10': count("cron.26"),
        'hasil11': count("cron.27"),
        'hasil12': count("cron.28"),
        'hasil13': count("cron.29"),
        'hasil14': count("cron.30"),
        'hasil15': count("cron.31"),
        'hasil16': count("cron.32"),
        'hasil17': count("cron.33")

    }
]

@app.route("/")
def hello_world():
    lol =123
    return jsonify(message = tasks2)

if __name__ == "__main__":
   app.run(host='192.168.43.123', port=5000)

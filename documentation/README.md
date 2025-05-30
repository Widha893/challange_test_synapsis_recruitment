Nama Kandidat   : Widha Rizqika Prasetya
E-Mail          : widharizqikap@gmail.com

Berikut disertakan tata cara run masing-masing program:

+--------+
| Soal 1 |
+--------+

1. Arahkan direktori ke root folder, yaitu challange_test.
2. Jalankan program dengan memasukkan perintah python -m soal_python.soal1.soal1.
3. Masukkan tepat 10 angka, lalu tekan ENTER.

+--------+
| Soal 2 |
+--------+

1. Pastikan library python Flask sudah ter-install.
2. Arahkan direktori ke root folder, yaitu challange_test.
3. Jalankan program dengan memasukkan perintah python -m soal_python.soal2.soal2 pada cmd (cmd perlu dijalankan sebagai administrator); Perintah ini akan menjalankan Flask.
4. Apabila Flask berjalan, akan muncul:
 * Running on http://127.0.0.1:8080 (Press CTRL+C to quit)
5. Buka cmd baru, kemudian jalankan perintah berikut:
curl -X POST -H "Content-Type: application/json" -d "{\"nilai\":(nilai)}" http://127.0.0.1:8080/api/(Nama)
(nilai) dan (Nama) dapat diganti sesuai keinginan.

+--------+
| Soal 3 |
+--------+

1. Pastikan library python requests sudah ter-install.
2. Arahkan direktori ke root folder, yaitu challange_test.
3. Jalankan program dengan memasukkan perintah python -m soal_python.soal3.soal3 pada cmd (cmd perlu dijalankan sebagai administrator).
4. Masukkan nama kota, lalu tekan ENTER.

+--------+
| Soal 4 |
+--------+

1. Pastikan library python paho-mqtt sudah ter-install.
2. Arahkan direktori ke root folder, yaitu challange_test.
3. Jalankan program dengan memasukkan perintah python -m soal_python.soal4.soal4 pada cmd (cmd perlu dijalankan sebagai administrator).
4. Masukkan periode publish data.
5. Untuk melakukan pengecekan apakah data telah ter-publish ke MQTT broker, masuk ke aplikasi test client MQTT, disini saya menggunakan aplikasi yang tersedia di: https://testclient-cloud.mqtt.cool/ lalu subscribe data menggunakan topic yang tepat, yaitu mqtt/Widha/data.

+--------+
| Soal 5 |
+--------+

1. Akses project wokwi melalui link: https://wokwi.com/projects/432391328521284609
2. Tekan Play.
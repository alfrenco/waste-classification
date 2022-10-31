[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8865015&assignment_repo_type=AssignmentRepo)


## Dataset

Dataset yang digunakan kali ini berisi gambar-gambar sampah organic dan anorganic yang diperoleh dari Kaggle dengan [Link](https://www.kaggle.com/datasets/techsash/waste-classification-data)

---


## Objectives

Pengelolaan sampah merupakan salah satu yang harus dihadapi masyarakat sekarang. Banyaknya aktivitas dan kegiatan manusia yang menghasilkan limbah/sampah semakin banyak. Limbah sampah yang menumpuk ini harus dikelola sesuai dengan jenisnya yaitu organic dan anorganic. Saya akan mencoba untuk mengklasifikasikannya menggunakan model CNN yang akan dibuat. Model CNN yang akan dibuat ini diharapkan bisa melakukan klaasifikasi jenis sampah dengan baik sehingga bisa membedakan sampah organic dan anorganic dengan gambar yang ada sehingga sampah tersebut bisa dikelola sesuai jenisnya.

---


## Kesimpulan

Model yang dibuat untuk prediksi adalah 2 model sequential dengan arsitektur yang berbeda. 

`Model baseline` yang dibuat  memiliki convolutional layer sejumlah 2 layer dimana layer pertama memiliki filter 3x3 sejumlah 16 filter sedangkan pada layer kedua jumlah filternya 32. Setelah setiap convolusi saya juga melakukan maxpooling dengan pool 2x2 yang bergeser 2 piksel. Selanjutnya hasil convolusi akan di flatten dimana selanjutnya masuk ke hidden layer pertama dengan jumlah neuron 64 dan terakhir menuju output layer dengan jumlah neuron 1 dan activation sigmoid karena merupakan binary classification. 

`Model baseline`  berhasil mendapatkan accuracy sebesar 0.84 pada test set.

**Label 0 - Organic** :

* Nilai precision 0.87 artinya model berhasil memprediksi 87% label organic ke organic sedangkan 13% sisanya diprediksi sebagai recycle. Nilai recall 0.82 artinya model berhasil memprediksi 82% label organic dengan benar dan 18% sisanya yang seharusnya recycle namun dimasukan ke label organic.

**Label 1 - Recycle** :

* Nilai precision 0.79 artinya model berhasil memprediksi 79% label recycle ke recycle sedangkan 21% sisanya diprediksi sebagai organic. Nilai recall 0.85 artinya model berhasil memprediksi 85% label recycle dengan benar dan 15% sisanya yang seharusnya organic namun dimasukan ke label recycle.

`Model improvement` yang dibuat memiliki convolutional layer sejumlah 3 layer dimana layer pertama memiliki filter 3x3 sejumlah 32 filter sedangkan pada layer kedua jumlah filternya 64 dan pada layer ketiga jumlah filternya sebanyak 128. Setelah setiap convolusi saya juga melakukan maxpooling dengan pool 2x2 yang bergeser 2 piksel. Selanjutnya hasil convolusi akan di flatten dimana selanjutnya masuk ke hidden layer pertama dengan jumlah neuron 128, lalu masuk ke hidden layer kedua dengan jumlah neuron 64, dan terakhir menuju output layer dengan jumlah neuron 1 dan activation sigmoid karena merupakan binary classification.

`Model improvement` ini berhasil mendapatkan accuracy sebesar 0.84 pada test set.

**Label 0 - Organic** :

* Nilai precision 0.87 artinya model berhasil memprediksi 87% label organic ke organic sedangkan 13% sisanya diprediksi sebagai recycle. Nilai recall 0.82 artinya model berhasil memprediksi 82% label organic dengan benar dan 18% sisanya yang seharusnya recycle namun dimasukan ke label organic.

**Label 1 - Recycle** :

* Nilai precision 0.79 artinya model berhasil memprediksi 79% label recycle ke recycle sedangkan 21% sisanya diprediksi sebagai organic. Nilai recall 0.85 artinya model berhasil memprediksi 85% label recycle dengan benar dan 15% sisanya yang seharusnya organic namun dimasukan ke label recycle.

Jadi model hasil improvement yang sudah dibuat berhasil mendapatkan hasil yang cukup baik dan berhasil memprediksi apakah suatu gambar merupakan sampah organic atau anorganic(recycle). 

**Saran** :

Menggunakan dataset yang berisi gambar benda yang sudah berbentuk sampah, bukan benda aslinya yang masih bagus sehingga bisa benar-benar memprediksi gambar sampah saat sudah menjadi bentuk sampah/rusak.




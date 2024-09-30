# Mini-Projek-1-NIM-Genap
DWI PEBRIYANTO PRADANA | 2409116012 | SISTEM INFORMASI A 2024

# Flowchart
![Flowchart - Mini projek 1 - DWI 012(1)](https://github.com/user-attachments/assets/688a548c-7072-484e-a4fb-521541a0d4f8)

# Penjelasan output pada terminal
1. User melakukan Log In dengan memasukan Nama(str), NIM(int), dan PIN
   
   ![Cuplikan layar 2024-09-29 145146](https://github.com/user-attachments/assets/f84b1ea0-fb32-4865-940e-8ed66ee8aec0)

   ![Cuplikan layar 2024-09-29 164119](https://github.com/user-attachments/assets/aff98bf0-58a6-4fe0-97d1-805a630d15f8)

   Jika user salah dalam memasukan PIN program akan selesai
   
   ![output jika login benar](https://github.com/user-attachments/assets/346bc002-6274-4e26-bbd6-13b59bd40ef4)

   Jika user benar dalam memasukan PIN, user akan menuju proses penginputan barang

   sistem login yang digunakan yaitu if & else, dengan user memasukan PIN yang sesuai maka proses akan berlanjut, jika PIN tidak sesuai proses akan berakhir
   
3. setelah berhasil log In user bisa memasukan Nama barang(str), Harga(int) dan jumlahnya(int)
   ![output menginput barang](https://github.com/user-attachments/assets/4b470f29-c075-410b-be15-acead3c34fee)

4. proses perhitungan harga total
   
   ![output jika melebihi 250000](https://github.com/user-attachments/assets/5c7c6030-1cd3-43b9-9797-386fc4af8957)

   output akan menampilkan perkalian barang dengan harga, jika total harga  mencapai dan melebihi 250000 maka akan mendapat diskon 25%

   ![output tidak dapat diskon](https://github.com/user-attachments/assets/56009874-f670-4e3d-a525-d475de7ab56d)

   jika harga total kurang dari 250000 maka tidak mendapat diskon 25%

5. penawaran untuk menginput ulang harga dan jumlah barang
   
   ![output jika melebihi 250000](https://github.com/user-attachments/assets/8fe3ae12-2bf8-43e3-bd68-9d686a1efa08)
   ![Cuplikan layar 2024-09-29 164828](https://github.com/user-attachments/assets/8e4c2a41-4c28-4569-afb8-4597cc35e4f2)

   jika user tidak mengetik sesuai pilihan yang diperintahkan akan muncul tulisan "input tidak sesuai" dan memerintahkan untuk mengetik sesuai pilihan yang disediakan

   ![output jika memilih ya](https://github.com/user-attachments/assets/9058acc0-3547-4393-b5be-ac346bfe557b)

   jika user memilih "YA" user dapat menginput ulang harga dan jumlah barang, sehingga dapat melakukan penghitungan ulang

   ![output jika memilih tidak](https://github.com/user-attachments/assets/5017e925-44fa-452d-884f-bc68ae151ed9)

   jika user memilih "TIDAK" maka proses akan selesai dengan menampilkan total harga terakhir dan ucapan terima kasih

import os
import matplotlib.pyplot as plt

os.system('cls')

class Batik:
    def __init__(self):
        self.batik = {}

    def TambahBatik(self, Produk, Motif, Harga, Ukuran, Stok):
        Ukuran = Ukuran.upper()
        if Ukuran not in ['XL', 'L', 'M']:
            print('Masukkan ukuran yang sudah tertera (XL/L/M)')
            input('Tekan enter untuk kembali...')
            return
        else:
            self.batik[Produk] = {'Produk': Produk, 'Motif': Motif, 'Harga': Harga, 'Ukuran': Ukuran, 'Stok': Stok}
            print(f"Produk {Produk} berhasil ditambahkan.")
            input('Tekan enter untuk melanjutkan...')

    def TampilkanStok(self):
        print("Stok Produk Batik:")
        if self.batik:
            for Produk, info in self.batik.items():
                print(f"Produk: {Produk}, Stok: {info['Stok']}")
            input('Tekan enter untuk melanjutkan...')
        else:
            print("Belum ada produk batik yang tersedia.")
            input('Tekan enter untuk melanjutkan...')

    def TampilkanBatik(self):
        print("Daftar Produk Batik:")
        if self.batik:
            for Produk, info in self.batik.items():
                print(f"Produk: {Produk}, Motif: {info['Motif']}, Ukuran: {info['Ukuran']}, Harga: {info['Harga']}, Stok: {info['Stok']}")
            self.plot_diagram_batang()
        else:
            print("Belum ada produk batik yang tersedia.")
            input('Tekan enter untuk melanjutkan...')

    def PerbaruiMotif(self, Produk, Motif_baru):
        if Produk in self.batik:
            self.batik[Produk]['Motif'] = Motif_baru
            print(f"Motif produk {Produk} berhasil diperbarui.")
            input('Tekan enter untuk melanjutkan...')
        else:
            print(f"Produk {Produk} tidak ditemukan.")
            input('Tekan enter untuk kembali...')

    def PerbaruiUkuran(self, Produk, Ukuran_baru):
        if Produk in self.batik:
            Ukuran_baru = Ukuran_baru.upper()
            while Ukuran_baru not in ['XL', 'L', 'M']:
                print('Masukkan ukuran yang sudah tertera (XL/L/M)')
                Ukuran_baru = input('Masukkan ukuran baru(XL/L/M): ').upper()
            self.batik[Produk]['Ukuran'] = Ukuran_baru
            print(f"Ukuran produk {Produk} berhasil diperbarui.")
            input('Tekan enter untuk melanjutkan...')
        else:
            print(f"Produk {Produk} tidak ditemukan.")
            input('Tekan enter untuk kembali...')

    def PerbaruiHarga(self, Produk, Harga_baru):
        if Produk in self.batik:
            self.batik[Produk]['Harga'] = Harga_baru
            print(f"Harga produk {Produk} berhasil diperbarui.")
            input('Tekan enter untuk melanjutkan...')
        else:
            print(f"Produk {Produk} tidak ditemukan.")
            input('Tekan enter untuk kembali...')

    def PerbaruiStok(self, Produk, Stok_baru):
        if Produk in self.batik:
            self.batik[Produk]['Stok'] = Stok_baru
            print(f"Stok produk {Produk} berhasil diperbarui.")
            input('Tekan enter untuk melanjutkan...')
        else:
            print(f"Produk {Produk} tidak ditemukan.")
            input('Tekan enter untuk kembali...')

    def HapusBatik(self, Produk):
        if Produk in self.batik:
            del self.batik[Produk]
            print(f"Produk {Produk} berhasil dihapus.")
            input('Tekan enter untuk melanjutkan...')
        else:
            print(f"Produk {Produk} tidak ditemukan.")
            input('Tekan enter untuk kembali...')

    def plot_diagram_batang(self):
        produk_list = list(self.batik.keys())
        harga_list = [self.batik[produk]['Harga'] for produk in produk_list]
        plt.figure(figsize=(10, 6))
        plt.bar(produk_list, harga_list, color='skyblue')
        plt.xlabel('Produk')
        plt.ylabel('Harga')
        plt.title('Diagram Batang Harga Produk Batik')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def menu():
    Batiku = Batik()
    while True:
        os.system('cls')
        print('╔════Pilih Opsi Yang Anda Inginkan════╗')
        print('| [1].Tampilkan Semua Produk Batik    |')
        print('| [2].Tambahkan Produk Batik          |')
        print('| [3].Perbarui Produk Batik           |')
        print('| [4].Tampilkan Stok Produk           |')
        print('| [5].Hapus Produk Batik              |')
        print('| [6].Keluar                          |')
        print('╚═════════════════════════════════════╝')
        try:
            pilihan = int(input('Silahkan masukkan pilihan anda (1/2/3/4/5/6): '))
        except ValueError:
            print('Masukkan opsi menggunakan angka!(1/2/3/4/5/6)')
            input('Tekan enter untuk kembali...')
            continue

        if pilihan == 1:
            Batiku.TampilkanBatik()

        elif pilihan == 2:
            Produk = input('Masukkan produk: ')
            Motif = input('Masukkan motif Batik: ')
            Harga = int(input('Masukkan harga(berupa angka): '))
            Ukuran = input('Masukkan Ukuran(XL/L/M): ')
            Stok = int(input('Masukkan Stok: '))
            Batiku.TambahBatik(Produk, Motif, Harga, Ukuran, Stok)

        elif pilihan == 3:
            os.system('cls')
            Batiku.TampilkanBatik()
            Produk = str(input('Masukkan produk yang ingin diperbarui: '))
            if Produk in Batiku.batik:
                while True:
                    os.system('cls')
                    print('╔════Pilih Opsi Yang Anda Inginkan════╗')
                    print('| [1].Perbarui Motif                  |')
                    print('| [2].Perbarui Ukuran                 |')
                    print('| [3].Perbarui Harga                  |')
                    print('| [4].Perbarui Stok                   |')
                    print('| [5].Kembali                         |')
                    print('╚═════════════════════════════════════╝')
                    try:
                        pilih = int(input('Silahkan pilih opsi (1/2/3/4/5): '))
                        if pilih == 1:
                            Motif_baru = input('Masukkan motif baru: ')
                            Batiku.PerbaruiMotif(Produk, Motif_baru)
                        elif pilih == 2:
                            Ukuran_baru = input('Masukkan ukuran baru(XL/L/M): ')
                            Batiku.PerbaruiUkuran(Produk, Ukuran_baru)
                        elif pilih == 3:
                            Harga_baru = int(input('Masukkan harga baru: '))
                            Batiku.PerbaruiHarga(Produk, Harga_baru)
                        elif pilih == 4:
                            Stok_baru = int(input('Masukkan stok baru: '))
                            Batiku.PerbaruiStok(Produk, Stok_baru)
                        elif pilih == 5:
                            break
                        else:
                            print('Opsi yang anda pilih tidak valid.')
                    except ValueError:
                        print('Masukkan opsi menggunakan angka!(1/2/3/4/5)')
                        input('Tekan enter untuk kembali...')
                        continue
            else:
                print(f"Produk {Produk} tidak ditemukan.")

        elif pilihan == 4:
            Batiku.TampilkanStok()

        elif pilihan == 5:
            os.system('cls')
            Batiku.TampilkanBatik()
            Produk = str(input('Masukkan produk yang ingin dihapus: '))
            Batiku.HapusBatik(Produk)

        elif pilihan == 6:
            print('Terima kasih telah menggunakan program ini.')
            break

        else:
            print('Pilihan tidak valid.')

def pembukaan():
    os.system('cls')
    print('!!!Hai selamat datang di RufBatik!!!')
    input('Tekan enter untuk melanjutkan...')
    menu()

pembukaan()

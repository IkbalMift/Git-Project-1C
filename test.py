def tampilkan_daftar(daftar):
    if not daftar:
        print("Daftar belanja kosong.")
    else:
        print("\nDaftar Belanja:")
        for i, item in enumerate(daftar, start=1):
            print(f"{i}. {item}")

def main():
    daftar_belanja = []

    while True:
        print("\nMenu:")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Tampilkan daftar belanja")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            item = input("Masukkan nama item yang ingin ditambahkan: ")
            daftar_belanja.append(item)
            print(f"'{item}' telah ditambahkan ke daftar belanja.")
        
        elif pilihan == '2':
            tampilkan_daftar(daftar_belanja)
            try:
                index = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
                if 0 <= index < len(daftar_belanja):
                    item_hapus = daftar_belanja.pop(index)
                    print(f"'{item_hapus}' telah dihapus dari daftar belanja.")
                else:
                    print("Nomor item tidak valid.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan nomor yang benar.")
        
        elif pilihan == '3':
            tampilkan_daftar(daftar_belanja)
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program daftar belanja!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
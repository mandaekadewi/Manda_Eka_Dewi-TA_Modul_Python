import importlingkara 

# tampilan awal 
print("Pilih bangun ruang yang akan di kerjakan")
print("1.Lingkaran")
print("2.Segitiga")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

#proses
proses = int(input("\n Ketik Pilihan : "))

if proses == 1 :
    print("Hitung Lingkaran")
    r = int(input("Masukan Jari-jari : "))
    importlingkara.lingkaran(r)
elif proses == 2 : 
    print("Hitung Segitiga")
    a = int(input("Masukan Alas Segitiga : "))
    t = int(input("Masukan Tinggi Segitiga : "))
    importlingkara.segitiga(a,t)
    



        



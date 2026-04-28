from huffman import HuffmanCodec

def test_huffman():
    
    test_file = "test_metni.txt"
    mesaj = "bursa uludag universitesi bilgisayar muhendisligi"
    
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(mesaj)
    
    print(f"--- TEST BAŞLIYOR ---")
    print(f"Orijinal Metin: {mesaj}")
    print(f"Orijinal Boyut: {len(mesaj) * 8} bit (ASCII)")

    
    codec = HuffmanCodec(test_file)
    
    
    encoded_mesaj = codec.encode()
    
    print(f"\n--- SIKIŞTIRMA SONUCU ---")
    print(f"Kodlanmış (Bit) Hali: {encoded_mesaj}")
    print(f"Yeni Boyut: {len(encoded_mesaj)} bit")
    
    
    oran = (1 - (len(encoded_mesaj) / (len(mesaj) * 8))) * 100
    print(f"Sıkıştırma Oranı: %{oran:.2f}")

    
     
    decoded_mesaj = codec.decode(encoded_mesaj)
    
    print(f"\n--- GERİ AÇMA SONUCU ---")
    print(f"Çözülen Metin: {decoded_mesaj}")

   
    
    if mesaj == decoded_mesaj:
        print("\nBASARILI: Mesaj kayipsiz bir sekilde geri donduruldu!")
    else:
        print("\nHATA: Mesajlar uyusmuyor, agac yapisini kontrol et.")

if __name__ == "__main__":
    test_huffman()
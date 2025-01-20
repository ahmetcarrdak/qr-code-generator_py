import qrcode

# Kullanıcıdan linki al
data = input("Lütfen QR kodunu oluşturmak istediğiniz linki girin: ")

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,  # Versiyon: QR kodun boyutunu belirler (1-40 arasında)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
    box_size=10,  # Her kutunun piksel boyutu
    border=4,  # Kenar boşluğundaki kutucuk sayısı
)
qr.add_data(data)
qr.make(fit=True)

# QR kodunu bir görüntü olarak oluştur
img = qr.make_image(fill_color="black", back_color="white")

# QR kodunu kaydetme
img.save("qrcode_example.png")

print("QR kod başarıyla oluşturuldu ve kaydedildi!")

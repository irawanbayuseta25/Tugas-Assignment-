def konversi_suhu_ke_fahrenheit(suhu, satuan):
    if satuan.lower() == 'celsius':
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
    elif satuan.lower() == 'kelvin':
        celsius = suhu - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    else:
        raise ValueError("Satuan suhu tidak valid. Gunakan 'celsius' atau 'kelvin'.")

# Contoh penggunaan fungsi
suhu_celsius = 25.0
suhu_kelvin = 298.15

# Panggil fungsi untuk konversi Celsius ke Fahrenheit
hasil_fahrenheit_celsius = konversi_suhu_ke_fahrenheit(suhu_celsius, 'celsius')
print(f"{suhu_celsius} Celsius = {hasil_fahrenheit_celsius:.2f} Fahrenheit")

# Panggil fungsi untuk konversi Kelvin ke Fahrenheit
hasil_fahrenheit_kelvin = konversi_suhu_ke_fahrenheit(suhu_kelvin, 'kelvin')
print(f"{suhu_kelvin} Kelvin = {hasil_fahrenheit_kelvin:.2f} Fahrenheit")

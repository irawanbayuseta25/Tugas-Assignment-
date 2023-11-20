def konversi_fahrenheit_ke_celcius_dan_kelvin(fahrenheit):
    # Konversi Fahrenheit ke Celsius
    celsius = (fahrenheit - 32) * 5/9

    # Konversi Celsius ke Kelvin
    kelvin = celsius + 273.15

    # Mengembalikan tuple suhu dalam format (Celsius, Kelvin)
    return celsius, kelvin

# Contoh penggunaan fungsi
suhu_fahrenheit = 98.6
suhu_celsius, suhu_kelvin = konversi_fahrenheit_ke_celcius_dan_kelvin(suhu_fahrenheit)

print(f"{suhu_fahrenheit} Fahrenheit = {suhu_celsius:.2f} Celsius")
print(f"{suhu_fahrenheit} Fahrenheit = {suhu_kelvin:.2f} Kelvin")

def kelvin_ke_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_ke_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

#Contoh penggunaan konversi Kelvin ke Celsius
suhu_kelvin_input = 300.0
suhu_celsius_hasil = kelvin_ke_celsius(suhu_kelvin_input)

print(f"{suhu_kelvin_input} Kelvin = {suhu_celsius_hasil:.2f} Celsius")

#Contoh penggunaan konversi Celsius ke Kelvin
suhu_celsius_input = 25.0
suhu_kelvin_hasil = celsius_ke_kelvin(suhu_celsius_input)

print(f"{suhu_celsius_input} Celsius = {suhu_kelvin_hasil:.2f} Kelvin")

import csv
from pathlib import Path
import math

input_filename = Path("dbc_deneme.csv")
if not input_filename.exists():
    print("Dosya Bulunamadı!")
    exit(1)

steer_wh_angle,  speed = [],[]


with open(input_filename, mode='r', newline='') as dosya:
    csv_okuyucu = csv.DictReader(dosya)

    for satir in csv_okuyucu:
        steer_wh_angle_column = satir['ActualAngle']
        speed_column = satir['Dsh_VehicleSpeed']
    
        steer_wh_angle.append((steer_wh_angle_column))
        speed.append((speed_column))


steer_wh_angle_yck=[]
for veri in steer_wh_angle:
    if veri != "":
            sayi = float(veri)
            sayi = sayi/(180/math.pi)
            steer_wh_angle_yck.append(sayi)

speed_yck=[]
for veri in speed:
    if veri != "":
            sayi = float(veri)
            speed_yck.append(sayi)


data = list(zip(steer_wh_angle_yck, speed_yck))


csv_file = 'output.csv'

with open(csv_file, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    writer.writerow(['steer_wh_angle', 'speed'])
    writer.writerows(data)

print(f'Data has been written to {csv_file}')
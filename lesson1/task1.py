print('Программа перевод секунд в время')
time_seconds = int(input('Введите время в секундах: '))
print(time_seconds)

time_hours = 0
time_minutes = 0

while time_seconds >= 3600:
    time_hours += 1
    time_seconds -= 3600

while time_seconds >= 60:
    time_minutes += 1
    time_seconds -= 60

final_result = f'{time_hours:02}:{time_minutes:02}:{time_seconds:02}'

print(final_result)
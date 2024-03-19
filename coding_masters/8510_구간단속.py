meter = int(input())
n = int(input())

camera_log = {}
for _ in range(n*2):
    car_num, time = input().split()
    h, m, s = time.split(':')
    time = int(h) * 3600 + int(m) * 60 + int(s)
    
    if camera_log.get(car_num) == None:    
        camera_log[car_num] = [time]
    else:
        camera_log[car_num].append(time)

for key in camera_log:
    camera_log[key] = int(meter / (camera_log[key][1] - camera_log[key][0]) * 3600)

camera_log = sorted(camera_log.items())
for car_num, speed in camera_log:
    print(car_num, speed)
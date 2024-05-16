start_weekday = input()
weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sidx = weekdays.index(start_weekday)
if sidx != 'SUN': weekdays = weekdays[sidx:] + weekdays[:sidx]

n = int(input())
holiday = [tuple(map(int, input().split())) for _ in range(n)]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = [{'red' : 0, 'blue': 0, 'black' : 0} for _ in range(10)]

cnt = 0
for mon, mon_of_days in zip(range(1, 13), days):
    for day in range(1, mon_of_days + 1):
        today = weekdays[cnt]
        cnt += 1

        if (mon, day) in holiday or today == 'SUN': 
            ans[day % 10]['red'] += 1
            if day >= 10: ans[day // 10]['red'] += 1
        elif today == 'SAT': 
            ans[day % 10]['blue'] += 1
            if day >= 10: ans[day // 10]['blue'] += 1
        else:
            ans[day % 10]['black'] += 1
            if day >= 10: ans[day // 10]['black'] += 1
        
        if cnt >= 7: cnt = 0
    
for item in ans: print(*item.values())
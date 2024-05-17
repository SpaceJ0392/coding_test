phone = input().split('-')

if len(phone) != 3:
    print('invalid')
else:
    if (len(phone[0]) != 3 or phone[0] != '010') or len(phone[1]) != 4 or len(phone[2]) != 4:
        print('invalid')
    else:
        print('valid')

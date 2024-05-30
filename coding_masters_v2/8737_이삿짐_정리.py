def check_possibility(boxes):
    # 각 상자에 넣어진 짐의 색을 가져옵니다.
    red_box, green_box, blue_box = boxes

    cnt = 0
    if red_box != 'R': cnt += 1
    if green_box != 'G' : cnt += 1
    if blue_box != 'B': cnt += 1

    print("possible") if cnt != 2 else print("impossible")

# 입력 받기
boxes = input().strip().split()

# 결과 출력
result = check_possibility(boxes)
print(result)

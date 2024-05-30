def is_good_array(N, array):
    position_map = {}
    
    # 각 숫자의 위치를 저장
    for index, value in enumerate(array):
        if value not in position_map:
            position_map[value] = []
        position_map[value].append(index)
    
    # 각 숫자 쌍의 위치를 확인
    for key in position_map:
        positions = position_map[key]
        if len(positions) != 2:
            return "NO"
        first, second = positions
        # 첫 번째와 두 번째 위치 사이에 다른 숫자의 쌍이 같은 패턴인지 확인
        for other_key in position_map:
            if other_key == key:
                continue
            other_positions = position_map[other_key]
            if (first < other_positions[0] < second and second < other_positions[1]) or \
               (other_positions[0] < first and first < other_positions[1] < second):
                return "NO"
    
    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    array = list(map(int, data[1:]))
    
    result = is_good_array(N, array)
    print(result)

if __name__ == "__main__":
    main()

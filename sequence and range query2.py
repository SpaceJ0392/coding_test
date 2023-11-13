arr = [4, 8, 1, 6, 3, 2, 7, 9]
start = 1
end = 4
basis = 6

# arr 리스트에서 start부터 end까지의 요소 중에서 basis보다 큰 값 중에서 가장 작은 값을 찾음
filtered_values = [x for x in arr[start:end + 1] if x > basis]

if filtered_values:
    result = min(filtered_values)
else:
    result = -1

print("가장 작은 값 중에서 basis보다 큰 값:", result)

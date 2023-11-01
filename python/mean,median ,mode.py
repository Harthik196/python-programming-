
data = [16,18,27,16,23,21,19]


mean = sum(data) / len(data)


n = len(data)
sorted_data = sorted(data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]


count_dict = {}
for d in data:
    if d in count_dict:
        count_dict[d] += 1
    else:
        count_dict[d] = 1

mode = [k for k, v in count_dict.items() if v == max(count_dict.values())]


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")


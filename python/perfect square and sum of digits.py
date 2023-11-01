lower_range = int(input(&quot;Enter lower range: &quot;))
upper_range = int(input(&quot;Enter upper range: &quot;))
result = []
for num in range(lower_range, upper_range + 1):
    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num:
        digit_sum = sum(map(int, str(num)))
        if digit_sum &lt; 10:
            result.append(num)
print(result)

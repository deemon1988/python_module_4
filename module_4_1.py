from fake_math import divide as div_fake_m
from true_math import divide as div_true_m

result1 = div_fake_m(3, 0)
result2 = div_fake_m(32,4)
result3 = div_true_m(3, 0)
result4 = div_true_m(42,4)
print(result1)
print(result2)
print(result3)
print(result4)

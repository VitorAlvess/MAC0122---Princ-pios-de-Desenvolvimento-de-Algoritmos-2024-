import re
# Exemplo 1:
t = "12 / 35 + 5/31 * (42/123 +5 / 21) - 8/21"
r = re.findall(r"(\b\d+|[\(\)\+\*\-\/])", t)
print(t)
print(r)
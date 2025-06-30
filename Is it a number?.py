def is_digit(s):
     try:
      float(s.strip())
      return True
     except ValueError:
      return False

print(is_digit("  3  "))
print(is_digit("  3   5"))

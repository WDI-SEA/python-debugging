# Answer found here:
# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
wealth = 1000000000

# No locale, just specify a 1,000's place separator
print(f'{wealth:,}')

# Alternatively, set locale (auto-detected)
import locale
locale.setlocale(locale.LC_ALL, '')
print(f'{wealth:n}')


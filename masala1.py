def solve():
    import sys
    input = sys.stdin.read
    n = input().strip()  # N ni string ko'rinishida o'qish
    result = []

    for char in n:
        if char == '0':
            result.append('1')  # 0 ni 1 bilan almashtirish
        else:
            result.append(char)  # Boshqa raqamlarni o'zicha qoldirish

    # Hosil qilingan natijani qaytarish
    print(''.join(result))

print(f"{'Miles':<10}{'Kilometers':>10}")
for miles in range(1, 11, 1):
    kilometers = miles * 1.609
    print(f"{'Mile ->'+ str(miles):<10}{str(round(kilometers, 3)):>10}")

def findStatistics(values):

    # Mencari nilai maksimum
    max_value = values[0]
    for val in values:
        if val > max_value:
            max_value = val

    # Mencari nilai minimum
    min_value = values[0]
    for val in values:
        if val < min_value:
            min_value = val

    # Mencari rata-rata
    total = 0
    count = 0
    for val in values:
        total += val
        count += 1
    mean_value = total / count

    # Mencari modus
    frequency = {}
    for val in values:
        if val in frequency:
            frequency[val] += 1
        else:
            frequency[val] = 1

    mode_value = None
    mode_count = 0

    for key in frequency:
        if frequency[key] > mode_count:
            mode_count = frequency[key]
            mode_value = key

    # Menampilkan hasil
    print("Value :", values)
    print("Nilai Maksimum :", max_value)
    print("Nilai Minimum :", min_value)
    print("Nilai Rata-Rata :", mean_value)
    print("Nilai Modus :", mode_value)


if __name__ == "__main__":

    print("Masukkan 10 angka dipisahkan dengan spasi:")
    user_input = input()
    value_strings = user_input.split()
    values = []

    for val_str in value_strings:
        values.append(int(val_str))

    if len(values) != 10:
        print("Error: Anda harus memasukkan tepat 10 angka!")
    else:
        findStatistics(values)

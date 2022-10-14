def bin_to_dec(bin_string):
    sum = 0;

    length = len(bin_string) - 1;

    for i in range(length + 1):
        sum += int(bin_string[length - i]) * pow(2, i);

    return sum;
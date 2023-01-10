def calculate_fahrenheit(celcius):
    # HOW TO RUN A TEST/DocString
    # """
    # This function converts temperature in celcius to fahrenheit
    # :param celcius:
    # :return:
    # >>> calculate_fahrenheit(16)
    # 60.8
    # """
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


print(calculate_fahrenheit(16))

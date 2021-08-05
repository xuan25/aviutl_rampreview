while True:
    input_str = input("Input your hex code：")

    hex_string = input_str.strip()
    hex_string = hex_string.replace("#$", "")
    hex_data = bytes.fromhex(hex_string)
    data_str = hex_data.decode("shift-jis")
    print(data_str)


    input_str = input("Input your translation：")

    data_str = input_str.strip()
    hex_data = data_str.encode("gbk")
    hex_string = ''.join(['#$%02X' % hex for hex in hex_data])
    print(hex_string)

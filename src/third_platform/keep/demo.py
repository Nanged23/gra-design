# # unicode_string = r"年度挑战"
# #
# # # 解码为汉字
# # decoded_string = unicode_string.encode('unicode_escape').decode('utf-8')
# #
# # # 打印结果
# # print(decoded_string)
# #
# #
# #
# #
# # unicode_string = r"\u8981\u8bbf\u95ee\u7684\u5185\u5bb9\u4e0d\u5b58\u5728"
# #
# # # 解码为汉字
# # decoded_string = unicode_string.encode('utf-8').decode('unicode_escape')
# #
# # # 打印结果
# # print(decoded_string)


# 汉字字符串
# text = "脱线神话"
#
# # 转换为 UTF-8 编码的字节串
# byte_string = text.encode('utf-8')
#
# # 将字节串转换为 \x 开头的 16 进制字符串形式
# hex_string = ''.join([f'\\x{byte:02x}' for byte in byte_string])
#
# print(hex_string)
#
# text = "30245795"
#
# # 转换为 UTF-8 编码的字节串
# byte_string = text.encode('utf-8')
#
# # 将字节串转换为 \x 开头的 16 进制字符串形式
# hex_string = ''.join([f'\\x{byte:02x}' for byte in byte_string])
#
# # print(hex_string)
# \xe8\x84\xb1\xe7\xba\xbf\xe7\xa5\x9e\xe8\xaf\x9d
# \x33\x30\x32\x34\x35\x37\x39\x35

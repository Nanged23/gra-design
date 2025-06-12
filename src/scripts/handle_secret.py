"""
本代码文件用于将.env文件解密

- 核心算法：AES-256 + Base64编码
- 原理：使用密钥对字符串加密（生成密文）或解密（还原原文），加密后的二进制数据通过Base64转换为可打印字符串。
- 步骤：
    - 密钥处理：输入密钥（任意字符串）通过SHA-256哈希生成256位固定长度密钥（AES要求）。
    - 加密：
        - 对原始字符串进行PKCS7填充，满足AES分块大小（16字节）。
        - 使用AES-256-CBC模式加密（CBC模式需要随机初始向量 IV）。
        - 将IV + 密文拼接后转换为Base64字符串。
    - 解密：
        - Base64解码字符串，分离出IV和密文。
        - 用同一密钥解密，移除填充还原原文。
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from Crypto import Random


class UnicodeCipher:
    def __init__(self, key):
        # 使用SHA-256将密钥统一为32字节
        self.key = SHA256.new(key.encode('utf-8')).digest()

    def encrypt(self, plaintext):
        # 确保正确处理Unicode（中文等）
        plaintext_bytes = plaintext.encode('utf-8')

        # 生成安全的随机IV（16字节）
        iv = Random.get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)

        # 加密并添加PKCS7填充
        ciphertext = cipher.encrypt(pad(plaintext_bytes, AES.block_size))

        # 返回Base64编码的字符串 (IV + 密文)
        return base64.b64encode(iv + ciphertext).decode('ascii')

    def decrypt(self, encrypted_str):
        # Base64解码得到原始字节数据
        data = base64.b64decode(encrypted_str)

        # 分离IV和加密内容
        iv = data[:16]
        ciphertext = data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # 将字节解码为Unicode字符串
        return decrypted_bytes.decode('utf-8')


# 测试包含中文的字符串
key = "这里需要填入密钥！"
cipher = UnicodeCipher(key)

# 加密
# original_text = "真正的环境变量！"
# encrypted = cipher.encrypt(original_text)
# print("\n加密结果:", encrypted)

# 解密
encrypted = "将 .env 中被加密的环境变量内容复制在此，输出转换后的内容 修改下格式放入原文件即可～"
decrypted = cipher.decrypt(encrypted)
print("\n解密结果:", decrypted)

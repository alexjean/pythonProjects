import base64
# string copy from keychain => private key certi => Public Key Info
humanCodes = ["CC 53 3B 26 F1 FF 14 6A F7 B7 1A 2B 43 C1 C9 35 3A CF EE 01 12 70 D4 F4 42 A2 14 B0 51 39 EB 4D",
              "89 8A DA 74 C0 F0 5C 65 CC DA 00 8B D1 32 48 08 AD 89 88 6D FF FC 44 33 1E 2C 39 36 B8 BB 13 5A",
              "C5 E0 CB 2F D2 D3 B0 C3 AD 7A A0 3D 65 EA 7E 9A 8E 2C AD 04 DB 90 DF E6 13 6E DC E6 6C 8E E5 51",
              "D8 65 FF 97 A4 84 12 AA 53 22 84 E7 33 F3 0C 01 B1 47 2E C7 F7 32 00 C1 D3 16 DB C7 02 8D 10 F8",
              "A4 DF B8 B8 50 EC DB 48 C3 04 9E D4 73 56 0D F6 A0 3C B7 75 57 DC 83 7F 19 36 BF C8 0E 61 0B 21",
              "8C F2 BD 28 6A 5E 5B 29 8A 7B A9 E0 8E 8B 03 74 DB F3 97 66 D1 06 FA AF EB 8B 59 33 83 82 1B FA",
              "55 3C 49 A3 AF 26 16 5B D2 22 F6 1F 71 8E AB B2 B9 55 BD 54 F0 D0 48 CA EF CB BC 1B 46 6F 46 8D",
              "26 BE C8 AF 1D EC 16 8D A2 FD B3 41 25 E1 DA D1 17 F4 5D F6 36 2E 3B 59 70 86 6D AE 11 3F 33 99"]


if __name__ == '__main__':
    binaries = bytearray()
    for frag in humanCodes:
        tmp = bytes.fromhex(frag)
        binaries += tmp
    # compare string with exported publickey.pem
    # Header "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA
    # Tail IDAQAB
    string = base64.encodebytes(binaries)
    print(string)
    
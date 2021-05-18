
text = '+��T������Y%�����MMSvÖ"�y3��迶�T1 [=���7ik�.�R2ik�*%�4i�@MB`b%�M�i (������Ԟp����Ć4�i���,��´\�����g�%�YOJDM����\'������}���R����'

# print(text.encode('utf-8').strip())


encodings = ['iso-8859-1']

encoded = text.encode('utf8', errors='replace')#.decode('utf8')

# barr = bytearray(encoded)
# print(barr)
barr = bytearray()
for b in encoded:
  if b < int(b'0xbf', 16):
    barr.append(b)

# final_text = barr.decode('utf8')
# print(final_text)
print(barr)

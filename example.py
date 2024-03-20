import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('14_segment.jpg')
for i in result:
    print(i[1])


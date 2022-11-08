# -*- coding: utf-8 -*-
# Cybernetics Plus Co., Ltd.
# Convert Currency Number to Thai Text

def unit_process(val):
    thai_number = [u"ศูนย์", u"หนึ่ง", u"สอง", u"สาม", u"สี่", u"ห้า", u"หก", u"เจ็ด", u"แปด", u"เก้า"]
    unit = [u"", u"สิบ", u"ร้อย", u"พัน", u"หมื่น", u"แสน", u"ล้าน"]
    length = len(val) > 1
    result = ''

    for index, current in enumerate(map(int, val)):
        if current:
            if index:
                result = unit[index] + result
            if length and current == 1 and index == 0:
                result += u"เอ็ด"
            elif index == 1 and current == 2:
                result = u"ยี่" + result
            elif index != 1 or current != 1:
                result = thai_number[current] + result

    return result

def th_num2text(number):
    sn = str(number)[::-1]
    nl = [sn[i:i + 6].rstrip("0") for i in range(0, len(sn), 6)]
    result = unit_process(nl.pop(0))

    for i in nl:
        result = unit_process(i) + u"ล้าน" + result

    return result
    
def th_baht(nb):
    split_num = str(nb).split(".")
    int_part = int(split_num[0])
    decimal_part = int(split_num[1])
    
    result = th_num2text(int_part) + u"บาท"
    
    if decimal_part>0:
        result += " " + th_num2text(decimal_part) + u"สตางค์"

    return result
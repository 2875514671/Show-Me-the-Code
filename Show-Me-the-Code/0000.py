"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

import string
import random


def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon


def two_hundred_coupons():
    data = ''
    count = 1
    for count in range(200):
        digit = 12
        count += 1
        data += 'coupon no.' + str(count) + ' ' + coupon_creator(digit) + '\n'
    return data


coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
coupondata.close()
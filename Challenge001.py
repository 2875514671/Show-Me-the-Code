# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/qq_35042679/article/details/80629613
"""


def main():
    in_characters = "abcdefghijklmnopqrstuvwxyz"
    out_characters = "cdefghijklmnopqrstuvwxyzab"
    transtab = str.maketrans(in_characters, out_characters)
    # s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
    #     "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    s = 'map'
    p = s.translate(transtab)
    print(p)
    pass


if __name__ == '__main__':
    main()
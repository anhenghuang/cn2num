# -*- coding:utf-8 -*-

common_used_numerals = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9,
                        u'十': 10, u'百': 100, u'千': 1000, u'万': 10000, u'亿': 100000000, u'元': 1.0, u'毛': 0.1, u'分': 0.01,
                        u'两': 2, u'角': 0.1, u'块': 1.0}
numerals = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9}
units = {u'十': 10, u'百': 100, u'千': 1000, u'万': 10000, u'亿': 100000000, u'元': 1.0, u'毛': 0.1, u'分': 0.01, u'两': 2,
         u'角': 0.1, u'块': 1.0}
units_10 = {u'十': u'元', u'百': u'十', u'千': u'百', u'万': u'千', u'亿': u'千万', u'元': u'角', u'毛': u'分', u'角': '分', u'块': u'角'}


def transform(uchars_cn, mode='f'):
    s = uchars_cn
    if len(s) == 0:
        return 0
    if len(s) > 2:
        if s[-1] in numerals:
            if s[-2] in units.keys():
                s = s + units_10[s[-2]]
    if mode in ['f', 'float']:
        return float(cn2digit(s))
    elif mode in ['i', 'int']:
        return int(cn2digit(s))
    else:
        return float(cn2digit(s))


def cn2digit(uchars_cn):
    s = uchars_cn
    if not s:
        return 0
    for i in [u'亿', u'万', u'千', u'百', u'十', u'元', u'块', u'毛', u'角', u'分']:
        if i in s:
            ps = s.split(i)
            lp = cn2digit(ps[0])
            if lp == 0 and i not in [u'元', u'块', u'毛', u'角', u'分']:
                lp = 1
            rp = cn2digit(ps[1])
            return 1.0 * lp * common_used_numerals.get(i[-1], 0) + rp * 1.0
    return 1.0 * common_used_numerals.get(s[-1], 0)


if __name__ == '__main__':
    assert (transform(u"两千七") == 2700)
    assert (transform(u"两万") == 20000)
    assert (transform(u"两千") == 2000)
    assert (transform(u"两毛七") == 0.27)
    assert (transform(u"两毛七分") == 0.27)
    assert (transform(u"两千三百万") == 23000000)
    assert (transform(u"两千三百万零两毛七分") == 23000000.27)

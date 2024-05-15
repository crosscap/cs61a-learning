def nondecreaselist_iter(s):
    res = []
    nondecList = []
    last_num = -1
    for item in s:
        if item >= last_num:
            nondecList.append(item)
        else:
            res.append(nondecList)
            nondecList = [item]
        last_num = item
    return res


def nondecreaselist_recu(s):
    def helper(s, res, nondecList, last_num):
        if s == []:
            return res
        elif s[0] >= last_num:
            nondecList.append(s[0])
        else:
            res.append(nondecList)
        return helper(s[1:], res, nondecList, s[0])
    return helper(s, [], [], -1)

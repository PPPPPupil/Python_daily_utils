"""
排序
"""


def sortByKey(num_list, head=1, tail=-1):
    """
    当list中不仅包含数字，还包含无用字符的话，需要使用数字作为关键字对lisy排序
    :param num_list: 被排序list
    :param head: （正）文件名中，数字之前的无用字符个数（1代表去掉元素中前一个字符）
    :param tail: （负）文件名中，数字之后的无用字符个数(包括“.后缀”)（-1代表去掉元素中最后一个字符）
    :return: 排序后的列表
    """
    num_list.sort(key=lambda x: int(x[head:tail]))
    return num_list


#  copy from https://blog.csdn.net/weixin_34149796/article/details/88901509
# 冒泡排序
def bubbleSort(seq=None, reversed=False):
    lens = len(seq)
    for i in range(lens):
        for j in range(lens - i - 1):
            if (seq[j] < seq[j + 1] if reversed else seq[i] > seq[j]):
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


# 选择排序
def selectionSort(seq=None, reversed=False):
    lens = len(seq)
    for i in range(lens):
        min_index = i
        for j in range(i + 1, lens):
            if (seq[min_index] < seq[j] if reversed else seq[i] > seq[j]):
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]

    return seq


# 插入排序
def insertionSort(seq=None, reversed=False):
    lens = len(seq)
    for i in range(1, lens):
        key = seq[i]
        j = i
        while j > 0 and (seq[j - 1] < seq[j] if reversed else seq[j - 1] > seq[j]):
            seq[j], seq[j - 1] = seq[j - 1], seq[j]
            j -= 1

    return seq


# 归并排序(分）
def mergeSort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])
    return merge(left, right)


# 归并排序（治）
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0

    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


# 快速排序
def quickSort(seq, start, end):
    if start < end:
        split = partition(seq, start, end)
        quickSort(seq, start, split - 1)
        quickSort(seq, split + 1, end)
    return seq


def partition(seq, start, end):
    pivot_index = start - 1
    for i in range(start, end):
        # 选择最右边的为pivot
        if seq[i] < seq[end]:
            pivot_index += 1
            seq[pivot_index], seq[i] = seq[i], seq[pivot_index]
    seq[end], seq[pivot_index + 1] = seq[pivot_index + 1], seq[end]
    return pivot_index + 1

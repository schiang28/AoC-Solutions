from collections import Counter

with open("day7input.txt") as f:
    file = f.read().splitlines()
cards = {i.split()[0]: int(i.split()[1]) for i in file}
rank_order, hands, p2 = 'J23456789TQKA', list(cards.keys()).copy(), True

def sort_cards(c1, c2):
    count1, count2 = Counter(c1), Counter(c2)
    max1, max2, len1, len2 = max(count1.values()), max(count2.values()), len(set(c1)), len(set(c2))
    if p2:
        if 'J' in c1:
            temp1 = Counter(c1)
            del temp1['J']
            if len(temp1) > 0: max1 = max(temp1.values())
            else: max1 = 0
            max1 += count1['J']
            len1 -= 1
        if 'J' in c2:
            temp2 = Counter(c2)
            del temp2['J']
            if len(temp2) > 0: max2 = max(temp2.values())
            else: max2 = 0
            max2 += count2['J']
            len2 -= 1
    if max1 > max2: return -1
    if max2 > max1: return 1
    if max1 == 3 and (len1 < len2): return -1
    if max1 == 3 and (len1 > len2): return 1
    if max1 == 2 and (len1 < len2): return -1
    if max1 == 2 and (len1 > len2): return 1
    else: # the cards are the same type
        for i in range(len(c1)):
            if rank_order.index(c1[i]) > rank_order.index(c2[i]): return -1
            if rank_order.index(c1[i]) < rank_order.index(c2[i]): return 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half, right_half = arr[:mid], arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if sort_cards(left_half[i], right_half[j]) > 0:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sort(hands)
total = sum([cards[hands[i]] * (i+1) for i in range(len(hands))])
print(total)
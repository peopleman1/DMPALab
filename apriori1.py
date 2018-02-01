from collections import Counter
from itertools import combinations
import pickle as cp



def input_transactions():
    trans_list = []
    max_len = -1
    for trans in range(n):
        x = list(map(int, input("Enter items in the transaction (space-separated) >> ").strip().split()))
        trans_list.append(x)
        if len(x)> max_len:
            max_len = len(x)
    cp.dump(trans_list, open("save.p", "wb"))
    return trans_list, max_len


def load_transactions():
    max_len = -1
    trans_list = cp.load(open("save.p", "rb"))
    for i in trans_list:
        if len(i) > max_len:
            max_len = len(i)
    return trans_list, max_len


def apriori(trans_list, max_len, ms):
    final = []
    for i in range(1, max_len):
        cnt = Counter()
        for j in trans_list:
            trans_item_set = combinations(j, i)
            for k in trans_item_set:
                cnt[k] += 1
        print("\n=== ", str(i) + "-Item Set === ")
        for z in cnt:                                   
            if cnt[z] != 0:
                print(z, cnt[z])
                if cnt[z] >= ms:
                    final.append(z)
    return final


n = int(input("Number of transactions >> "))
min_support = int(input("Minimum support >> "))
transactions, max_trans_len = input_transactions()
final_set = apriori(transactions, max_trans_len, min_support)
print(final_set)
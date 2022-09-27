import jieba
import codecs
import OpenHowNet
from os01 import file

hownet_dict = OpenHowNet.HowNetDict()
hownet_dict_advanced = OpenHowNet.HowNetDict(init_sim=True)
# OpenHowNet.download()

f = codecs.open("C:\\Users\\Sun Mengyuan\\Desktop\\外卖评论(1).csv", "r", "utf-8")
lines = f.readlines()

list_p = ["好吃", "可口", "很棒", "方便", "美味", "满意"]
list_n = ["难吃", "恶心", "差", "失望", "坑爹", "难闻"]
aa = []
bb = []
hownet_dict.initialize_similarity_calculation()

# 对bb中的数值进行排序，因为bb中数值交换的同时，aa中的对应元素也要进行交换，故不方便直接使用sort()
for i in range(len(bb)):
    for n in range(0, len(bb) - 1 - i):
        if bb[n] > bb[n + 1]:
            bb[n], bb[n + 1] = bb[n + 1], bb[n]
            aa[n], aa[n + 1] = aa[n + 1], aa[n]

# 去除重复的词语
res_aa = []
res_bb = []
cnt = 0
for i in aa:
    if i not in res_aa:
        res_aa.append(i)
        res_bb.append(bb[cnt])
    cnt = cnt + 1

for i in res_bb:
    print(i)
txt1 = "negative_word.txt"
f = open(txt1, "w")
f.writelines("具有负向情感的前50个单词（除去种子词）如下：\n")
count = 0
for c in res_aa:
    flag = 1
    if count == 50:
        break
    for j in list_n:
        if c == j:
            flag = 0
            break
        else:
            continue
    if flag == 1:
        f.writelines(str(count + 1) + ":" + c + "\n")
        count = count + 1
f.close()

txt2 = "positive_word.txt"
f = open(txt2, "w")
f.writelines("具有正向情感的前50个单词（除去种子词）如下：\n")
res_aa.reverse()
count = 0
for c in res_aa:
    flag = 1
    if count == 50:
        break
    for j in list_p:
        if c == j:
            flag = 0
            break
        else:
            continue
    if flag == 1:
        f.writelines(str(count + 1) + ":" + c + "\n")
        count = count + 1
f.close()

f.close()
test = hownet_dict.calculate_word_similarity("好", "坏")
print("test:" + str(test))

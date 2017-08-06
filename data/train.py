def ou (messege):
    with open('orf_2.txt') as f:
        for st in f:
            if messege == st[0:len(messege)]:
                return st
mess = input()
rm = ou(mess)
print(rm)

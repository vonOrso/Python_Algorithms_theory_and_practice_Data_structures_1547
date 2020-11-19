# def sk(strok):
#     skob = {')': '(', ']': '[', '}': '{'}
#     stek_skob, stek_ind = [],[]
#     c = 1
#     inp = list(strok)
#     for i in inp:
#         if i in skob.values():
#             stek_skob.append(i)
#             stek_ind.append(c)
#             c += 1
#         elif i in skob.keys():
#             if len(stek_skob) != 0:
#                 if stek_skob.pop() == skob[i]:
#                     stek_ind.pop()
#                     c += 1
#                 else:
#                     return c
#             else:
#                 return c
#         else:
#             c += 1
#     return 'Success' if len(stek_skob) == 0 else stek_ind[-1]
#
# print(sk(input()))

# Проверки
# assert sk("([](){([])})") == 'Success'
# assert sk("()[]}") == 5
# assert sk("{{[()]]") == 7
# assert sk("{{{[][][]") == 3
# assert sk("{*{{}") == 3
# assert sk("[[*") == 2
# assert sk("{*}") == 'Success'
# assert sk("{{") == 2
# assert sk("{}") == 'Success'
# assert sk("") == 'Success'
# assert sk("}") == 1
# assert sk("*{}") == 'Success'
# assert sk("{{{**[][][]") == 3

# def poisk(chislo, spis):
#    if chislo not in spis:
#        return chislo
#
# def derev(in1, in2):
#     n = int(in1)
#     strok = list(map(int, in2.split(' ')))
#     korni = map(lambda x: poisk(x,spis=strok), range(n))
#     dlin = []
#     for i in korni:
#         if i != None:
#             c = 0
#             while i != -1:
#                 i = strok[i]
#                 c += 1
#             dlin.append(c)
#     return max(dlin)
#
# print(derev(input(),input()))

# Проверки
# assert derev('10', '9 7 5 5 2 9 9 9 2 -1') == 4
# assert derev('10', '2 2 3 5 5 7 7 9 9 -1') == 6

# from collections import deque
# size_n = deque(map(int, input().split(' ')))
# ochered = deque([0 for i in range(size_n[0])])
# for i in range(size_n[1]):
#     a_d = input().split(' ')
#     a = int(a_d[0])
#     d = int(a_d[1])
#     if ochered[0] <= a:
#         print(a) if ochered[-1] <= a else print(ochered[-1])
#         ochered.append(ochered[-1] + d)
#         ochered.popleft()
#     else:
#         print(-1)

# import sys
# from collections import deque
# stek, stek_maximus = deque([]), deque([])
# maximus = 0
# for i in range(int(input())):
#     strok = sys.stdin.readline()
#     if 'pop' in strok:
#         stek.pop()
#         stek_maximus.pop()
#         maximus = stek_maximus[-1]
#     elif 'max' in strok:
#         print(maximus)
#     else:
#         vhod = int(strok.split(' ')[1])
#         stek.append(vhod)
#         if maximus < vhod:
#             maximus = vhod
#         stek_maximus.append(maximus)

# import sys
# from collections import deque
# kolvo = int(sys.stdin.readline())
# mas = deque(sys.stdin.readline().split(' '))
# kpod = int(sys.stdin.readline())
# vhod, vhod_maxs,vihod, vihod_maxs, rez = [],[],[],[],[]
# mas.append(0)
# mvh, mvih = 0, 0
# x, c = 0, 0
# for i in range(kpod):
#     z = int(mas.popleft())
#     vhod.append(z)
#     if mvh < z:
#         mvh = z
#
#     vhod_maxs.append(mvh)
# kolvo -= kpod
# while kolvo != -1:
#     if x == 0:
#         z = vhod.pop()
#         vihod.append(z)
#         if mvih < z:
#             mvih = z
#         vihod_maxs.append(mvih)
#         c += 1
#     elif x == 1:
#         vihod.pop()
#         z = vihod_maxs.pop()
#         rez.append(str(z)) if z > mvh else rez.append(str(mvh))
#         och = int(mas.popleft())
#         vhod.append(och)
#         if mvh < och:
#             mvh = och
#         vhod_maxs.append(mvh)
#         kolvo -= 1
#         c -= 1
#
#     if c == kpod:
#         x = 1
#         mvh = 0
#     elif c == 0:
#         x = 0
#         mvih = 0
#
# print(' '.join(rez))

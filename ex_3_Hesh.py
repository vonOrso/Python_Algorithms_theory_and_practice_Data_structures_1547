# import sys
#
# knigga = {}
# for i in range(int(sys.stdin.readline())):
#     zapros = sys.stdin.readline().split(' ')
#     zapros[-1] = zapros[-1].replace('\n','')
#     if zapros[0] == 'add':
#         knigga[zapros[1]] = zapros[2]
#     elif zapros[0] == 'find':
#         if zapros[1] in knigga.keys():
#             print(knigga[zapros[1]])
#         else:
#             print('not found')
#     else:
#         if zapros[1] in knigga.keys():
#             knigga.pop(zapros[1])

# import sys
# from collections import deque
#
# def schet(slovo, hesh):
#     vkod = list(slovo)
#     tab = 0
#     for z in range(len(vkod)-1):
#         tab += ord(vkod[z]) * (263 ** z)
#     tab %= 1000000007
#     tab %= hesh
#     return tab
#
# raz_hesh = int(sys.stdin.readline())
# tablicy = deque([deque([]) for i in range(raz_hesh)])
# for i in range(int(sys.stdin.readline())):
#     zapros = sys.stdin.readline().split(' ')
#     if zapros[0] == 'add':
#         tab = schet(zapros[1], raz_hesh)
#         if zapros[1] not in tablicy[tab]:
#             tablicy[tab].appendleft(zapros[1])
#
#     elif zapros[0] == 'find':
#         tab = schet(zapros[1], raz_hesh)
#         if zapros[1] in tablicy[tab]:
#             print('yes')
#         else:
#             print('no')
#
#     elif zapros[0] == 'check':
#         print(' '.join(tablicy[int(zapros[1])]))
#
#     else:
#         tab = schet(zapros[1], raz_hesh)
#         if zapros[1] in tablicy[tab]:
#             tablicy[tab].remove(zapros[1])

# import sys
#
# def ne_rabina_karpa(str_pattern, str_text):
#     otv = ''
#     len_patt = len(str_pattern)
#     len_text = len(str_text)
#     list_patt = list(str_pattern)
#     hesh_patt = 0
#     for z in list_patt:
#         hesh_patt += ord(z)
#
#     hesh_per = 0
#     str_per = str_text[:len_patt]
#     for z in str_per:
#         hesh_per += ord(z)
#
#     if hesh_patt == hesh_per:
#         if str_pattern == str_per:
#             otv += ' 0'
#
#     for i in range(len_patt, len_text):
#         hesh_per += ord(str_text[i]) - ord(str_text[i - len_patt])
#         if hesh_per == hesh_patt:
#             if str_text[i - len_patt + 1:i + 1] == str_pattern:
#                 otv += ' ' + str(i - len_patt + 1)
#
#     return otv[1:]
#
# str_pattern = sys.stdin.readline().replace('\n', '')
# str_text = sys.stdin.readline().replace('\n', '')
# print(ne_rabina_karpa(str_pattern, str_text))
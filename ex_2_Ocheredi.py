# import sys
# kolvo = int(sys.stdin.readline())
# mas = list(map(int,sys.stdin.readline().split(' ')))
# mas = [0] + mas
# otvet = []
# c = 0
# def sftdown(i):
#     ind_min = i
#     lft = 2*i
#     if lft <= kolvo and mas[lft] < mas[ind_min]:
#         ind_min = lft
#     rgt = 2*i+1
#     if rgt <= kolvo and mas[rgt] < mas[ind_min]:
#         ind_min = rgt
#     if i != ind_min:
#         otvet.append(str(i-1) + ' ' + str(ind_min-1))
#         new_roditel = mas[ind_min]
#         new_potomok = mas[i]
#         mas[i] = new_roditel
#         mas[ind_min]= new_potomok
#         sftdown(ind_min)
#
# for z in range(kolvo//2,0,-1):
#     sftdown(z)
#
# print(len(otvet))
# for z in otvet:
#     print(z)

# import queue
# import sys
#
# proc_kolv = sys.stdin.readline().split(' ')
# ochered = sys.stdin.readline().split(' ')
# proc = int(proc_kolv[0])
# kolv = int(proc_kolv[1])
# derevo = queue.PriorityQueue()
#
# for z in range(proc):
#     derevo.put([0,proc,z])
# for x in ochered:
#     x = int(x)
#     verh = derevo.get()
#     if x < 1:
#         print(verh[2], verh[0])
#         derevo.put(verh)
#         continue
#     else:
#         print(verh[2], verh[0])
#         verh[0] += x
#         derevo.put(verh)

# import sys
#
# def find(i):
#     if i != parent[i]:
#         parent[i] = find(parent[i])
#     return parent[i]
#
# def union(i,j):
#     i_id = find(i)
#     j_id = find(j)
#     new = 0
#     if i_id != j_id:
#         parent[j_id] = i_id
#         znacheniya[i_id] += znacheniya[j_id]
#         new = znacheniya[i_id]
#
#     return new
#
# cif_oper = sys.stdin.readline().split(' ')
# dano_cif = sys.stdin.readline().split(' ')
# cif = int(cif_oper[0])
# oper = int(cif_oper[1])
# znacheniya = list(map(int, dano_cif))
# parent = [i for i in range(cif)]
# maxim = max(znacheniya)
# for i in range(oper):
#     destination_source = sys.stdin.readline().split(' ')
#     destination = int(destination_source[0]) - 1
#     source = int(destination_source[1]) - 1
#     new = union(destination, source)
#     if new > maxim:
#         maxim = new
#
#     print(maxim)

# import sys
#
# def find(i):
#     if i != parent[i]:
#         parent[i] = find(parent[i])
#     return parent[i]
#
# def union(i,j):
#     i_id = find(i)
#     j_id = find(j)
#     if i_id != j_id:
#         parent[j_id] = i_id
#
#
# def prover():
#     for z in range(d):
#         i_j = sys.stdin.readline().split(' ')
#         i = int(i_j[0]) - 1
#         j = int(i_j[1]) - 1
#         if find(i) == find(j):
#             return 0
#
#     return 1
#
# n_e_d = sys.stdin.readline().split(' ')
# n = int(n_e_d[0])
# e = int(n_e_d[1])
# d = int(n_e_d[2])
# parent = [z for z in range(n)]
# for z in range(e):
#     i_j = sys.stdin.readline().split(' ')
#     i = int(i_j[0]) - 1
#     j = int(i_j[1]) - 1
#     union(i,j)
#
# print(prover())

# import sys
#
# def preorder(derev, indox):
#     verh = derev[indox]
#     otv_pre.append(verh[0])
#     lev, prav = verh[1], verh[2]
#     if lev != -1:
#         preorder(derev, lev)
#     if prav != -1:
#         preorder(derev, prav)
#
# def inorder(derev, indox):
#     verh = derev[indox]
#     lev, prav = verh[1], verh[2]
#     if lev != -1:
#         inorder(derev, lev)
#     otv_in.append(verh[0])
#     if prav != -1:
#         inorder(derev, prav)
#
# def postorder(derev, indox):
#     verh = derev[indox]
#     lev, prav = verh[1], verh[2]
#     if lev != -1:
#         postorder(derev, lev)
#     if prav != -1:
#         postorder(derev, prav)
#     otv_post.append(verh[0])
#
# kolvo = int(sys.stdin.readline())
# derev = {}
# schet = 0
# otv_pre, otv_in, otv_post = [], [], []
# for i in range(kolvo):
#     strok = sys.stdin.readline().split(' ')
#     derev[i] = [strok[0], int(strok[1]), int(strok[2])]
#
# inorder(derev, 0)
# preorder(derev, 0)
# postorder(derev, 0)
# print(' '.join(otv_in))
# print(' '.join(otv_pre))
# print(' '.join(otv_post))
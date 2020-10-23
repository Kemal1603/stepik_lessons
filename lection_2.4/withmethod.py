with open ('sample.txt') as f:
    for line in f:
        line = line.rstrip()
        print(line)

#  Данный способ чтения\записи рекомендуется, так как  в этом методе нет необходимости следить за тем, что бы файл был
# закрыт. При желении можно открывать несколько файлов, через запятую сразу для чтения и для записи, например:
#
# with open ('sample.txt') as f, open('sample2.txt','w') as second_f:
#     for line in f:
#         line = line.rstrip()
#         print(line)
#     second_f.write('asdfsdfsf')

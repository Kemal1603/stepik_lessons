with open('/home/kemal/Downloads/dataset_24465_4.txt', 'r') as read_file:
    lst = read_file.readlines()[::-1]

with open('/home/kemal/Downloads/dataset_24465_4.txt', 'w') as w_file:
    for line in lst:
        w_file.write(line)

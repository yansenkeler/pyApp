import tools

loop = True
no = 1
fo = open('prime_table.txt', 'w+')
while no <= 1000000:
    prime = tools.nth_prime(no)
    print(no, prime)
    fo.write(str(prime)+',')
    no += 1
fo.close()

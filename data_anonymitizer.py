import os

for p in range(1, 21):
    # print p
    for t in range (1, 21):
        f_in = open('p' + str(p) + '/' + str(t) + '.txt')
        f_out = open('p' + str(p) + '/' + str(t) + '.csv', 'w')

        line_cnt = 0 
        for line in f_in.readlines():
            line_cnt += 1
            if line_cnt == 1 or line_cnt == 2 or line_cnt == 3:
                print line
            else:
                f_out.write(line)
        f_in.close()
        f_out.close()

        os.remove('p' + str(p) + '/' + str(t) + '.txt')
        
            

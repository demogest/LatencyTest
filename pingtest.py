from functools import reduce
import subprocess,os,sys
# if os.path.exists(sys.argv[0]+'/ping.txt'): 
#     subprocess.Popen(['del',sys.argv[0]+'/ping.txt'])
# p = subprocess.Popen(['ping','-n','10','192.168.73.1'],stdout=subprocess.PIPE)
# inp = p.stdout
file = open("ping.txt",'r',encoding='utf8')
# for line in inp:
#     line = line.decode('gbk')
#     file.write(line)
tot,sum, buff= 0,0,[]
file.seek(0,0)
for line in file:
    if ':' not in line or 'ms' not in line:
        continue
    tot+=1
    line = ((line.split(':')[1][:-1]).split(' ')[1:][1])
    if line[2] == '<':
        continue
    line = line.split('=')[1][:-2]
    buff.append(int(line))
sum = reduce(lambda x,y:x+y,buff) /len(buff)
print("Average:{:.2f}ms\nMax:{:.2f}ms\nMin:{:.2f}ms\n{}\\{} above average\n{}\\{} above 100ms".format(sum,max(buff),min(buff),len(list(filter(lambda x:x>sum,buff))),tot,len(list(filter(lambda x:x>100,buff))),tot))
stab = len(list(filter(lambda x:x>sum,buff))) / len(buff)
print("Excess rate:{:.2f}%".format(stab*100))
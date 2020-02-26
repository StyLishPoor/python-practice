cap1 = ['F','F','B','B','B','F','B',
        'B','B','F','F','B','F']
cap2 = ['F','F','B','B','B','F','B',
        'B','B','F','F','F','F']

def pleaseConform_2path(cap):
    group_f = []
    group_b = []
    group_start = 0
    for i in range(len(cap)-1):
        if(cap[i] != cap[i+1]):
            if(cap[i] == 'F'):
                group_f.append([group_start,i])
            else:
                group_b.append([group_start,i])
            group_start = i+1
    #最後の要素
    if(cap[-1] == 'F'):
        group_f.append([group_start,len(cap)-1])
    else:
        group_b.append([group_start,len(cap)-1])

    return group_f,group_b

def pleaseConform_1path(cap):
    major_flip = cap[0]
    caps = cap + ["eof"]
    start = 0
    for i in range(1,len(cap)):
        if(caps[i] != major_flip):
            if(cap[i-1] == major_flip):
                start = i
            elif(caps[i+1] == major_flip):
                if(start == i):
                    print("Person in position " +str(start)+ ", please flip your caps")
                else:
                    print("Person in position " +str(start)+ " through " +str(i)+ ", please flip your caps") 
            
            


group_f,group_b = pleaseConform_2path(cap2)
"""
if(len(group_f) > len(group_b)):
    for i in range(len(group_b)):
        if(group_b[i][0] == group_b[i][1]):
            print("Person in position " +str(group_b[i][0])+ ", please flip your caps")
        else:
            print("Person in position " +str(group_b[i][0])+" through " +str(group_b[i][1])+ ", please flip your caps")
else:
    for i in range(len(group_f)):
        if(group_f[i][0] == group_f[i][1]):
            print("Person in position " +str(group_f[i][0])+ ", please flip your caps")
        else:
            print("Person in position " +str(group_f[i][0])+" through " +str(group_f[i][1])+ ", please flip your caps")        
"""
if(len(group_f) > len(group_b)):
    group_change = group_b
else:
    group_cahnge = group_f
for i in range(len(group_b)):
        if(group_change[i][0] == group_change[i][1]):
            print("Person in position " +str(group_change[i][0])+ ", please flip your caps")
        else:
            print("Person in position " +str(group_change[i][0])+" through " +str(group_change[i][1])+ ", please flip your caps")

pleaseConform_1path(cap2)

'''
count char in string
if there is duplicate char, return ?
'''
import operator

def cnt(str):
    lowStr = str.lower()
    dic = dict()
    
    # make dic
    for i in lowStr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
    
    # validate if ? or Num
    if sorted_dic[-1][1] == sorted_dic[-2][1]:
        return '?', sorted_dic[-1][1]
    else:
        return sorted_dic[-1][0], sorted_dic[-1][1]
    
def main():
    print(cnt('jaZz'))
    
    print(cnt('miSsisSippi'))

if __name__ == '__main__':
    main()
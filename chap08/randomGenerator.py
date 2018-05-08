#!/bin/python3
# coding: utf-8

#生成随机试卷并写入文件，将答案写入文件

import random

capitals = {
    '四川': '成都',
    '重庆': '重庆',
    '贵州': '贵阳',
    '云南': '昆明',
    '湖南': '长沙',
    '湖北': '武汉',
    '广西': '南宁',
    '广东': '广州',
    '福建': '福州',
    '浙江': '杭州',
    '山东': '济南',
    '山西': '太原',
    '河北': '石家庄',
    '河南': '郑州'
}


def gen(n):
    N = n
    
    #生成试卷
    for examNum in range(N):
        #创建试卷和答案
        exam = open('%s.exam' % (examNum+1), 'w')
        answer = open('%s.ans' % (examNum+1), 'w')

        #写入试卷头部信息
        exam.write('姓名:\n\n学号:\n\n日期:\n\n')
        exam.write((' ' * 30)+'试卷 %s' % (examNum +1))
        exam.write('\n\n')

        answer.write(' '*30 + '答案: %' % (examNum+1))
        answer.write('\n\n')
        #省份和省会
        provices = list(capitals.keys())

        #打乱
        random.shuffle(provices)


        #生成答案
        for questionNum in range(len(provices)):
            correctAns = capitals[provices[questionNum]]
            allAns = list(capitals.values())
            del allAns[allAns.index(correctAns)]
            wrongAns = random.sample(allAns, 3)
            ansOptions = wrongAns+[correctAns]

            random.shuffle(ansOptions)

            #写入内容
            exam.write('%: %s省的省会是哪个城市? \n' % (questionNum+1, provices[questionNum])

            for i in range(4):
                exam.write(' %s: %s \n' % ('ABCD'[i], ansOptions[i]))
            exam.write('\n')

            answer.write('%s: %s \n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAns)]))


        exam.close()
        answer.close()



gen(20)



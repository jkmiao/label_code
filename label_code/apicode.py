#!/usr/bin/env python
# coding=utf-8

import os
import random 

class Apicode(object):

    def __init__(self, path='./static/uploads'):
        totalImg = [os.path.join(path, fname) for fname in os.listdir(path)]
        finished = [fname for fname in totalImg if fname.find('_')>1 ]
        self.unfinished = [fname for fname in totalImg if fname not in finished]
        
        self.label_msg = {}
        self.label_msg['city'] = '探迹'
        self.label_msg['totalCnt'] = len(totalImg)
        self.label_msg['finishedCnt'] = len(finished)


    def get_labelmsg(self, fname='', result=''):

        if fname in self.unfinished and len(result)>1:
            newName = './static/uploads/%s_%s.jpg' % (result, fname.split('/')[-1].split('.')[0])
            if os.path.exists(fname):
                os.rename(fname, newName) # 更新名字
                self.unfinished.remove(fname)
                self.label_msg['finishedCnt'] += 1
                
        if self.unfinished:
            self.label_msg['fname'] = random.choice(self.unfinished)
        else:
            self.label_msg['fname'] = 'none'

        return self.label_msg

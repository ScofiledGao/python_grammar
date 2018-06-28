# -*- coding:UTF-8 -*-
import requests
import re
import random
from bs4 import BeautifulSoup

def get_qiushibaike():
  content = requests.get('http://www.qiushibaike.com').content
  soup = BeautifulSoup(content, 'html.parser')

  for div in soup.find_all('div', {'class':'content'}):
      print div.text.strip()

def demo_string():
  stra='hello world'
  print stra.capitalize()
  print stra.replace('world','Gaoqisong')

  strb = '\n\rhello gaoqisong \r\n'
  print 1, strb.lstrip()
  print 2, strb.rstrip()

  strc = 'hello w'
  print 3, strc.startswith('hel')
  print 4, strc.endswith('x')
  print 5, stra+strb+strc
  print 6, len(strc)
  print 7, '-'.join(['a','b','c'])
  print 8, strc.split(' ')

def demo_operation():
  print 1, 1+2,5/2,5*2,5-2
  print 2, True,not True
  print 3, 1<2,55>2
  print 4, 2<<3
  print 5, 5 | 3,5 & 3,5^3
  x = 2
  y = 3.3
  print x, y,type(x),type(y)

def demo_builtInFunc():             #内置函数
  print 1, max(2, 1), min(5, 3)
  print 2, len('xxx'), len([1, 2, 3])
  print 3, abs(-2)  # 绝对值
  print 4, range(1, 19, 3)
  print 5, dir(list)
  x = 2
  print 6, eval('x+3')
  print 7, chr(65), ord('a')
  print 8, divmod(11, 3)

def demo_controlFlow():
  score =65
  if score > 99:
    print 1, 'A'
  elif score > 60:
    print 2, 'B'
  else:
    print 3, 'C'

  while score < 100:
    print score
    score += 10
  score = 65

  for i in range(0,10,2):
    if i ==0:
      pass    #do_specail
    if i<5:
      continue
    print 3,i
    if i == 8:
      break

def demo_list():
  lista = [1,2,3]  #vector   Arraylist
  print 1, lista
  listb = ['a',1,'c',1.1]
  print 2,listb
  lista.extend(listb)
  print 3,lista
  print 4, len(lista)
  print 5, 'a' in listb
  lista = lista+listb
  print 6,lista
  listb.insert(0,'www')
  print 7, listb
  listb.pop(1)
  print 8,listb
  listb.reverse()
  print 9, listb
  print 10, listb[0],listb[1]
  listb.sort()
  print 11,listb
  list.sort(reverse=True)
  print 12,listb
  print 13,listb*2
  print 14,[0]*4

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def demo_dict():
  dicta = {1:1,2:4,3:9}
  print 1,dicta
  print 2,dicta.keys(),dicta.values()
  print 3,dicta.has_key(1),dicta.has_key('3')
  for key,value in dicta.items():
    print 'key-value:',key,value

  dictb = {'+':add,'-':sub}
  print 4, dictb['+'](1,2)
  print 5,dictb.get('-')(15,3)
  dictb['*']='x'
  print dictb
  dicta.pop(1)
  print 6,dicta
#  del dicta[1]
  print 7, dicta


def demo_set():
  seta = set((1,2,3))
  setb = set((2,3,4))
  print 1,seta
  #seta.add(4)
  print 2,seta
  print 3, seta.intersection(setb),seta&setb
  print 4,seta | setb, seta.union(setb)
  print 5,seta-setb
  seta.add('x')
  print 6, seta


class User:
  type = 'USER'
  def __init__(self,name,uid):
    self.name = name
    self.uid = uid
  def __repr__(self):
    return 'im\t'+self.name+'\t'+str(self.uid)

class Admin(User):
  type = 'ADMIN'

  def __init__(self,name,uid,group):#初始化函数
    User.__init__(self,name,uid)
    self.group =group
  def __repr__(self):
    return 'im\t'+self.name+'\t'+str(self.uid)+'\t'+self.group


def demo_exception():
  try:
    print 2/1
    #print 2/0
    raise Exception('Raise Error','aaa')    #自己主动抛出一个异常
  except Exception as e:
    print 'error:',e
  finally:
    print 'clear up'

#随机数
def demo_random():
  #random.seed(1)    #总值----幂等性
  #1--100
  print 1, int(random.random()*100)
  print 2, random.randint(0,100)
  print 3, random.choice(range(0,100,1))
  print 4, random.sample(range(0,100),5)
  a=[1,2,3,4,5,6]
  random.shuffle(a)
  print 5, a

#正则表达式
def demo_re():
  str = 'abc123def456fghi789'
  p1 = re.compile('[\d]+')#模式    \d：数字  \D:非数字  \s:空格、\t、\r等  \w:0~9、a~z
  print 1, p1.findall(str)
  p2 = re.compile('[\d]')
  print 2,p2.findall(str)

  str1 = 'a0@163.com;b1@163.com;c2@qq.com;e3@qq.com;f4@163.com'
  p3 = re.compile('[\w]+@[163|qq]+\.com')
  print 3,p3.findall(str1)

  str2 = '<html><h>title</h><body>xxxxxx</body></html>'
  p4 = re.compile('<h>[^<]+</h>')
  print 4, p4.findall(str2)

  p5 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')#()指定要找的部分
  print 5, p5.findall(str2)

  str3 = 'xxx2018-06-28xx'
  #p5= re.compile('\d\d\d\d-\d\d-\d\d')
  p5= re.compile('\d{4}-\d{2}-\d{2}')
  print 6, p5.findall(str3)

if __name__ == '__main__':
  #demo_string()
  #demo_operation()
  #demo_builtInFunc()
  #demo_controlFlow()
  #demo_list()
  #demo_dict()
  #demo_set()
  '''
  user  = User('u1',1)
  print user
  admin = Admin('a1',101,'HR')
  print admin
  demo_exception()
  '''
  #demo_random()
  demo_re()
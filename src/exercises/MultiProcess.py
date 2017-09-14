#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue,Pipe
import os, time, random
from time import sleep
"""Queue 执行方法"""
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

"""pipes 执行方法"""

def send(conn):
    print('Process to send: %s' % os.getpid())
    for i in range(10):
        conn.send([42, None, 'hello' + str(i)])
        sleep(1)
    conn.close()

def recv(conn):
    print('Process to recv: %s' % os.getpid())
    while True:
        print(conn.recv())
        

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    """Queue"""
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    
    """Pipes"""
    pt1,pt2 = Pipe()
    ps = Process(target=send, args=(pt1,))
    pr = Process(target=recv, args=(pt2,))
    # 启动子进程pw，写入:
    ps.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    ps.join()

# encoding: utf-8


import argparse


parser = argparse.ArgumentParser(description="多线程拉取物料正排信息")
# 1. positional arguments，位置参数，定义了类型，参数范围，参数默认值
parser.add_argument("thread_num", type=int, choices=[i for i in range(1, 11)],
                    default=6, help="the thread num, 1~10")
# 2. optional arguments，可选参数
# action="store_true"，如果命令行中出现 -v(可以只出现 -v，不必要出现参数值)，则 debug 的值为 True，否则为 False
parser.add_argument("-i", "--input", help="input filename")
parser.add_argument("-o", "--output", help="output filename")
parser.add_argument("-d", "--debug", help="debug switch", action="store_true")
# 3. 互斥参数
# 定义了一组互斥参数，可以都不带，也可以只带一个，不可以都带
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
group.add_argument("-q", "--quiet", help="silent mode", action="store_true")
args = parser.parse_args()


print(args.thread_num)
print(args.input)
print(args.output)
print(args.debug)
print(args.verbose)
print(args.quiet)


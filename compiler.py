import sass
import sys
import os
from multiprocessing import Pool, cpu_count

reload(sys)
sys.setdefaultencoding('utf8')

PATH = "../web-project/skins/"


def compile_file(name):
    # print name
    try:
        # outfile = open("../web-project/skins/" + name + "/sass/skin.scss", 'r')
        # k = outfile.read()
        os.chdir(PATH + name + "/sass")
        my_output = sass.compile(filename="skin.scss", output_style='expanded')
        with open("../css/skin.css", 'w') as out:
            out.write(my_output)
            print name + ' compiled'
    except Exception as e:
        pass
        print type(e), name, e.message
    finally:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))


def compile_all_sync(path):
    for name in os.listdir(path):
        compile_file(name)

 
def compile_all_async(path):
    pool = Pool(cpu_count())
    jobs = [name for name in os.listdir(path)]
    pool.map(compile_file, jobs)


# compile_all2(PATH)

# from timeit import default_timer as timer
#
#
# def time_it(func, *args):
#     start = timer()
#     func(*args)
#     return timer() - start
#
#
# print '>>> sync'
# print time_it(compile_all_sync, PATH)
#
# print '>>> async'
# print time_it(compile_all_async, PATH)
while 1:
    k = raw_input('Enter skin url\n')
    if k == 'allskins':
        compile_all_async(PATH)
        break
    elif k == 'exit':
        break
    else:
        compile_file(k)

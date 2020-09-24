from multiprocessing import Pool
import random, time
from difflib import get_close_matches

# constants
wordlist = ["".join([random.choice([letter for letter in "abcdefghijklmnopqersty"]) 
                     for lengthofword in range(5)]) for nrofwords in range(1000000)]
mainword = "hello"

# comparison function
def findclosematch(subwordlist):
    matches = get_close_matches(mainword,subwordlist,len(subwordlist),0.7)
    if matches:
        return matches

from multiprocessing import Queue, Process
import difflib

def f2(wordlist, mainwordlist, q):
    for mainword in mainwordlist:
        matches = difflib.get_close_matches(mainword,wordlist,len(wordlist),0.7)
        q.put(matches)


if __name__ == '__main__':
    print("pool method: direct call")
    pool = Pool(processes=6)
    t=time.time()
    result = pool.map_async(findclosematch, wordlist, chunksize=100)
    #do something with result
    for r in result.get():
        pass
    print(time.time()-t)


    # normal
    print("normal method")
    t=time.time()
    # run function
    result = findclosematch(wordlist)
    # do something with results
    for r in result:
        pass
    print(time.time()-t)

    print("------------ part II -----------")
    # constants (for 50 input words, find closest match in list of 100 000 comparison words)
    q = Queue()
    wordlist = ["".join([random.choice([letter for letter in "abcdefghijklmnopqersty"]) 
        for lengthofword in range(5)]) for nrofwords in range(100000)]
    mainword = "hello"
    mainwordlist = [mainword for each in range(50)]

    # normal approach
    print("normal method")
    t = time.time()
    for mainword in mainwordlist:
        matches = difflib.get_close_matches(mainword,wordlist,len(wordlist),0.7)
        q.put(matches)
    print (time.time()-t)

    # split work into 5 or 10 processes
    processes = 10
    def splitlist(inlist, chunksize):
        return [inlist[x:x+chunksize] for x in range(0, len(inlist), chunksize)]
    # print (len(mainwordlist)/processes)
    mainwordlistsplitted = splitlist(mainwordlist, int(len(mainwordlist)/processes))
    print ("list ready")

    print("pool method")
    t = time.time()
    for submainwordlist in mainwordlistsplitted:
        print ("sub")
        p = Process(target=f2, args=(wordlist,submainwordlist,q,))
        p.Daemon = True
        p.start()
    for submainwordlist in mainwordlistsplitted:
        p.join()
    print (time.time()-t)
    # while True:
    #     print (q.get())
    q.close()
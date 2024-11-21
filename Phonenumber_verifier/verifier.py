try:
    import queue
    import threading
    import phonenumbers
    from phonenumbers import carrier
    from phonenumbers.phonenumberutil import number_type

except:
    print("couldn't install some library")

inputQueue = queue.Queue()

mailist = input("phone number file name :- ")
thread = input("How many threads :- ")

print('\n')
countList = len(list(open(mailist)))

def main(number):

    num = phonenumbers.parse(number)

    a = carrier._is_mobile(number_type(num))
    a = str(a)

    if a == 'True':
        b =carrier.name_for_number(num, "en")
        print('[+] {} ({}) [+] --> valid'.format(number,b))    
        valid = open('valid.txt', 'a')
        valid.write(number)
        valid.write ('\n')
        valid.close()
        
        valids = open('valid_carrier.txt', 'a')
        valids.write(number + ':' + b)
        valids.write ('\n')
        valids.close()
                

    else:
        print('[+] {} [+] --> Not Valid'.format(number))
        invalid = open('invalid.txt', 'a')
        invalid.write(number)
        invalid.write ('\n')
        invalid.close()
        

def chk():

    try:
        while 1:
            number = inputQueue.get()

            rezs = main(number)
    
            inputQueue.task_done()

    except:
        pass

def run_thread():
    for x in range(int(thread)):
        t = threading.Thread(target=chk)
        t.setDaemon(True)
        t.start()
    for y in open(mailist, 'r').readlines():
        inputQueue.put(y.strip())
        inputQueue.join()

  
mafia = run_thread()





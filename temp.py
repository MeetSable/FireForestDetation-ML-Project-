import time,sys
# for x in range (0,5):  
#     b = "Loading" + "." * x
#     print (b, end="\r")
#     # sys.stdout.write("\033[F")
#     time.sleep(0.1)
    
# sys.stdout.write("\033[K")

while(True):
    for i in range (9):
        tmp = chr(int("2581",16) + i)
        print(tmp , end = "")
        time.sleep(0.2)
    # print()
    # time.sleep(0.2)
    # sys.stdout.write("\033[F")
    for i in range(8):
        sys.stdout.write("\033[1K")
        sys.stdout.write("\033[E")
        
    time.sleep(.2)
alist=[17,20,26,31,44,54,55,77,93]

def binary_search(alist,item):
    n = len(alist)
    mid = int(n/2)
    #print(mid)
    if n >= 0:
        print(alist[mid],mid)
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            binary_search(alist[:mid],item)
        else:
            binary_search(alist[mid+1:],item)
    return False

if __name__=="__main__":
    print(binary_search(alist,54))

import sys
def untie(data,subs=1,divs=1):
    '''Extract a bytes object into a 1d or 2d array'''
    subc = 0 #subdivision count
    divc = 0 #division count
    rtar = [] #returned array
    tval = 0 #temporary value
    for div in range(divs):
        rtar.append([])
    for i in data:
        if subc >= subs:
            rtar[divc].append(tval)
            divc += 1
            subc = 0
        if divc >= divs:
            divc = 0
        if subc == 0:
            tval = i
        else:
            if sys.byteorder == "little":
                tval = (i << 8) | tval
            elif sys.byteorder == "big":
                tval = tval | (i >> 8)
            else:
                break
        subc += 1
    return rtar
def indax(inpl, aftr=True):
    '''Adds the list index as a second axis to a 1-dimensional list'''
    if type(inpl[0]) == list():
        return inpl
    else:
        outl = []
        cntr = 0
        tval = ()
        while len(inpl) > 0:
            if aftr == True:
                tval = (inpl.pop(0), cntr)
            else:
                tval = (cntr, inpl.pop(0))
            outl.append(tval)
            cntr += 1
        return outl
def fitax(inpl, minv=None, maxv=None):
    emin = 0
    emax = 0
    outl = []
    imin = min(inpl)
    imax = max(inpl)
    if minv == None:
        emin = imin
    else:
        emin = minv
    if maxv is None:
        emax = imax
    else:
        emax = maxv
    print(emax,emin)
    print(imax,imin)
    fctr = (emax - emin) / (imax - imin)
    while len(inpl) > 0:
        outl.append(inpl.pop(0) * fctr)
    return outl

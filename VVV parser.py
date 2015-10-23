def fileparser ():
    import os
    import shutil
    import os.path
    import re
    d = input ('Enter parent directory: ')
    # moves annoying useless thumb images into subfolder called 'thumb'
    os.mkdir (os.path.join (d, r'Thumb'))
    dst1 = os.path.join (d, r'Thumb')
    for file in os.listdir(d):
        c = re.compile ("thumb")
        if c.search (file) is None:
            print ('...')
        else:
            shutil.move (os.path.join (d, file), os.path.join(dst1, file))
    if len (os.listdir(os.path.join(d, r'Thumb')))== 0:
            os.rmdir(os.path.join(d, r'Thumb'))
    ftype = ['RFP', 'DIC', 'GFP']
    x = 0
    count = 1
    alist = []
    #check for "Break up into multiple files based on sample loader position" option; process based on answer
    avar = input ('Did you check "Break up into multiple files based on sample loader position?" (y/n) ')
    if avar == 'y':
        maxsp = int (input('What is the max number of stage positions per plate used? '))
        while count <= maxsp:
            alist.append (count)
            count +=1
        b = len (alist)
        aval = 1
        while aval <=8:
            while x < len (ftype):
                while 0 < b <= len(alist):
                    os.mkdir (os.path.join (d, str(ftype [x]) + '_SAMPLE' + str(aval) + '_S' + str (alist [b-1])))
                    dst2 = os.path.join (d, str(ftype [x]) + '_SAMPLE' + str(aval) + '_S' + str (alist [b-1]))
                    search = re.compile ('Sample' + str(aval) + '.*' + str (ftype [x])+ '.*' + '_s' + str (alist [b-1]))
                    for file in os.listdir(d):
                        if re.search( search, file) is None:
                            print (search, aval)
                        else:
                            shutil.move (os.path.join(d, file), os.path.join(dst2, file))
                    if len (os.listdir(dst2)) == 0:
                        os.rmdir(dst2)
                    b -=1
                x +=1
                b = len (alist)
            aval +=1
            x = 0
            b = len(alist)
    else:
        stagepos = int (input ('How many stage positions? '))
        while count <= stagepos:
            alist.append (count)
            count +=1
        b = len (alist)
        while x < len (ftype):
            while 0< b <= len (alist):
                os.mkdir (os.path.join (d, str(ftype [x]) + '_S' + str (alist [b-1])))
                dst2 = os.path.join (d, str(ftype [x]) + '_S' + str (alist [b-1]))
                search = re.compile (str (ftype [x])+ '.*' +'_s' + str (alist [b-1]))
                for file in os.listdir(d):
                    if re.search( search, file) is None:
                        print (b, x)
                    else:
                        shutil.move (os.path.join(d, file), os.path.join(dst2, file))
                if len (os.listdir(dst2)) == 0:
                    os.rmdir(dst2)
                b -=1
            x +=1
            b = len(alist)

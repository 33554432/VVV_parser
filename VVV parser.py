import os
import shutil
import os.path
import re


def fileparser():
    d = input('Enter parent directory: ')
    # moves annoying useless thumb images into subfolder called 'thumb'
    os.mkdir(os.path.join(d, r'Thumb'))
    dst1 = os.path.join(d, r'Thumb')
    for file in os.listdir(d):
        c = re.compile("thumb")
        if c.search(file) is None:
            print('...')
        else:
            shutil.move(os.path.join(d, file), os.path.join(dst1, file))
    if len(os.listdir(os.path.join(d, r'Thumb'))) == 0:
        os.rmdir(os.path.join(d, r'Thumb'))
    ftype = ['RFP', 'DIC', 'GFP']
    x = 0
    count = 1
    alist = []
    # This part is here because if you don't have more than one wavelength it won't append *any* ftype to the file name
    # I'm going to slap whoever made this decision
    # check for any mention of DIC, RFP, or GFP in the file name, if none increment count2 variable
    # process based on value of count2
    count2 = 0
    alazyindex = 0
    while alazyindex < len (ftype):
        dumbcheck = re.compile(ftype[alazyindex])
        for file in os.listdir(d):
            if dumbcheck.search(file) is None:
                print ('Nah', ftype[alazyindex], count2)
            else:
                count2 -= 10000
        alazyindex += 1
    # check for option
    # "Break up into multiple files based on sample loader position"
    # process based on answer
    avar = input(('Did you check "Break up into multiple files based on '
                  'sample loader position?" (y/n) '))
    if avar == 'y' and count2 != 3:
        maxsp = int(input(('What is the max number of stage positions per '
                           'plate used? ')))
        while count <= maxsp:
            alist.append(count)
            count += 1
        b = len(alist)
        aval = 1
        while aval <= 8:
            while x < len(ftype):
                while 0 < b <= len(alist):
                    dst2 = os.path.join(d, str(ftype[x]) + '_SAMPLE' + str(aval) + '_S' + str(alist[b-1]))
                    os.mkdir(dst2)
                    search = re.compile('Sample' + str(aval) + '.*' + str(ftype[x]) + '.*' + '_s' + str(alist[b-1]))
                    for file in os.listdir(d):
                        if re.search(search, file) is None:
                            print(b, x)
                        else:
                            shutil.move(os.path.join(d, file),
                                        os.path.join(dst2, file))
                    if len(os.listdir(dst2)) == 0:
                        os.rmdir(dst2)
                    b -= 1
                x += 1
                b = len(alist)
            aval += 1
            x = 0
            b = len(alist)
    elif avar == 'n' and count2 != 3:
        # untested, should work though
        stagepos = int(input('How many stage positions? '))
        while count <= stagepos:
            alist.append(count)
            count += 1
        b = len(alist)
        while x < len(ftype):
            while 0 < b <= len(alist):
                dst2 = os.path.join(d, str(ftype[x]) + '_S' + str(alist[b-1]))
                os.mkdir(dst2)
                search = re.compile(str(ftype[x]) + '.*' + '_s' + str(alist[b-1]))
                for file in os.listdir(d):
                    if re.search(search, file) is None:
                        print(b, x)
                    else:
                        shutil.move(os.path.join(d, file),
                                    os.path.join(dst2, file))
                if len(os.listdir(dst2)) == 0:
                    os.rmdir(dst2)
                b -= 1
            x += 1
            b = len(alist)
    elif avar == 'y' and count2 == 3:
        # this conditional as of yet untested, is probably broken
        maxsp = int(input(('What is the max number of stage posittions per '
                           'plate used? ')))
        while count <= maxsp:
            alist.append(count)
            count += 1
        b = len(alist)
        aval = 1
        while aval <= 8:
            while 0 < b <= len(alist):
                dst2 = os.path.join(d, '_SAMPLE' + str(aval) + '_S' + str(alist[b-1]))
                os.mkdir(dst2)
                search = re.compile('Sample' + str(aval) + '.*' + '.*' + '_s' + str(alist[b-1]))
                for file in os.listdir(d):
                    if re.search(search, file) is None:
                        print(search, aval)
                    else:
                        shutil.move(os.path.join(d, file),
                                    os.path.join(dst2, file))
                if len(os.listdir(dst2)) == 0:
                    os.rmdir(dst2)
                b -= 1
    elif (avar == 'n') and (count2 == 3):
        stagepos = int(input('How many stage positions? '))
        while count <= stagepos:
            alist.append(count)
            count += 1
        b = len(alist)
        while 0 < b <= len(alist):
            dst2 = os.path.join(d, '_S' + str(alist[b-1]))
            os.mkdir(dst2)
            search = re.compile('.*' + '_s' + str(alist[b-1]))
            for file in os.listdir(d):
                if re.search(search, file) is None:
                    print(b, x)
                else:
                    shutil.move(os.path.join(d, file),
                                os.path.join(dst2, file))
            if len(os.listdir(dst2)) == 0:
                os.rmdir(dst2)
            b -= 1

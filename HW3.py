from functools import reduce
import inspect
# ############################## addDict() declaration and testing ##################################
# 1 A)


def addDict(d):
    l = []
    f = {}
    # Gives outermost key
    for key in d:
        # Gives inner key
        for val in d[key]:
            # Add these keys to a dictionary, and add all keys and values to a list
            f[val] = 0
            l.append([val, d[key][val]])
    # Traverse list and add values to keys in the dictinoary
    for var in l:
        f[var[0]] += var[1]
    return f

# Test function for addDict()
def testaddDict():
   t1 = (addDict({'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}))
   t1a = {'355' : 8, '360' : 9, '451' : 8}
   t2 = addDict({'Sat':{'Drinks':4,'Study':2},'Sun':{'Study':5,'Sleep':8}})
   t2a = {'Drinks':4,'Study':7,'Sleep':8}
   t3 = addDict({'Mon':{'317':1,'355':1}, 'Wed':{'321':1,'402':1,'322':1}, 'Fri':{'317':4,'355':6,'321':3,'402':1,'322':2}})
   t3a = {'317':5,'355':7,'321':4,'402':2,'322':3}
   t4 = addDict({})
   t4a = {}
   if t1 != t1a:
       return False
   if t2 != t2a:
       return False
   if t3 != t3a:
       return False
   if t4 != t4a:
       return False
   return True


# ############################## addDictN() declaration and testing ##################################
# 1 B)


def addDictN(L):
    # Declare variables
    d = {}
    l = []
    # Traverse list for map function
    for val in L:
        # append each hash table gone through addDict to new list
        f = list(map(lambda x: x(val), [addDict]))
        l.append(f[0])
    # Traverse list of dictionaries, make new dictionary with each hash key from l set to 0
    for thing in l:
        for key in thing:
            d[key] = 0
    # Add values to new dictionary with += starting from 0
    for thing in l:
        for key in thing:
            d[key] += thing[key]
    # Return final dictionary
    return d


# Test function for addDictN()
def testaddDictN():
    t1 = addDictN([{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},'Fri':{'355':2},'Sun':{'355': 1}},{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}, {'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}}])
    t1a = {'451': 6, '360': 24, '355': 16}
    t2 = addDictN([{},{},{}])
    t2a = {}
    t3 = addDictN([{'Mon':{'317':1,'355':1}},{'Mon':{'321':1,'402':1,'322':1}},{'Mon':{'317':4,'355':6,'321':3,'402':1,'322':2}}])
    t3a = {'317':5,'355':7,'321':4,'402':2,'322':3}
    t4 = addDictN([{'Mon':{'317':0,'355':-1}}, {'Tues':{'Work':3,'Sleep':9,'355':4.5},'Mon':{'317':0,'355':-1}}, {'Fri':{'Drinks':3,'Sleep':9,'Procrastinate':15},'Sat':{'Recover':24}}])
    t4a = {'Procrastinate': 15, '317': 0, 'Recover': 24, '355': 2.5, 'Work': 3, 'Sleep': 18, 'Drinks': 3}
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    if t4 != t4a:
        return False
    return True


# ############################## charCount/charCount2 declaration and testing ##################################
# 2 a)

def charCount(s):
    d = {};
    L = []
    for val in s:
            d[val] = 0
    for val in s:
            d[val] += 1
    for val in d:
        if val != ' ':
            L.append((val, d[val]))
    return sorted(sorted(L, key=lambda tup: tup[0]), key=lambda tup: tup[1])

# 2 b)

def charCount2(s):
    d = {}
    L = []
    for val in s:
        if val != ' ':
            d[val] = 0
    for val in d:
        L.append((val,(s.count(val))))
    return sorted(sorted(L, key=lambda tup: tup[0]), key=lambda tup: tup[1])

# Test function for charCount()/charCount2()
def testcharCount():
    t1 = charCount(' 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1111')
    t12 = charCount2(' 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1111')
    t1a = [('1', 18)]
    t2 = charCount('')
    t22 = charCount2('')
    t2a = []
    t3 = charCount('zYxwVuTSRqpoNMlkJIhgFeDcbA')
    t32 = charCount2('zYxwVuTSRqpoNMlkJIhgFeDcbA')
    t3a = [('A', 1), ('D', 1), ('F', 1), ('I', 1), ('J', 1), ('M', 1), ('N', 1), ('R', 1), ('S', 1), ('T', 1), ('V', 1), ('Y', 1), ('b', 1), ('c', 1), ('e', 1), ('g', 1), ('h', 1), ('k', 1), ('l', 1), ('o', 1), ('p', 1), ('q', 1), ('u', 1), ('w', 1), ('x', 1), ('z', 1)]
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    if t12 != t1a:
        return False
    if t22 != t2a:
        return False
    if t32 != t3a:
        return False
    return True


# ############################## charCount/charCount2 declaration and testing ##################################
# 3 a)
# Definition of lookupVal
def lookupVal(L,k):
    # Reverse list to access back elements first per requirements
    for val in reversed(L):
        # Traverse list and look for key values in dictionaries
        if k in val.keys():
            return val[k]
    return None

# 3 b)
# Recursive call to help lookupVal2
def lookupVal2Helper(tL,k,count):
    # Base case for recursion, check for value, return if found or None if not
    if count == 0:
        if k in tL[0][1].keys():
            return tL[0][1][k]
        else:
            return None
    # Base case not met just check current value and return if there or move to next value if not
    elif k in tL[count][1].keys():
        return tL[count][1][k]
    else:
        return lookupVal2Helper(tL,k,tL[count][0])

# Standard call for lookupVal2
def lookupVal2(tL,k):
    return lookupVal2Helper(tL,k,-1)

# Start of tests for both lookupVal functions
def lookupValTest():
    t1 = lookupVal([{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}], "y")
    t1a = False
    t2 = lookupVal([{}],None)
    t2a = None
    t3 = lookupVal([{90:"throw"},{"90":"Words"},{'90':"something"}],90)
    t3a = "throw"
    t4 = lookupVal([{90:"throw"},{'90':"No no no"},{"90":"Words"},{'90':"something"}],'90')
    t4a = "something"
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    if t4 != t4a:
        return False
    return True

def lookupVal2Test():
    t1 = lookupVal2([(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}),(1,{"y":False}),(1,{"x":3, "z":"three"}),(2,{})],"z")
    t1a = "zero"
    t2 = lookupVal2([(0,{})],None)
    t2a = None
    t3 = lookupVal2([(0,{"A":False,"B":True}),(2,{"c":(5,8),"d":[1,2,3,4]}),(0,{"E":"Hello there","f":'c'}),(1,{"g":100,"H":-50})],"c")
    t3a = (5,8)
    t4 = lookupVal2([(0,{"A":False,"B":True}),(2,{"c":(5,8),"d":[1,2,3,4]}),(0,{"E":"Hello there","f":'c'}),(1,{"g":100,"H":-50})],"H")
    t4a = -50
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    if t4 != t4a:
        return False
    return True


# ############################## funRun declaration and testing ##################################
# 4)
def funRun(d,name,args):
    # Check if name is in dictionary
    if name in d.keys():
        val = inspect.getargspec(d[name])
        # Cases for argument values 0 - 3, includes case for anything else that returns error
        if len(val[0]) == len(args):
            if len(args) == 0:
                return d[name]()
            elif len(args) == 1:
                return d[name](args[0])
            elif len(args) == 2:
                return d[name](args[0],args[1])
            elif len(args) == 3:
                return d[name](args[0],args[1],args[2])
            else:
                print("Error: More than 4 arguments entered")
                return "Error"
        # If number of arguments doesn't match parameters needed for lambda function
        else:
            print("Error: Arguments don't match")
            return "Error"
    # If name not in the dictionary
    else:
        print("Error: name not in dictionary")
        return "Error"


def testfunRun():
    t1 = funRun({"SomeFunc": lambda a,b,c:(a + b - c)},"SomeFunc",[5,4,3,2,1])
    t1a = "Error"
    t2 = funRun({"String": lambda a,b,c:(a + b + c)},"String",["Oh!"," Hi"," Mark"])
    t2a = "Oh! Hi Mark"
    t3 = funRun({},"",[])
    t3a = "Error"
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    return True



# ############################## numPaths declaration and testing ##################################
# 5)
def numPaths(m,n):
    if m == 1 or n == 1:
        return 1
    return (numPaths(m-1,n) + numPaths(m,n-1))


# Tests for numPaths

def testnumPaths():
    t1 = numPaths(10,3)
    t1a = 55
    t2 = numPaths(1,5)
    t2a = 1
    t3 = numPaths(6,6)
    t3a = 252
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    return True


# ############################## Iterators declaration and testing ##################################
# 6 a)
class iterSquares():
    val = 1

    def __iter__(self):
        self.val += 1

    def __reduce__(self):
        self.val -= 1

    def __next__(self):
        thing = self.val ** 2
        self.__iter__()
        return thing

# b)
def numbersToSum(iNumbers,sum):
    val2 = iNumbers.__next__()
    val = val2
    ret = []
    while val < sum:
        ret.append(val2)
        val2 = iNumbers.__next__()
        val = val + val2
    iNumbers.__reduce__()
    return ret

def testnumbersToSum():
    thing = iterSquares()
    t1 = numbersToSum(thing,0)
    t1a = []
    t2 = numbersToSum(thing,55)
    t2a = [1,4,9,16]
    thing.__next__()
    thing.__next__()
    t3 = numbersToSum(thing,1000)
    t3a = [49, 64, 81, 100, 121, 144, 169, 196]
    if t1 != t1a:
        return False
    if t2 != t2a:
        return False
    if t3 != t3a:
        return False
    return True


# ############################## Streams declaration and testing ##################################
# 7 a)

class Stream(object):
    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._computed = False

    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest
empty_stream = Stream(None,None,True)

def streamSquares(k):
    def compute_rest():
        a = k ** (1/2)
        a = int((a+1) ** 2)
        return streamSquares(a)
    return Stream(k,compute_rest)


def evenStream(stream):
    def compute_rest2():
        s = stream
        k = s.first
        while k % 2 != 0:
            k = s.first
            s = s.rest
        s = s.rest
        return evenStream(s)
    s = stream
    k = s.first
    while k % 2 != 0:
        k = s.first
        s = s.rest
    return Stream(k,compute_rest2)

def testEvenStream():
   t1 = evenStream(streamSquares(25))
   t2 = evenStream(streamSquares(121))
   t3 = evenStream(streamSquares(4))
   mylist1 = []
   mylist2 = []
   mylist3 = []
   while t1.first < 300:
       mylist1.append(t1.first)
       t1 = t1.rest
   while t2.first < 1000:
       mylist2.append(t2.first)
       t2 = t2.rest
   while t3.first < 225:
       mylist3.append(t3.first)
       t3 = t3.rest
   if mylist1 != [36,64,100,144,196,256]:
       return False
   if mylist2 != [144, 196, 256, 324, 400, 484, 576, 676, 784, 900]:
       return False
   if mylist3 != [4, 16, 36, 64, 100, 144, 196]:
       return False
   return True


# ########################################## Main ################################################

if __name__ == '__main__':
    arr = [(testaddDict(),"addDict"), (testaddDictN(),"addDictN"), (testcharCount(),"charCount/charCount2"),
           (lookupValTest(),"lookupVal"), (lookupVal2Test(),"lookupVal2"),
           (testfunRun(),"funRun"), (testnumPaths(),"numPaths"), (testnumbersToSum(),"numbersToSum"),
           (testEvenStream(),"evenStream")]
    passedmsg = "%s Passed"
    failedmsg = "%s Failed"
    for val in arr:
        if val[0]:
            print(passedmsg % val[1])
        else:
            print(failedmsg % val[1])
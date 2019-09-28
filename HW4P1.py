# Samuel Carroll
# CptS 355
# Homework 4 Pt 1
## All functions contain debug/error messages. Seperated by code
## Comments designating what following section will contain.

######################### OpStack with pop and push #############################
opstack = []


def opPop():
    if opstack:
        x = opstack[-1]
        del opstack[-1]
        return x
    else:
        print("No values in opstack")
        return None

def opPush(value):
    opstack.append(value)


######################## DictStack with pop, push, define, and lookup #######################


dictstack = []


def dictPop():
    if dictstack:
        del dictstack[-1]
    else:
        print("Stack is empty")

def dictPush(d):
    dictstack.append(d)


def define(name,value):
    if dictstack:
        dictstack[-1][name] = value
    else:
        dictstack.append( {name:value} )


def lookup(name):
    for val in reversed(dictstack):
        if ('/'+name) in val.keys():
            return val['/'+name]
    print("Error - Item not found")
    return None


####################### Operators Ints ####################


def add():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            opPush(a + b)
        else:
            print("Error Add - Non ints returned")
    else:
        print("Error Add - Not enough values in stack or non ints present")


def sub():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            opPush(b - a)
        else:
            print("Error Sub - Non ints returned")
    else:
        print("Error Sub - Not enough values in stack or non ints present")


def mul():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            opPush(a * b)
        else:
            print("Error Mul - Non ints returned")
    else:
        print("Error Mul - Not enough values in stack or non ints present")

def div():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            opPush(b / a)
        else:
            print("Error Div - Non ints returned")
    else:
        print("Error Div - Not enough values in stack or non ints present")

def mod():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            opPush(b % a)
        else:
            print("Error Mod - Non ints returned")
    else:
        print("Error Mod - Not enough values in stack or non ints present")


####################### Operators Arrays ####################

def length():
    if opstack and isinstance(opstack[-1],list):
        opstack.append(len(opstack[-1]))
    else:
        print("Error Length - Empty stack or non array at start")


def get():
    if len(opstack) > 1:
        value = opPop()
        arr = opPop()
        if isinstance(arr,list) and isinstance(value,int) and value >= 0 and value <= len(opstack):
            opPush(arr[value])
        elif isinstance(arr,int) and isinstance(value,list) and arr >= 0 and value <= len(opstack):
            opPush(value[arr])
        else:
            print("Error Get - Improper return types from operator stack")
    else:
        print("Error Get - Too few items in opstack")


################# Stack manipulation and print operators ###################

def dup():

    if opstack:
        opPush(opstack[-1])
    else:
        print("Error Dup - Empty stack")


def exch():
    if len(opstack) > 1:
        a = opPop()
        b = opPop()
        opPush(a)
        opPush(b)
    else:
        print("Error Exch - Stack has insufficient nodes")


def pop():
    if opstack:
        print("Popped Value:", opstack[-1])
        del opstack[-1]
    else:
        print("Error Pop - Stack has insufficient nodes")


def roll():
    top = opPop()
    Spos = opPop()
    if top <= len(opstack):
        hold = opstack[len(opstack) - Spos:]
        for i in range(Spos):
            opPop()
        if top:
            for val in range(abs(top)):
                temp = hold[0]
                hold.append(temp)
                hold.remove(temp)
        else:
            for val2 in range(top):
                temp = hold.pop()
                hold.insert(0,temp)
        for val3 in hold:
            opPush(val3)
    else:
        print("Error Roll - Rolling more than in stack")


def copy():
    newlist = []
    if opstack:
        val = opPop()
        if val <= len(opstack) + 1:
            for i in range(val):
                newlist.append(opPop())
            newlist.reverse()
            opstack.extend(newlist + newlist)
        else:
            print("Error Copy - Input greater than stack length")
    else:
        print("Error Copy - Empty Stack")


def clear():
    del opstack[:]


def stack():
    print(opstack)


################# Dictionary Manipulations ################

def psDict():
    opPop()
    opPush({})


def begin():
    if opstack:
        a = opPop()
        if (isinstance(a,dict)):
            dictPush(a)
        else:
            print("Error Begin - Non Dictionary type")
    else:
        print("Error Begin - Empty Stack")


def end():
    if dictstack:
        del dictstack[-1]
    else:
        print("Error End - Dictstack Empty")


def psDef():
    if len(opstack) > 1:
        newval = opPop()
        newname = opPop()
        if isinstance(newname, str):
            define(newname,newval)
        else:
            print("Error PSDef - Name value not a string")
    else:
        print("Error PSDef - Insufficient nodes in opstack")


#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    define("/n2", 0)
    define("/n3", -15)
    define("/n4", 1000)
    if lookup("n1") != 4 and lookup("n2") != 0 and lookup("n3") != -15 and lookup("n4") != 1000:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    opPush("/n2")
    opPush(0)
    psDef()
    opPush("/n3")
    opPush(-15)
    psDef()
    opPush("/n4")
    opPush(1000)
    psDef()
    if lookup("n1") != 4 and lookup("n2") != 0 and lookup("n3") != -15 and lookup("n4") != 1000:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    T1 = opPop()
    opPush(15)
    opPush(-5)
    add()
    T2 = opPop()
    opPush(0)
    opPush(0)
    add()
    T3 = opPop()
    opPush(-5)
    opPush(1000)
    add()
    T4 = opPop()
    if T1 != 3 and T2 != 10 and T3 != None and T4 != -995:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    T1 = opPop()
    opPush(15)
    opPush(-5)
    sub()
    T2 = opPop()
    opPush(0)
    opPush(0)
    sub()
    T3 = opPop()
    opPush(-5)
    opPush(1000)
    sub()
    T4 = opPop()
    if T1 != 5.5 and T2 != 20 and T3 != 0 and T4 != -1005:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    T1 = opPop()
    opPush(.5)
    opPush(-5)
    mul()
    T2 = opPop()
    opPush(0)
    opPush(0)
    mul()
    T3 = opPop()
    opPush(-5)
    opPush(1000)
    mul()
    T4 = opPop()
    if T1 != 9 and T2 != -2.5 and T3 != None and T4 != -5000:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    T1 = opPop()
    opPush(15)
    opPush(-5)
    sub()
    T2 = opPop()
    opPush(50)
    opPush(0)
    sub()
    T3 = opPop()
    opPush(5)
    opPush(1)
    sub()
    T4 = opPop()
    if T1 != 2.5 and T2 != -3 and T3 != 0 and T4 != .2:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    T1 = opPop()
    opPush(15)
    opPush(-5)
    sub()
    T2 = opPop()
    opPush(3)
    opPush(3)
    sub()
    T3 = opPop()
    opPush(6)
    opPush(1000)
    sub()
    T4 = opPop()
    if T1 != 1 and T2 != 10 and T3 != None and T4 != 4:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    T1 = opPop()
    opPush([])
    length()
    T2 = opPop()
    opPush(["One", "Two", "Three"])
    length()
    T3 = opPop()
    opPush([[],[1],[1,2],[1,2,3]])
    length()
    T4 = opPop()
    if T1 != 5 and T2 != None and T3 != 3 and T4 != 4:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    T1 = opPop()
    opPush([1,2,3,4,5])
    opPush(0)
    get()
    T2 = opPop()
    opPush(["One", "Two", "Three"])
    opPush(2)
    get()
    T3 = opPop()
    opPush([[],[1],[1,2],[1,2,3]])
    opPush(3)
    get()
    T4 = opPop()
    if T1 != 5 and T2 != 1 and T3 != "Three" and T4 != [1,2,3]:
        return False
    return True

#stack manipulation functions
def testDup():
    vals = [10,'a',-5,"Hello"]
    for i in vals:
        opPush(i)
        dup()
        if opPop()!=opPop():
            return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1 != l2:
        return False
    l1 = len(opstack)
    opPush(10)
    opPush(10)
    pop()
    pop()
    l2 = len(opstack)
    if l1 != l2:
        return False
    l1 = len(opstack)
    opPush(10)
    opPush(10)
    opPush(10)
    pop()
    pop()
    pop()
    l2 = len(opstack)
    if l1 != l2:
        return False
    l1 = len(opstack)
    opPush(10)
    opPush(10)
    opPush(10)
    opPush(10)
    pop()
    pop()
    pop()
    pop()
    l2 = len(opstack)
    if l1 != l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    opPush(7)
    opPush(3)
    opPush(9)
    opPush(6)
    opPush(13)
    opPush(5)
    opPush(-3)
    roll()
    if opPop()!=9 and opPop()!=3 and opPop()!=7 and opPop()!=13 and opPop()!=6:
        return False
    opPush(7)
    opPush(3)
    opPush(9)
    opPush(6)
    opPush(13)
    opPush(5)
    opPush(4)
    roll()
    if opPop()!=6 and opPop()!=9 and opPop()!=3 and opPop()!=7 and opPop()!=13:
        return False
    opPush(0)
    opPush(0)
    opPush(-3)
    opPush(-13)
    opPush(-5)
    opPush(2)
    opPush(1)
    roll()
    if opPop()!=-13 and opPop()!=-5 and opPop()!=-3 and opPop()!=0 and opPop()!=0:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    opPush("Hello")
    opPush("Grader")
    opPush("Please")
    opPush("Provide")
    opPush("An")
    opPush("A")
    opPush(7)
    copy()
    if opPop()!="A" and opPop()!="An" and opPop()!="Provide" and opPop()!="Please" and opPop()!="Grader" and opPop()!="Hello":
        return False
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(6)
    opPush(3)
    copy()
    if opPop()!=6 and opPop()!=4 and opPop()!=3:
        return False
    opPush(0)
    opPush(0)
    opPush(0)
    opPush(0)
    copy()
    if opPop()!=0:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    opPush(10)
    opPush("/x")
    opPush({"/x":10})
    clear()
    if len(opstack)!=0:
        return False
    opPush(0)
    clear()
    if len(opstack)!=0:
        return False
    opPush(15)
    opPush("No")
    opPush('a')
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    opPush({"Name":5})
    opPush(8)
    opPop()
    psDict()
    if opPop()!={}:
        return False
    opPush({"new":"Val"})
    opPush({"Old":"Newval"})
    opPush({"Not":'3'})
    psDict()
    if opPop()!={}:
        return False
    opPush(10000)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    opPush("/y")
    opPush(15)
    psDef()
    opPush({})
    begin()
    opPush("/y")
    opPush(15)
    psDef()
    end()
    if lookup("y")!=15:
        return False
    opPush("/z")
    opPush("No")
    psDef()
    opPush({})
    begin()
    opPush("/z")
    opPush(4)
    psDef()
    end()
    if lookup("z")!="No":
        return False
    opPush("/a")
    opPush('a')
    psDef()
    opPush({})
    begin()
    opPush("/a")
    opPush("b")
    psDef()
    end()
    if lookup("a")!='a':
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    opPush("/y")
    opPush("a")
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("y")!="a":
        end()
        return False
    opPush("/z")
    opPush(None)
    psDef()
    opPush(15)
    psDict()
    begin()
    if lookup("z")!=None:
        end()
        return False
    opPush("/a")
    opPush([1,1,2,3,5,8])
    psDef()
    opPush("Hello")
    psDict()
    begin()
    if lookup("a")!=[1,1,2,3,5,8]:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('mod', testMod), \
                ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        print("Fail")
        return ('Some tests failed', failedTests)
    else:
        print("Pass")
        return ('All part-1 tests OK')


main_part1()
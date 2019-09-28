# Samuel Carroll
# CptS 355
# Homework 4 Pt 1

######################### OpStack with pop and push #############################
opstack = []


def opPop():
    if len(opstack) > 0:
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

def clearDictStack():
    del dictstack[:]

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
        opstack.append(len(opPop()))
    else:
        print("Error Length - Empty stack or non array at start")


def get():
    if len(opstack) > 1:
        value = opPop()
        arr = opPop()
        if isinstance(arr,list) and isinstance(value,int) and value >= 0 and value <= len(arr):
            opPush(arr[value])
        elif isinstance(arr,int) and isinstance(value,list) and arr >= 0 and arr <= len(value):
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


#main_part1()

##################################### Part 2 ########################################

#################################### Tokenizing #####################################

import re

# provided tokenize, using regular expression
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


#################### Parsing #######################


def ParaMatching(it):
    ret = []
    for val in it:
        # handles curly brackets, including looped curly brackets
        if val == ')':
            return ret
        elif val == '(':
            ret.append(ParaMatching(it))
        else:
            # additional conditions for special cases
            if val.isnumeric():
                ret.append(int(val))
            elif val[0] == '-':
                ret.append(int(val))
            else:
                ret.append(val)
    return False

def curlyMatching(it):
    ret = []
    for val in it:
        # handles curly brackets, including looped curly brackets
        if val == '}':
            return ret
        elif val == '{':
            ret.append(curlyMatching(it))
        elif val[0] == '[' and len(val) > 1:
            l = []
            thing = re.findall("[a-zA-Z0-9]+", val)
            for things in thing:
                if things.isnumeric():
                    l.append(int(things))
                elif things[0] == '-':
                    l.append(int(things))
                else:
                    l.append(things)
            ret.append(l)
        else:
            # additional conditions for special cases
            if val.isnumeric():
                ret.append(int(val))
            elif val[0] == '-':
                ret.append(int(val))
            else:
                ret.append(val)
    return False

def bracketMatching(it):
    ret = []
    for val in it:
        # handles brackets, including looped brackets
        if val == ']':
            return ret
        elif val == '[':
            ret.append(curlyMatching(it))
        else:
            # additional conditions for special cases
            if val.isnumeric():
                ret.append(int(val))
            elif val[0] == '-':
                ret.append(int(val))
            else:
                ret.append(val)
    return False

# Parse a token

def parse(tokens):
    ret = []
    it = iter(tokens)
    for val in it:
        # Conditions for curly brackets
        if val == '{':
            ret.append(curlyMatching(it))
        elif val == '}':
            print("Error improper curly brace use")
            return False
        # Non Curly bracket conditions
        else:
            if val.isnumeric():
                ret.append(int(val))
            elif val[0] == '-':
                ret.append(int(val))
            # condition for list
            elif val[0] == '[' and len(val) > 1:
                l = []
                thing = re.findall("[a-zA-Z0-9]+", val)
                for things in thing:
                    if things.isnumeric():
                        l.append(int(things))
                    elif things[0] == '-':
                        l.append(int(things))
                    else:
                        l.append(things)
                ret.append(l)
            elif val == '[':
                ret.append(bracketMatching(it))
            else:
                ret.append(val)
    return ret

# Implements the for loop property of postscript
def forloop():
    # Pop top four off stack
    if len(opstack) > 3:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        op4 = opPop()
        # Loop based on bottom 3 popped
        if op2 > op4:
            while op2 >= op4:
                # push op4 and interpret the command found in op1
                opPush(op4)
                interpret(op1)
                if op3 > 0:
                    op4 = op4 + op3
                else:
                    op4 = op4 - op3
        else:
            while op2 <= op4:
                # same as above, second loop for seperate condition
                opPush(op4)
                interpret(op1)
                if op3 < 0:
                    op4 = op4 + op3
                else:
                    op4 = op4 - op3


# Interpret, actually interprets the code
def interpret(code):
    # Conditions for each command or command type
    for val in code:
        if isinstance(val, int) or isinstance(val, bool):
            opPush(val)
        elif val[0] == '/':
            opPush(val)
        elif isinstance(val,list):
            opPush(val)
        elif val == 'for':
            forloop()
        elif val == 'add':
            add()
        elif val == 'sub':
            sub()
        elif val == 'div':
            div()
        elif val == 'mod':
            mod()
        elif val == 'mul':
            mul()
        elif val == 'roll':
            roll()
        elif val == 'get':
            get()
        elif val == 'begin':
            begin()
        elif val == 'end':
            end()
        elif val == 'stack':
            stack()
        elif val == 'lookup':
            lookup()
        elif val == 'def':
            psDef()
        elif val == 'dict':
            psDict()
        elif val == 'clear':
            clear()
        elif val == 'pop':
            pop()
        elif val == 'length':
            length()
        elif val == 'get':
            get()
        elif val == 'exch':
            exch()
        elif val == 'copy':
            copy()
        elif val == 'dup':
            dup()
        elif isinstance(val, str):
            newval = lookup(val)
            if isinstance(newval, list):
                for things in newval:
                    if isinstance(things, int):
                        fact = True
                    else:
                        fact = False
                        break
                if fact == False:
                    interpret(newval)
                else:
                    opPush(newval)
            else:
                opPush(newval)
        else:
            print("Unregistered value")

# Calls interpreter off of initial string
def interpreter(s):
    interpret(parse(tokenize(s)))


#################################### TESTING #########################################

Provtest = """ /fact{ 0 dict begin /n exch def 1 n -1 1 {mul} for end }def [1 2 3 4 5] dup 4 get pop length fact stack """
def ProvTests():
    if tokenize(Provtest) == ['/fact', '{', '0', 'dict', 'begin', '/n', 'exch', 'def', '1', 'n', '-1', '1', '{', 'mul', '}', 'for', 'end', '}', 'def', '[1 2 3 4 5]', 'dup', '4', 'get', 'pop', 'length', 'fact', 'stack']:
        if parse(tokenize(Provtest)) == ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, ['mul'], 'for', 'end'], 'def', [1, 2, 3, 4, 5], 'dup', 4, 'get', 'pop', 'length', 'fact', 'stack']:
            interpreter(Provtest)
            if opstack == [120]:
                print("Provided Tests Passed")
            else:
                print("Interpreter failed")
        else:
            print("Parse failed")
    else:
        print("Tockenize failed")

ProvTests()
clear()

Test1 = ""
def MyTests1():
    if tokenize(Test1) == []:
        if parse(tokenize(Test1)) == []:
            interpreter(Test1)
            if opstack == []:
                print("Test 1 Passed")
            else:
                print("Interpreter1 failed")
        else:
            print("Parse1 failed")
    else:
        print("Tockenize1 failed")

MyTests1()

clear()
Test2 = "/thing { [5 4 3 2 1] length } def 15 thing add"
def MyTests2():
    if tokenize(Test2) == ['/thing', '{', '[5 4 3 2 1]', 'length', '}', 'def', '15', 'thing', 'add']:
        if parse(tokenize(Test2)) == ['/thing', [[5,4,3,2,1], 'length'], 'def', 15, 'thing', 'add']:
            interpreter(Test2)
            if opstack == [20]:
                print("Test 2 Passed")
            else:
                print("Interpreter2 failed")
        else:
            print("Parse2 failed")
    else:
        print("Tockenize2 failed")

MyTests2()

clear()
Test3 = "1 1 10 { 10 mul } for"
def MyTests3():
    if tokenize(Test3) == ['1', '1', '10', '{', '10', 'mul', '}', 'for']:
        if parse(tokenize(Test3)) == [1, 1, 10, [10,'mul'], 'for']:
            interpreter(Test3)
            if opstack == [10,20,30,40,50,60,70,80,90,100]:
                print("Test 3 Passed")
            else:
                print("Interpreter3 failed")
        else:
            print("Parse3 failed")
    else:
        print("Tockenize3 failed")



MyTests3()

clear()
Test4 = "[10 20 30 40 50] dup 3 get exch 4 get mul"
def MyTests4():
    if tokenize(Test4) == ['[10 20 30 40 50]', 'dup', '3', 'get', 'exch', '4', 'get', 'mul']:
        if parse(tokenize(Test4)) == [[10, 20, 30, 40, 50], 'dup', 3, 'get', 'exch', 4, 'get', 'mul']:
            interpreter(Test4)
            if opstack == [2000]:
                print("Test 4 Passed")
            else:
                print("Interpreter4 failed")
        else:
            print("Parse4 failed")
    else:
        print("Tockenize4 failed")


MyTests4()

clear()
Test5 = "{ 0 -1 -10 {add} for } /check exch def 1 check"
def MyTests5():
    if tokenize(Test5) == ['{', '0', '-1', '-10', '{', 'add', '}', 'for', '}', '/check', 'exch', 'def', '1', 'check']:
        if parse(tokenize(Test5)) == [[0,-1,-10,['add'], 'for'], '/check', 'exch', 'def', 1, 'check']:
            interpreter(Test5)
            if opstack == [-54]:
                print("Test 5 Passed")
            else:
                print("Interpreter5 failed")
        else:
            print("Parse5 failed")
    else:
        print("Tockenize5 failed")


MyTests5()
clear()
clearDictStack()


def main_part2():

#---------Test Case 1 -------
    print('---------Test Case-1 (15%)-------')
    testcase1= """
    /fact{
    0 dict
            begin
                    /n exch def
                    1
                    n -1 1 {mul} for
            end
    }def
    [1 2 3 4 5] dup 4 get pop
    length
    fact
    stack
    """
    interpreter(testcase1)
    #output should print 120
    clear() #clear the stack for next test case
    clearDictStack()

#---------Test Case 2a -------
    print('---------Test Case-2a (15%)-------')
    testcase2a = """
    /L [4 3 2 1] def
    /lengthL {L length 1 sub} def
    /getL {L exch get} def
    0 1 lengthL {getL dup mul} for 
    stack
    """
    interpreter(testcase2a)
    #should print : 1 4 9 16
    clear() #clear the stack for next test case
    clearDictStack()

#---------Test Case 2b -------
    print('---------Test Case-2b (5%)-------')
    testcase2b = """
    /L [4 3 2 1] def
    /lengthL { [4 3 2 1] length 1 sub} def
    /getL { [4 3 2 1] exch get} def
    0 1 lengthL {getL dup mul} for 
    stack
    """
    interpreter(testcase2b)
    #should print : 1 4 9 16
    clear() #clear the stack for next test case
    clearDictStack()


#---------Test Case 3 -------
    print('---------Test Case-3 (20%) -------')
    testcase3 = """
     /x 10 def 
     /y 5 def
     /f1 { x y 1 dict begin
                /y /z y def x def
                /x z def
                x y sub
         end} def 
     f1 3 1 roll sub     
     stack
    """
    interpreter(testcase3)
    #should print 5  -5
    clear() #clear the stack for next test case
    clearDictStack()

#---------Test Case 4 -------
    print('---------Test Case-4 (15%)-------')
    testcase4 = """
        /sum { -1 0 {add} for} def 
        0 
        [1 2 3 4] length 
        sum 
        2 mul 
        [1 2 3 4] 2 get 
        add  
        stack 
    """
    interpreter(testcase4)
    # should print 23
    clear() #clear the stack for next test case
    clearDictStack()

#---------Test Case 5 -------
    print('---------Test Case-5 (15%) -------')
    testcase5 = """
        /a 2 def
        /b 3 def
        /f1 { 1 dict begin 
                a 1 add /a exch def 
                2 dict begin 
                a 1 sub /a exch def 
                b 1 add /b exch def 
             end
             a b mul
             end } def
        f1
        stack
    """
    interpreter(testcase5)
    # should print 9
    clear() #clear the stack for next test case
    clearDictStack()

    print('---------Test Case-6 (15%) -------')
    testcase6 = """
        /x 2 def
        /y 3 def
        /fn { x y add
              x y mul
        } def
        fn add 
        stack
    """
    interpreter(testcase6)
    print("---------------------------")
    # should print 11
    clear() #clear the stack for next test case
    clearDictStack()


if __name__ == '__main__':
    main_part2()


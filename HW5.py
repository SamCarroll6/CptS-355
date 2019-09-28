# Samuel Carroll
# CptS 355
# Homework 4 Pt 1
## All functions contain debug/error messages. Seperated by code
## Comments designating what following section will contain.

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
        dictstack[-1][0][name] = value
    else:
        dictstack.append(({name: value}, 0))


# Lookup function
def lookup(name):
    # Looks for appropriate value, follows static links
    # For dynamic funcions the links are just n - 1 where n is current stack place
    # this means it just rolls back in this situation through the stack until proper value found
    hold = dictstack[-1][1]
    if ('/' + name) in dictstack[-1][0].keys():
        return dictstack[-1][0]['/'+name]
    while hold != 0:
        if ('/' + name) in dictstack[hold][0].keys():
            return dictstack[hold][0]['/' + name]
        hold = dictstack[hold][1]
    if ('/' + name) in dictstack[hold][0].keys():
        return dictstack[hold][0]['/' + name]
    else:
        print(dictstack)
        return None

# Just used for static situations, sets static link value
# When this function returns it gives integer value of stack containing declaration
# This int will become the new dictionaries static link value
def lookup2(name):
    hold = dictstack[-1][1]
    # If value declaration found in top spot return current top spot
    if ('/' + name) in dictstack[-1][0].keys():
        return len(dictstack)-1
    # Other wise we traverse the already set static links and return when value found
    while hold != 0:
        if ('/' + name) in dictstack[hold][0].keys():
            return hold
        hold = dictstack[hold][1]
    if ('/' + name) in dictstack[hold][0].keys():
        return hold
    else:
        return None
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
    this = len(dictstack) - 1
    print("===========")
    for val in reversed(opstack):
        print(val)
    print("===========")
    for val in reversed(dictstack):
        print("----", this, "----", val[1], "----")
        for key in val[0]:
            print(key, val[0][key])
        this = this - 1
    print("===========")


################# Dictionary Manipulations ################


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
def forloop(scope):
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
                interpretSPS(op1,scope)
                if op3 > 0:
                    op4 = op4 + op3
                else:
                    op4 = op4 - op3
        else:
            while op2 <= op4:
                # same as above, second loop for seperate condition
                opPush(op4)
                interpretSPS(op1,scope)
                if op3 < 0:
                    op4 = op4 + op3
                else:
                    op4 = op4 - op3


# Interpret, actually interprets the code
def interpretSPS(code, scope):
    Dictfunc = {'for': forloop, 'add': add, 'sub': sub, 'div': div,
                'mod': mod, 'mul': mul, 'roll': roll, 'stack': stack,
                'lookup': lookup, 'def': psDef, 'clear': clear, 'pop': pop, 'length': length,
                'get': get, 'exch': exch, 'copy': copy, 'dup': dup}
    # Conditions for each command or command type
    for val in code:
        if isinstance(val, int) or isinstance(val, bool):
            opPush(val)
        elif val[0] == '/':
            opPush(val)
        elif isinstance(val,list):
            opPush(val)
        elif isinstance(val, str):
            if val in Dictfunc:
                if val == 'for':
                    Dictfunc[val](scope)
                else:
                    Dictfunc[val]()
            else:
                # If static scope use lookup2 value for static link
                if scope == 'static':
                    dictPush(({}, lookup2(val)))
                # Otherwise just set current top of stack value, this makes
                # dynamic lists simply traverse linearly through the stack for value searches
                # and meant I only needed on lookup function for both static and dynamic
                # (Above lookup is a different function than lookup2 to clarify)
                else:
                    dictPush(({}, len(dictstack) - 1))
                newval = lookup(val)
                if isinstance(newval, list):
                    for things in newval:
                        if isinstance(things, int):
                            fact = True
                        else:
                            fact = False
                            break
                    if fact == False:
                        interpretSPS(newval, scope)
                    else:
                        opPush(newval)
                else:
                    opPush(newval)
                if scope == 'static' or dictstack[-1][0] == {}:
                    dictPop()
        else:
            print("Unregistered value")

# Calls interpreter off of initial string
def interpreter(s, scope):
    if scope == 'dynamic' or scope == 'static':
        interpretSPS(parse(tokenize(s)),scope)
    else:
        print("Scope incorrectly specified")


#################################### TESTING #########################################


print("####################### Provided Tests Start ########################")
print()

Test1 = """ /m 50 def
/n 100 def
/egg1 {/m 25 def n} def
/chic {
/n 1 def
/egg2 { n } def m n
egg1
egg2
 stack } def n
chic """

print("Test1 Dynamic")
interpreter(Test1,'dynamic')

clear()
clearDictStack()

print("Test1 Static")
interpreter(Test1,'static')

clear()
clearDictStack()

Test2 = """
/x 4 def
/g { x stack } def
/f { /x 7 def g } def
f
"""

print("Test2 Dynamic")
interpreter(Test2,'dynamic')

clear()
clearDictStack()

print("Test2 Static")
interpreter(Test2,'static')

clear()
clearDictStack()

Test3 = """
/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C } def
B
"""

print("Test3 Dynamic")
interpreter(Test3,'dynamic')

clear()
clearDictStack()

print("Test3 Static")
interpreter(Test3,'static')

clear()
clearDictStack()

print()
print("####################### Provided Tests End ########################")

print()
print("####################### My Testing Starts ########################")
print()

def Test1():
    MyTest1 = "5 4 add stack"
    print("My Test 1 Dynamic:")
    interpreter(MyTest1,'dynamic')
    if opstack != [9]:
        print("Test 1 dynamic failed")
        return False
    clear()
    clearDictStack()
    print("My Test 1 Static:")
    interpreter(MyTest1,'static')
    if opstack != [9]:
        print("Test 1 static failed")
        return False
    clear()
    clearDictStack()
    return True

def Test2():
    MyTest2 = "/m 3 def /n 4 def /g { m n add } def /blah { /m 10 def /n 5 def g } def blah stack "
    print("My Test 2 Dynamic:")
    interpreter(MyTest2,'dynamic')
    if opstack != [15]:
        print("Test 2 dynamic failed")
        return False
    clear()
    clearDictStack()
    print("My Test 2 Static:")
    interpreter(MyTest2,'static')
    if opstack != [7]:
        print("Test 2 static failed")
        return False
    clear()
    clearDictStack()
    return True

def Test3():
    MyTest3 = "/m 3 def /n 4 def /blah { /m 10 def /n 5 def } def blah m n add stack"
    print("My Test 3 Dynamic:")
    interpreter(MyTest3,'dynamic')
    if opstack != [15]:
        print("Test 3 dynamic failed")
        return False
    clear()
    clearDictStack()
    print("My Test 3 Static:")
    interpreter(MyTest3,'static')
    if opstack != [7]:
        print("Test 3 static failed")
        return False
    clear()
    clearDictStack()
    return True

def Test4():
    MyTest4 = "/y 10 def /x 15 def /B { x y add } def /C{ /x 2 def B stack} def" \
              "/A { /y 4 def /B { -5 -10 add } def C } def A"
    print("My Test 4 Dynamic:")
    interpreter(MyTest4,'dynamic')
    if opstack != [-15]:
        print("Test 4 dynamic failed")
        return False
    clear()
    clearDictStack()
    print("My Test 4 Static:")
    interpreter(MyTest4,'static')
    if opstack != [25]:
        print("Test 4 static failed")
        return False
    clear()
    clearDictStack()
    return True

def Test5():
    MyTest5 = "stack"
    print("My Test 5 Dynamic:")
    interpreter(MyTest5,'dynamic')
    if opstack != []:
        print("Test 5 dynamic failed")
        return False
    clear()
    clearDictStack()
    print("My Test 5 Static:")
    interpreter(MyTest5,'static')
    if opstack != []:
        print("Test 5 static failed")
        return False
    clear()
    clearDictStack()
    return True


def Testing():
    if Test1() and Test2() and Test3() and Test4() and Test5():
        print("All tests passed!")
    else:
        print("Testing failed")


Testing()



print()
print("####################### My Testing Ends ########################")
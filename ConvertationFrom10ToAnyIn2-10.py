# except any more than 10
# basically to any scale in 2-10

def From10ToAny(a, NumberSystem):
    b = ''
    while a > 0:
        for i in range (0, len(str(a))):
            b += str(a % NumberSystem)
            a //= NumberSystem
    return b[::-1]

#tests
print( From10ToAny(112, 8) )
print( From10ToAny(1000, 8) )
print( From10ToAny(1000, 9) )
print( From10ToAny(654, 3) )
print( From10ToAny(100, 2) )
print( From10ToAny(48, 10) )
print( From10ToAny(64, 2) )
print( From10ToAny(10, 2) )
print( From10ToAny(6, 6) )
print( From10ToAny(6, 6) )
print( From10ToAny(78, 7) )
print( From10ToAny(10, 16) ) # example of not working, primitive function
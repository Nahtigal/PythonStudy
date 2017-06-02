class MyErr (Exception):
    mess='Less then zero'

a=-10
try:
    assert a>0
        
except AssertionError:
    print 'Assertion Error'
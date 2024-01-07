#finally section always runs even after function returns something.
# try:
#   some code that may return error
# except:
#   handling code
# finally:
#   handling finally code   

def my_function():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter the index:"))
        print(l[i])
        return 'success'
    except Exception as e:
        print(e)
        return 'fail'
    finally:
        print("finally executed")

x = my_function()
print(x)
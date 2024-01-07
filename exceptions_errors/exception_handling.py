#exception handling is done to make sure that the program in not halted upon error
# try:
#     #some code that could generate error
# except:
#     #handling code

a = input('Enter the number:')
print(f"multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print('this is the end of the line.')
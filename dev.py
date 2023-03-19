

def func(txt):
    msg = "You entered {}".format(txt)
    if txt:
        print(msg)
    else:
        print('No message!')
    
    
def main():
    func('testing')



if __name__ == '__main__':
    main()
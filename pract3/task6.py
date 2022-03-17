import logging
import datetime


def run_with_log(func):
    if func[0] == "Done":
        logging.info(" %s is Done!\n", func[1])
    else:
        logging.warning(" In %s error is: %s, %s, %s", func[0], func[1], type(func[1]), (func[1]).__traceback__)
        logging.error(" An error has happened!\n")

def func_1():
    try:
        x = 10 / 0
        return("Done", "func_1()")
    except Exception as e:
        return ("func_1()", e)

def func_2():
    s = 'ferew'
    try:
        s[3] = 'f'
        return ("Done", "func_2()")
    except Exception as e:
        return ("func_2()", e)

def func_3():
    try:
        a.append(3)
        return ("Done", "func_3()")
    except Exception as e:
        return ("func_3()", e)

def func_4():
    try:
        x = 4 + 5
        return ("Done", "func_4()")
    except Exception as e:
        return ("func_4()", e)

def func_5():
    try:
        x = 4 + 5
        x.append(4)
        return ("Done", "func_5()")
    except Exception as e:
        return ("func_5()", e)

def func_6():
    a = [1, 2, 3, 4]
    try:
        print(a[4])
        return ("Done", "func_6()")
    except Exception as e:
        return ("func_6()", e)

def func_7():
    x = 0
    y = '1'
    try:
        z = x + y
        return ("Done", "func_7()")
    except Exception as e:
        return ("func_7()", e)

def func_8():
    try:
        import xyz
        return ("Done", "func_8()")
    except Exception as e:
        return ("func_8()", e)

def func_9():
    d = {'a' : 5, 'b': 6}
    try:
        d['c'] = 5
        return ("Done", "func_9()")
    except Exception as e:
        return ("func_9()", e)

def func_10():
    try:
        a, b, c = [1, 2, 3, 4]
        return ("Done", "func_10()")
    except Exception as e:
        return ("func_10()", e)

def func_11():
    d = {'a' : 1, 'b' : 2}
    try:
        print(d['c'])
        return ("Done", "func_11()")
    except Exception as e:
        return ("func_11()", e)

def main():
    """
    The main prog
    """

    logging.basicConfig(filename="logs.log", filemode='w', level=logging.INFO)
    '''
    logging.basicConfig(filename='logs.log', filemode='w',
                        format='%(asctime)s %(msecs)d- %(process)d- % (levelname)s - % (message)s',
                        datefmt = '%d-%b-%y %H:%M:%S %p',
                        level = logging.INFO)
    '''
    logging.debug('This is a debug message\n')
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logging.info(" Program started %s\n", now)
    run_with_log(func_1())
    run_with_log(func_2())
    run_with_log(func_3())
    run_with_log(func_4())
    run_with_log(func_5())
    run_with_log(func_6())
    run_with_log(func_7())
    run_with_log(func_8())
    run_with_log(func_9())
    run_with_log(func_10())
    run_with_log(func_11())
    logging.info(" Program end!")


if __name__ == "__main__":
    main()


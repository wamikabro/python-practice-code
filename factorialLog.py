import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# to disable logging whenever needed
# disabling logging.CRITICAL will disable all the levels down CRITICAL
# CRITICAL bieng top level, means all levels getting disabled.
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')


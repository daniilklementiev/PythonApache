# Logging is a way to track events that happen when some software runs.
import logging

logging.basicConfig(
        filename='logs.txt', 
        level=logging.INFO, 
        format='[%(asctime)s] - [%(levelname)s] in [%(filename)s::%(lineno)d] : %(message)s with %(args)s',
        datefmt='%Y-%m-%d %H:%M:%S')

import i10_module

def main() -> None:
    
    i10_module.log_warning()
    logging.info('Start program')
    logging.error('DAO error', {'sql': 'SELECT * FROM users;', 'err': 'Syntax error'})


if __name__ == '__main__':
    main()
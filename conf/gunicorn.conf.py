import multiprocessing

bind = '0.0.0.0:8080'
workers = multiprocessing.cpu_count() * 2 + 1
logfile = '/home/soad/Programming/Projects/web/Django/kupikrovat_ru/log/gunicorn.log'
loglevel = 'info'

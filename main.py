import os
import schedule
import time
import logging

script_dir = os.path.dirname(os.path.realpath(__file__))
LOG_FOLDER = os.path.join(script_dir, 'logs')
os.makedirs(LOG_FOLDER, exist_ok=True)

# Configurar o logger
log_file = os.path.join(LOG_FOLDER, "logfile.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def job1():
  print("Primeiro JOB 5 segundos!")
  logging.info("Primeiro JOB 5 segundos!")

def job2():
  print("Segundo JOB 9 segundos!")  
  logging.info("Segundo JOB 9 segundos!")

def job3():
  print("Terceiro JOB 21 segundos!")  
  logging.info("Terceiro JOB 21 segundos!") 

schedule.every(5).seconds.do(job1)
schedule.every(9).seconds.do(job2)
schedule.every(21).seconds.do(job3)

while True:
  schedule.run_pending()
  time.sleep(1)

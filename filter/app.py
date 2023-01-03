import os
from random import randint
from datetime import datetime, timedelta

# Fijar la fecha de inicio
start_date = datetime(2023, 1, 1)

# Iterar sobre los días del año
for i in range(1, 16):
    # Generar un número aleatorio de commits para el día actual
    for j in range(0, randint(1, 20)):
        # Calcular la fecha para el commit
        commit_date = start_date + timedelta(days=i)
        d = commit_date.strftime("%Y-%m-%d")
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -am "commit"')

os.system('git push -u origin main')

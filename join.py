
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(100000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['rgpps.zip.000.COOL', 'rgpps.zip.001.COOL', 'rgpps.zip.002.COOL', 'rgpps.zip.003.COOL', 'rgpps.zip.004.COOL', 'rgpps.zip.005.COOL', 'rgpps.zip.006.COOL', 'rgpps.zip.007.COOL', 'rgpps.zip.008.COOL', 'rgpps.zip.009.COOL', 'rgpps.zip.010.COOL', 'rgpps.zip.011.COOL', 'rgpps.zip.012.COOL', 'rgpps.zip.013.COOL', 'rgpps.zip.014.COOL', 'rgpps.zip.015.COOL', 'rgpps.zip.016.COOL', 'rgpps.zip.017.COOL', 'rgpps.zip.018.COOL', 'rgpps.zip.019.COOL', 'rgpps.zip.020.COOL', 'rgpps.zip.021.COOL', 'rgpps.zip.022.COOL', 'rgpps.zip.023.COOL', 'rgpps.zip.024.COOL', 'rgpps.zip.025.COOL', 'rgpps.zip.026.COOL', 'rgpps.zip.027.COOL', 'rgpps.zip.028.COOL', 'rgpps.zip.029.COOL', 'rgpps.zip.030.COOL', 'rgpps.zip.031.COOL', 'rgpps.zip.032.COOL'],'rgpps.zip')
print('unziping')
with zipfile.ZipFile('rgpps.zip', 'r') as zip_ref:
    zip_ref.extractall('rgpps')
os.remove('rgpps.zip')
os.remove('join.py')

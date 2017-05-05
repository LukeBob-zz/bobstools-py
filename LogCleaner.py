
#!/usr/bin/env python3
## Author: LukeBob
import os

dur_list = []
file_list = []

def removal(file_path):
    if file_path.endswith('.gz'):
        try:
            os.system('rm {}'.format(file_path))
            print('Removing {}'.format(file_path))
        except:
            raise

def list_files(startpath):    
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        for f in files:
            if f.endswith('.gz'):
                dur = os.path.basename(root)
                filez = f
                dur_list.append(dur)
                file_list.append(f)

def main():    
    a=0
    list_files('/var/log/')
    for file in file_list:
        a=a+1
        
    print('Found: {} Files\n'.format(str(a)))
    
    if a > 1:
        for b, c in zip(dur_list, file_list):
            file_path = '/var/log/'+b+'/'+c
            removal(file_path)
        print('\nRemoved {} Archived Log Files'.format(a))
    else:
        print('Exiting')
        exit(0)

if __name__ == '__main__':
    main()

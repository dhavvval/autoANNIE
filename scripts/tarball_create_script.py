import os, time

# script to create tar-ball for grid submission scripts
# usage: python3 scripts/tarball_create_script.py

# ---- Configuration (must match master_script.py settings) ----
user         = os.environ.get('USER', '<user>')   # ANNIE username — defaults to $USER env var; override if different
tarball_name = 'MyToolAnalysis_grid.tar.gz'        # must match TA_tar_name in master_script.py
folder_name  = 'EventBuilding/'                    # must match TA_folder in master_script.py
# ---------------------------------------------------------------

folder_path = '/exp/annie/app/users/' + user + '/'

tar_command = 'tar -czvf ' + tarball_name + ' -C ' + folder_path + ' ' + folder_name

print('\nTar-ing folder (details below)')
print(' - tar-ball name: ' + tarball_name)
print(' - folder path:   ' + folder_path)
print(' - folder name:   ' + folder_name)
print('\n')
print('Full command: ' + tar_command)
print('\n')

time.sleep(3)

os.system(tar_command)

print('\ndone')

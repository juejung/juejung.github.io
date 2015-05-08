import os, shutil

#target = input( 'Enter full directory path: ')
#prefix = input( 'Enter prefix: ')
srcDir= 'C://Dropbox//Towson//Teaching//3_ComputationalEconomics//Lectures'

for root, dirs, files in os.walk(srcDir):
    for file in files:
        if file[0:6] == 'Script':
            if file[-3:]=='.py':
                file1 = file[:-3] + '.txt'
                print file1
                shutil.copy(os.path.join(root, file), os.path.join(root,file1))
            elif file[-2:]=='.R':
                file1 = file[:-2] + '.txt'
                print file1
                shutil.copy(os.path.join(root, file), os.path.join(root,file1))
        if file[0:8] == 'Homework':
            if file[-3:]=='.py':
                file1 = file[:-3] + '.txt'
                print file1
                shutil.copy(os.path.join(root, file), os.path.join(root,file1))
            elif file[-2:]=='.R':
                file1 = file[:-2] + '.txt'
                print file1
                shutil.copy(os.path.join(root, file), os.path.join(root,file1))





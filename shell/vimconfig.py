import os
#buid ctags 
os.system('ctags -R --c++-kinds=+px --fields=+iaS --extra=+q')
os.system('cscope -Rbq')
dir=os.getcwd()

#write tags into ~/.vimrc
f=open('/root/.vimrc','a')
f.write('\nset tags='+dir+'/tags')
f.write('\ncs add '+dir+'/cscope.out')



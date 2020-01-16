# import getpass

# user = getpass.getuser()
# passwd = getpass.getpass()

# if svc_login(user, passwd):    # You must write svc_login()
#    print('Yay!')
# else:
#    print('Boo!')

import subprocess
out_bytes = subprocess.check_output(['ping',"www.baidu.com"])
out_text = out_bytes.decode('asc')
print(out_text)

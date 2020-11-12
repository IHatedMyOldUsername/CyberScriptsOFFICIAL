import grp
import os

def sudolist():
    for group in grp.getgrall():
        if group.gr_name == 'sudo':
            return(group.gr_mem)

def adduseradmin(user):
    os.system('sudo gpasswd -a {} sudo'.format(user))
    
def remuseradmin(user):
    os.system('sudo gpasswd -d {} sudo'.format(user))

def enableFirewall():
    os.system('sudo ufw enable')

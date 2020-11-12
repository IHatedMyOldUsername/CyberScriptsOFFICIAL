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

def updateSystem():
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')

def removeUnneeded():
    os.system('sudo apt-get remove kismet nmap')
    os.system('sudo systemctl stop apache2')
    os.system('sudo systemctl stop apache2')

def configureSSH():
    with open('/etc/ssh/sshd.config', 'rw') as sshFile:
        sshFileLines = sshFile.readlines()
        cnt = 0
        for line in sshFileLines:
            if 'PermitRootLogin' in line:
                sshFileLines[cnt] = 'PermitRootLogin no\n'
            if 'PermitEmptyPasswords' in line:
                sshFileLines[cnt] = 'PermitEmptyPasswords no\n'
            cnt += 1
        sshFile.write(sshFileLines())
        

def passwordReqs():
    with open('/etc/login.defs', 'rw') as passReqs:
        passReqsLines = passReqsLines.readlines()
        cnt = 0
        for line in PassReqsLines:
            if 'PASS_MAX' in line:
                passReqsLines[cnt] = 'PASS_MAX_DAYS = 90\n'
            else if 'PASS_MIN' in line:
                passReqsLines[cnt] = 'PASS_MIN_DAYS = 10\n'
            else if 'PASS_WARN_AGE' in line:
                passReqsLines[cnt] = 'PASS_WARN_AGE = 7\n'
            cnt += 1
        passReqs.write(passReqsLines)

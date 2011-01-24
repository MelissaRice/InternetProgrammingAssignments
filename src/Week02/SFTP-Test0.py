'''
File: InternetProgrammingLabs/Week02/SFTP-Test0.py
Last Revised: 18 January 2011
Purpose: test scripted sftp transfer to/from bluebox using the paramiko package

Description: SFTP is secure ftp which runs over TCP/IP using SSH (secure shell).
Paramiko is a pure-python package (no C-libraries) which implementing SSH.
I found these tutorials useful in learning paramiko:
http://commandline.org.uk/forum/topic/419/

Details: Before running this script, testfile1 exists here on the local machine
and testfile2 exists on the remote machine. After running the script, both test
files should exist on both machines.
 


Authenticating with a key:

Another way is to use an SSH key:
import os
privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
username = 'warrior'
transport.connect(username = username, pkey = mykey)

Authentication problem:
I was able to find out the problem. 
In my /opt/ssh/etc/sshd_config file I need to uncomment out the line:
HostbasedAuthentication yes
After i di that then now the servers are now working. 


try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect_ex((hostname, port)) 
except Exception, e: 
    print 'Connect failed: ' + str(e) 
    traceback.print_exc() 
    sys.exit(1) 
 
t = paramiko.Transport(sock) 
event = threading.Event() 
t.start_client(event) 
print "started client" 
event.wait(15) 
 
if not t.is_active(): 
    print 'SSH negotiation failed.' 
    sys.exit(1) 
else: 
    print "SSH negotiation sucessful" 
 
print "doing authentication" 
t.auth_password(username, password, event) 
 
 
connect(self, hostkey=None, username='', password=None, pkey=None)
source code 
Negotiate an SSH2 session, and optionally verify the server's host key and 
authenticate using a password or private key. This is a shortcut for 
  start_client, 
  get_remote_server_key, and 
  Transport.auth_password or 
  Transport.auth_publickey. Use those methods if you want more control.

You can use this method immediately after creating a Transport to negotiate encryption with a server. If it fails, an exception will be thrown. On success, the method will return cleanly, and an encrypted session exists. You may immediately call open_channel or open_session to get a Channel object, which is used for data transfer.

Parameters:
hostkey (PKey) - the host key expected from the server, or None if you don't want to do host key verification.
username (str) - the username to authenticate as.
password (str) - a password to use for authentication, if you want to use password authentication; otherwise None.
pkey (PKey) - a private key to use for authentication, if you want to use private key authentication; otherwise None.
Raises:
SSHException - if the SSH2 negotiation fails, the host key supplied by the server is incorrect, or authentication fails.
Note: If you fail to supply a password or private key, this method may succeed, but a subsequent open_channel or open_session call may fail because you haven't authenticated yet. 


server, username, password = ('host', 'username', 'password')
ssh = paramiko.SSHClient()
parmiko.util.log_to_file(log_filename)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#In case the server's key is unknown,
#we will be adding it automatically to the list of known hosts
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#Loads the user's local known host file.
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /tmp')
print "output", ssh_stdout.read() #Reading output of the executed command
error = ssh_stderr.read()
#Reading the error stream of the executed command
print "err", error, len(error) 
 
#Transfering files to and from the remote machine
sftp = ssh.open_sftp()
sftp.get(remote_path, local_path)
sftp.put(local_path, remote_path)
sftp.close()
ssh.close()


'''

import paramiko

logging = True
dateStamp = "2011-01-18-1425"
logFilename = "C:/A/eclipse/projects/InternetProgrammingLabs/src/Week02/sftp-log" + dateStamp + ".txt"
testFilename1 = "testfile1.txt"
testFilename2 = "testfile2.txt"
localFilepath = "C:/A/eclipse/projects/InternetProgrammingLabs/src/Week02/"
remoteFilepath = "/home/mlrice/"

if logging:
    paramiko.util.log_to_file(logFilename)

# Set up the ssh socket to the remote machine and start the sftp client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
try:
   print "creating connection"
   ssh.connect(host, username=username, password=password)
   print "connected"
   yield ssh
finally:
   print "closing connection"
   ssh.close()
   print "closed"
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect('block115397-xwp.blueboxgrid.com', username='mlrice')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /tmp')
print "output", ssh_stdout.read() #Reading output of the executed command
error = ssh_stderr.read()
#Reading the error stream of the executed command
print "err", error, len(error) 

''' 
from contextlib import contextmanagerhost = '192.168.10.142'
username = 'slacker'
password = 'insecure'@contextmanager
def create_ssh(host=host, username=username, password=password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) try:
       print "creating connection"
       ssh.connect(host, username=username, password=password)
       print "connected"
       yield ssh
    finally:
       print "closing connection"
       ssh.close()
       print "closed"
'''

#Transfering files to and from the remote machine
sftp = ssh.open_sftp()


# try moving a file local to remote...
remoteFilename = remoteFilepath + testFilename1
localFilename = localFilepath + testFilename1
sftp.get(remoteFilename, localFilename)

# try moving a file remote to local
remoteFilename = remoteFilepath + testFilename2
localFilename = localFilepath + testFilename2
sftp.put(remoteFilename, localFilename)

sftp.close()
ssh.close()

'''

remoteSocketID = ('block115379-pwc.blueboxgrid.com',22) # host,port    
remoteSocket = paramiko.Transport(remoteSocketID)
try:
    authTypes = []
    authTypes = remoteSocket.connect(username='mlrice',password='')
    #remoteSocket.start_client()
    #authTypes = remoteSocket.auth_password(username="mlrice", fallback=True)
    #remoteSocket.connect(username='mlrice',password='xxx')
except Exception, e: 
    print 'Connect failed: \n' + str(e)
    if authTypes: 
        print str(authTypes) 
    #traceback.print_exc() 
    #sys.exit(1)
    #e = remoteSocket.get_exception() 
    #self.log.warn("do_authenticateWithPassword:: SSHException: %s", e)
    # If it's problem reading the SSH protocol banner, it's likely
    # because the user has specified the wrong details:
    # http://bugs.activestate.com/show_bug.cgi?id=47047
    #if e.args[-1] == "Error reading SSH protocol banner":
        #error_message = "%s:%d is not a recognized SSH server. " \
        #                "Please recheck your %s server and port " \
        #                "configuration." % (self.server, self.port,
        #                                    self.protocol.upper())
        #self._raiseServerException(error_message)
            # else, problem logging in
        #self.log.warn("SSH error: Invalid username/password") 
sftp = paramiko.SFTPClient.from_transport(remoteSocket)

# try moving a file local to remote...
remoteFilename = remoteFilepath + testFilename1
localFilename = localFilepath + testFilename1
sftp.get(remoteFilename, localFilename)

# try moving a file remote to local
remoteFilename = remoteFilepath + testFilename2
localFilename = localFilepath + testFilename2
sftp.put(remoteFilename, localFilename)

# Close the sftp client and remote socket
sftp.close()
remoteSocket.close()


# sftp.put(filepath, localpath) is incorrect.
# This should be sftp.put(localpath, filepath)

'''



'''

Easy SFTP uploading with paramiko
paramiko makes it so easy to use SFTP that it's hard to believe it's legal in this day and age. Command Line Warriors has a wonderful post showing how to use paramiko to do SFTP uploads/downloads.

In this post, I want to share a small helper module called sftp (zip file) (code in post below) that wraps paramiko.SFTPClient and makes uploading/downloading via SFTP even simpler.

First, some usage

Upload or download a file

server = sftp.Server("user", "pass", "example.com")
# upload a file
server.upload("/local/path", "/remote/path")
# download a file
server.download("remote/path", "/local/path")
server.close()
with statement also supported:

with sftp.Server("user", "pass", "example.com") as server:
    server.upload("/local/path", "/remote/path")
Finally, a demo recipe for uploading all the png files from a specified local directory to a specified directory on the server:

# needed for python 2.5
from __future__ import with_statement
import sftp
import glob
from os import path

remote_dir = "/path/on/remote/server/"

with sftp.Server("user", "pass", "www.example.com") as server:
    for image in glob.glob("/local/path/to/*.png"):
        base = path.basename(image)
        server.upload(image, path.join(remote_dir, base))

Now, here's the code for my sftp module:

import paramiko
class Server(object):
    """
    Wraps paramiko for super-simple SFTP uploading and downloading.
    """

    def __init__(self, username, password, host, port=22):

        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def upload(self, local, remote):
        self.sftp.put(local, remote)

    def download(self, remote, local):
        self.sftp.get(remote, local)

    def close(self):
        """
        Close the connection if it's active
        """

        if self.transport.is_active():
            self.sftp.close()
            self.transport.close()

    # with-statement support
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()




it easier to start off with the SSHClient class. It will wrap up all the authentication, and host verification pieces in one package. It also has an open_sftp() convenience method to return an SFTPClient instance.


http://www.minvolai.com/blog/2009/09/how-to-ssh-in-python-using-paramiko/
server, username, password = ('host', 'username', 'password')
ssh = paramiko.SSHClient()
parmiko.util.log_to_file(log_filename)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#In case the server's key is unknown,
#we will be adding it automatically to the list of known hosts
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#Loads the user's local known host file.
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls /tmp')
print "output", ssh_stdout.read() #Reading output of the executed command
error = ssh_stderr.read()
#Reading the error stream of the executed command
print "err", error, len(error) 
 
#Transfering files to and from the remote machine
sftp = ssh.open_sftp()
sftp.get(remote_path, local_path)
sftp.put(local_path, remote_path)
sftp.close()
ssh.close()
The connect method also allows you to provide your own private key, or 
connect to the SSH agent on the local machine or read from the users local key files. 
Click here for a more detailed description of  the connect method's signature.
privkey = paramiko.RSAKey.from_private_key_file (path_to_priv_key_file)
ssh.connect(server, username=username,pkey=privkey )
#private key to use for authentication
or
ssh.connect(server, username=username, key_filename=path_to_priv_key_file)
#the filename, or list of filenames, of optional private key(s)
#to try for authentication
or
ssh.connect(server, username=username, allow_agent=True)
#Connects to the local SSH agent and tries to obtain the private key
or
ssh.connect(server, username=username, look_for_keys=True)
#Searches for discoverable private key files in ~/.ssh/
The Transport Object
It provides more direct control over how the connections are formed and authentication is carried over.   It provides for various   options such as logging debugging information like hex dump, manipulating the algorithms used and their priorities, controlling the authentication methods and their sequence, the type of channels to open, forcing renegotiating keys etc.   It is also possible to start an SSH Server or SFTP Server using this object.
The below example uses the Transport Object to connect:
import os
import paramiko
server, port, username, password = (host, 22, username, password)
parmiko.util.log_to_file(log_filename)
nbytes = 100
An SSH Transport attaches to a stream (usually a socket), negotiates an encrypted session, authenticates, and then creates stream tunnels, called Channels, across the session. Multiple channels can be multiplexed across a single session (and often are, in the case of port forwardings).
trans = paramiko.Transport((host, port))
trans.connect(username = username, password = password)
Next, after authentication, we create a channel of type session
session = trans.open_channel("session")
#Once the channel is established, we can execute only one command.   To execute another command, we need to create another channel
session.exec_command('ls /tmp')
We need to wait till the command is executed or the channel is closed.   recv_exit_status return the result of the exit status of the command executed or -1 if no exit status was given.
exit_status = session.recv_exit_status()
Now the command execution is over and stdout and stderr streams will be linked to the channel and can be read.
stdout_data = []
stderr_data = []
 
while session.recv_ready():
stdout_data.append(session.recv(nbytes))
stdout_data = "".join(stdout_data)
 
while session.recv_stderr_ready():
stderr_data.append(session.recv_stderr(nbytes))
stderr_data = "".join(stderr_data)
 
print "exit status", exit_status
print "output"
print stdout_data
print "error"
print stderr_data
We can also create SFTP client from the Transport Object as below
sftp = paramiko.SFTPClient.from_transport(trans)
sftp.get('remote_path', 'local_path')
sftp.put('local_path', 'remote_path')
sftp.close()
SFTP client object. SFTPClient is used to open an sftp session across an open ssh Transport and do remote file operations.
Personally I prefer to write a wrapper module over the SSHClient api and use that in my day to day needs.
Caveats
Paramiko's SFTPClient is significantly slower compared to sftp or scp, some times by an order of magnitude, especially for huge files.   The scp implementation listed in the Interesting Read below assures to be faster though I've not tested it yet.
Paramiko's SSHClient does not allow for setting a timeout for exec_command.   This means that, in case of the remote_machine not returning the exec_command call, the process would freeze and need to be killed.




'''



import DebDownloader as DebDown
import tkinter as tk
import paramiko
import pysftp

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def download(self):
        DebDown.DownloadDeb(self.Repo.get(), self.Package.get())
    def InstallToDevice(self):
        ip = self.ip.get()
        username = self.username.get()
        password = self.password.get()
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None  
        with pysftp.Connection(ip, username=username, password=password, cnopts=cnopts) as sftp:
            with sftp.cd('/tmp'):
                self.v.set("Placing deb in /tmp temporarly")
                sftp.put('debs/'+ self.Package.get() + '.deb')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        self.v.set("Installing deb")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("dpkg -i /tmp/{}.deb".format(self.Package.get()))
        stdout=ssh_stdout.readlines()
        self.v.set("Removing temporary file")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("rm /tmp/" + self.Package.get() + ".deb")
        ssh.close()
        self.v.set("Finished!")
        
    def create_widgets(self):
        self.label1 = tk.Label(self, text='URL to repo')
        self.label1.pack()
        self.Repo = tk.Entry(self)
        self.Repo.pack()

        self.Packagelabel = tk.Label(self, text='Package name')
        self.Packagelabel.pack()
        self.Package = tk.Entry(self)
        self.Package.pack()
        
        self.Download = tk.Button(self, text="Download", command=self.download)
        self.Download.pack()
        
        self.iplabel = tk.Label(self, text = "Device ip")
        self.iplabel.pack()
        self.ip = tk.Entry(self)
        self.ip.pack()
        
        self.usernamelabel = tk.Label(self, text = "SSH Username")
        self.usernamelabel.pack()
        self.username = tk.Entry(self)
        self.username.pack()

        self.passwordlabel = tk.Label(self, text = "SSH Password")
        self.passwordlabel.pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()
        
        self.install = tk.Button(self, text="Install", command=self.InstallToDevice)
        self.install.pack()
        self.v = tk.StringVar()
        self.progress = tk.Label(self, textvariable=self.v)
        self.progress.pack()
        self.v.set("")
        
root = tk.Tk()
root.title('DebDownloader')
root.geometry("400x300")
app = Application(master=root)
app.mainloop()
        

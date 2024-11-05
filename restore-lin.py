import os;

#dirs_to_process = ["desktop", "documents", "downloads", "music", "pictures", "updates", "videos", "bin", "code"]
dirs_to_process = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Updates", "Videos"]


command = "/usr/bin/rsync"
argfrom = " /mnt/nas/jdrive/Users/jacox/"
argto = " /home/jacox/"
opts = " -avz"
logfile = " /home/jacox/.restorelog"

for count, dname in enumerate(dirs_to_process):
    print("processing ", count, ": ", dname)
    log = ">" + logfile if count == 0 else ">>" + logfile
    full_command = command + opts + argfrom + dname + "/" + argto + dname + "/" + log
    print("full command:", full_command)
    os.system(full_command)


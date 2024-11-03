import os;

dirs_to_process = ["desktop", "documents", "downloads", "music", "pictures", "updates", "videos", "bin", "code"]

command = "c:\\windows\\system32\\robocopy.exe "
arg1 = " c:\\users\\jacox\\"
arg2 = " j:\\users\\jacox\\"
opts = " /mir /copy:dat /xj /s /xj /xa:sh /np /copy:dat /dcopy:dat /r:0"
logpart = " /log:c:\\users\\jacox\\bin\\backuplog.log"
log2part = " /log+:c:\\users\\jacox\\bin\\backuplog.log"

for count, dname in enumerate(dirs_to_process):
    print("processing ", count, ": ", dname)
    log = logpart if count == 0 else log2part
    os.system(command + arg1 + dname + arg2 + dname + opts + log)


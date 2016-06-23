import os,subprocess,collections
 
 
ext_list = []
fpath_list = []
format_list =[]
 
def evaluate_file(file_loc):
    global ext_list, fpath_list
    fpath_list.append(str(file_loc))
    ext_list.append(str(file_loc).split(".")[1])
 
 
def nav_folder(dir_path):
    if os.path.isdir(dir_path):
        files = os.listdir(dir_path)
        for f in files:
            if not f.startswith('.'):
                if os.path.isdir(os.path.join(dir_path,f)):
                    nav_folder(os.path.join(dir_path,f))
                else:
                    evaluate_file(os.path.join(dir_path,f))
    else:
        evaluate_file(dir_path)
 
 
def create_folders(dest_loc):
    unique_fmts = set(sorted(ext_list))
    for fmt in unique_fmts:
        if fmt in format_list or len(format_list)==1:
            if not os.path.isdir(os.path.join(dest_loc,"FO-"+fmt)):
                os.makedirs(os.path.join(dest_loc,"FO-"+fmt))
 
 
def organize(d_loc):
    for file in fpath_list:
        if str(file).split('.')[1] in format_list or len(format_list)==1:
            foldername=os.path.join(d_loc,"FO-"+str(file).split('.')[1])
            fname=str(file).replace("\\","\\")
            print foldername
            print str(file).replace("\\","\\")
            try:
                dfile = open(os.path.join(foldername,fname.split("\\")[-1]),'wb')
                dfile.seek(0)
                sfile = open(fname,'rb')
                dfile.writelines(sfile.read())
                dfile.close()
                sfile.close()
                #Use the below line to move the file
                #os.rename(fname,os.path.join(foldername,fname.split("\\")[-1]))
            except Exception as e:
                print e.message
def main():
    global format_list
    s_loc = raw_input("Enter the source location:")
    d_loc = raw_input("Enter the destination location:")
    fmt_list = raw_input("Enter the format to organize (, seperated):")
    for fmt in fmt_list.split(','):
        format_list.append(fmt)
    nav_folder(s_loc)
    create_folders(d_loc)
    organize(d_loc)
    print set(sorted(ext_list))
    print fpath_list
 
main()

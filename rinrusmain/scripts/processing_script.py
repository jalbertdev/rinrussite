import os, shutil, sys


def get_res_chain(residues,chains):
    length=min(len(residues),len(chains))
    res=""
    for x in range(length):
        res+=chains[x]
        res+=":"
        res+=residues[x]
        res+=","
    res=res[:len(res)-1]
    return res

def pymol_res(res):
    result=""
    for res in res:
        result+=res
        result+=','
    return result

def run_scripts(path, residues, chains, name): 
    #located in rinrussite folder
    reschain=get_res_chain(residues,chains) #format residue and chain into proper format to run scripts m
    file_path="rinrusmain/static/files"
    path=file_path+path
    home=os.getcwd() #to return 
    directory=(path[:path.rfind('/')])

    #Step 0: Logging
    os.chdir(home+"/"+directory) #move into file folder
    os.system("pwd")
    f = open("script_log.txt", 'w')
    temp=sys.stdout
    sys.stdout = f
    

    #Step 1: Probe
    probe_string='./../../../scripts/rinrus_algs/probe -unformated -self "all" '
    pdb_path=""+name+".pdb"
    probe_string+=pdb_path
    probe_path=""+name+".probe" #make probe file path
    probe_string+=" > " + probe_path
    print(probe_string)
    os.system(probe_string)
    print()
  

    #Step 2: Probe2Rins
    #python3 probe2rins.py -f 3bwm_h.probe -s A:300,A:301,A:302
    probe2rins_string="python3 ../../../scripts/rinrus_algs/probe2rins.py -f "
    probe2rins_string+=probe_path
    probe2rins_string+=" -s "+reschain
    print(probe2rins_string)
    os.system(probe2rins_string)
    print()

    #Step 3: Probe_freq_2pdb
    #python3 ../bin/probe_freq_2pdb.py pdb.ent file.probe freq_per_res.dat A,300,A,301,A,302
    probe_freq_string="python3 ../../../scripts/rinrus_algs/probe_freq_2pdb.py " + pdb_path + " " + probe_path + " "
    freq_path="freq_per_res.dat"
    if not os.path.exists(freq_path):
        print("!!!!!!!!!!!!!!  Step 2 Failed  !!!!!!!!!!!!!!\n")
    reschain2=reschain.replace(':',',')
    probe_freq_string+= freq_path + " " + reschain2
    print(probe_freq_string)
    os.system(probe_freq_string)
    print("")
    #creates a ton of pdb files called res_XX.pdb

    #Step 4+5: Pymol scripts and Pymol
    #interate through res_xx.pdb
    log_path="log.pml"
    if not os.path.exists(log_path):
        print("!!!!!!!!!!!!!  Step 3 Failed  !!!!!!!!!!!!!!\n")
    os.system("ls")
    step4=False
    for filename in os.listdir("."):
        if filename.endswith(".pdb") and  filename.startswith('res_') and not filename.endswith("_h.pdb"): #CHECK SECOND PART
            #python3 ../bin/pymol_scripts.py res_5.pdb 301,302
            step4=True
            pymol_string="python3 ../../../scripts/rinrus_algs/pymol_scripts.py "+filename+" "+pymol_res(residues)
            print(pymol_string)
            os.system(pymol_string)
            os.system("pymol -qc "+log_path)
        print(filename)
    if not step4:
        print("\n!!!!!!!!!!!! Step 4 and 5 Failed  !!!!!!!!!!!!!!\n")

    #Step 6 Create res folder
    os.mkdir("./res")
    for filename in os.listdir("."):
        if filename.endswith(".pdb") and  filename.startswith('res_'): #CHECK SECOND PART
            shutil.move(filename,"res/"+filename)



    #Step 7 Create Zip File
    f.close() #close logging file
    sys.stdout=temp
    os.chdir(home) #reset current directory location
    folder_path=directory
    zip_path=folder_path[:folder_path.rfind('/')+1]+name
    shutil.make_archive(zip_path, 'zip', folder_path)
    if not step4:
        return "Simulation Failed: Check Log File"
    else:
        return "good"





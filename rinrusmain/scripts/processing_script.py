import os, shutil


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

    #Step 1
    os.chdir(home+"/"+directory) #move into file folder
    os.system("pwd")
    probe_string='./../../../scripts/rinrus_algs/probe -unformated -self "all" '
    pdb_path=""+name+".pdb"
    probe_string+=pdb_path
    probe_path=""+name+".probe" #make probe file path
    probe_string+=" > " + probe_path
    print(probe_string)
    os.system(probe_string)

    #Step 2
    #python3 probe2rins.py -f 3bwm_h.probe -s A:300,A:301,A:302
    
    probe2rins_string="python3 ../../../scripts/rinrus_algs/probe2rins.py -f "
    probe2rins_string+=probe_path
    probe2rins_string+=" -s "+reschain
    print(probe2rins_string)
    os.system(probe2rins_string)

    #Step 3
    #python3 ../bin/probe_freq_2pdb.py pdb.ent file.probe freq_per_res.dat A,300,A,301,A,302
    probe_freq_string="python3 ../../../scripts/rinrus_algs/probe_freq_2pdb.py " + pdb_path + " " + probe_path + " "
    freq_path="freq_per_res.dat"
    reschain2=reschain.replace(':',',')
    probe_freq_string+= freq_path + " " + reschain2
    print(probe_freq_string)
    os.system(probe_freq_string)
    #creates a ton of pdb files called res_XX.pdb

    #Step 4+5
    #interate through res_xx.pdb
    log_path="log.pml"
    os.system("ls")
    for filename in os.listdir("."):
        if filename.endswith(".pdb") and  filename.startswith('res_'): #CHECK SECOND PART
            #python3 ../bin/pymol_scripts.py res_5.pdb 301,302
            pymol_string="python3 ../../../scripts/rinrus_algs/pymol_scripts.py "+filename+" "+pymol_res(residues)
            print(pymol_string)
            os.system(pymol_string)
            os.system("pymol -qc "+log_path)
        print(filename)
    
    
    #Step 6 Create Zip File
    os.chdir(home) #reset current directory location
    folder_path=directory
    zip_path=folder_path[:folder_path.rfind('/')+1]+name
    shutil.make_archive(zip_path, 'zip', folder_path)
    return zip_path





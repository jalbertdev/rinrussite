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

def run_scripts(path, residues, chains, name): 
    #located in rinrussite folder
    reschain=get_res_chain(residues,chains) #format residue and chain into proper format to run scripts 
    file_path="rinrusmain/static/files"
    path=file_path+path
    print(path)

    #USE BIN FOLDER SCRIPTS
    #Step 1
    os.system("chmod u+x rinrus_algs/probe") #move to install instructions
    probe_string='./rinrus_algs/probe -unformated -self "all" '
    probe_string+=path
    probe_path=(path[:path.rfind('.')])+".probe" #make probe file path
    probe_string+=" > " + probe_path
    os.system(probe_string)

    #Step 2

    #SCRIPTS IN BIN
    #python3 probe2rins.py -f 3bwm_h.probe -s A:300,A:301,A:302
    probe2rins_string="python rinrusAlgs/probe2rins.py -f "
    probe2rins_string+=probe_path
    probe2rins_string+=" -s "+reschain
    os.system(probe2rins_string)

    #Step 3
    #python3 ../bin/probe_freq_2pdb.py pdb.ent file.probe freq_per_res.dat A,300,A,301,A,302
    probe_freq_string="python rinrusAlgs/probe_freq_2pdb.py " + path + " " + probe_path + " "
    freq_path=""
    probe_freq_string+= freq_path + " " + reschain
    os.system(probe_freq_string)
    #creates a ton of pdb files called res_XX.pdb

    #Step 4
    #interate through res_xx.pdb
    for filename in os.listdir(directory):
        if filename.endswith(".FILETYPE"): #add correct file types
            #python3 ../bin/pymol_scripts.py res_5.pdb 301,302
            log_path=""
            os.system("pymol -qc "+log_path)
            continue
        else:
            continue
    
    #Step 6 Create Zip File
    folder_path=path[:path.rfind('/')]
    output_path=output_path[:output_path.rfind('/')]+name+".zip"
    shutil.make_archive(output_path, 'zip', folder_path)
    zipPath="" #path of the zip file
    return zipPath





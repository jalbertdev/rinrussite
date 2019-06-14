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
        result.append(res)
        result.append(',')
    return result

def run_scripts(path, residues, chains, name): 
    #located in rinrussite folder
    reschain=get_res_chain(residues,chains) #format residue and chain into proper format to run scripts m
    file_path="rinrusmain/static/files"
    path=file_path+path
    directory=(path[:path.rfind('/')])
    print(path)
    print(reschain)
    print(directory)
    

    #USE BIN FOLDER SCRIPTS
    #Step 1
    probe_string='./rinrus_algs/probe -unformated -self "all" '
    probe_string+=path
    probe_path=(path[:path.rfind('.')])+".probe" #make probe file path
    probe_string+=" > " + probe_path
    os.system(probe_string)

    #Step 2
    #python3 probe2rins.py -f 3bwm_h.probe -s A:300,A:301,A:302
    probe2rins_string="python3 rinrusAlgs/probe2rins.py -f "
    probe2rins_string+=probe_path
    probe2rins_string+=" -s "+reschain
    os.system(probe2rins_string)

    #Step 3
    #python3 ../bin/probe_freq_2pdb.py pdb.ent file.probe freq_per_res.dat A,300,A,301,A,302
    probe_freq_string="python3 rinrusAlgs/probe_freq_2pdb.py " + path + " " + probe_path + " "
    freq_path=(path[:path.rfind('/')])+"/freq_per_res.dat"
    print(freq_path)
    #HERE
    reschain2=reschain#replace : with ,
    probe_freq_string+= freq_path + " " + reschain
    os.system(probe_freq_string)
    #creates a ton of pdb files called res_XX.pdb

    #Step 4
    #interate through res_xx.pdb
    log_path=(path[:path.rfind('/')])+"/log.pml"
    for filename in os.listdir(directory):
        if filename.endswith(".FILETYPE") and  filename.startswith('res_'): #CHECK SECOND PART
            #python3 ../bin/pymol_scripts.py res_5.pdb 301,302
            pymol_string="python3 rinrusAlgs/pymol_scripts.py "+directory+"/"+filename+" "+pymol_res(residues)
            os.system(pymol_string)
            os.system("pymol -qc "+log_path)
            continue
        else:
            continue
    
    #Step 6 Create Zip File
    folder_path=directory
    zip_path=output_path[:folder_path.rfind('/')+1]+name+".zip"
    shutil.make_archive(zip_path, 'zip', folder_path)
    return zipPath





import os, shutil
#import rinrus_algs.probe2rins as p2r

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

    #Step 1
    os.system("chmod u+x rinrus_algs/probe")
    probe_string='./rinrus_algs/probe -unformated -self "all" '
    probe_string+=path
    probe_path=(path[:path.rfind('.')])+".probe" #make probe file path
    probe_string+=" > " + probe_path
    os.system(probe_string)

    #Step 2
    probe2rins_string="python rinrusAlgs/probe2rins.py "
    probe2rins_string+=probe_path
    probe2rins_string+=reschain
    os.system(probe2rins_string)

    #Step 3
    #./../scripts/probe_freq_2pdb.py 3bwm_h_mg_ts_wGlu199.ent file.probe freq_per_res.dat  A,300,A,301,A,302
    probe_freq_string="python rinrusAlgs/probe_freq_2pdb.py " + path + " " + probe_path + " "
    freq_path=""
    probe_freq_string+= freq_path + " " + reschain
    os.system(probe_freq_string)

    #Step 4
    log_path=""
    os.system("pymol -qc "+log_path)

    #Step 5
    for filename in os.listdir(directory):
        if filename.endswith(".FILETYPE"): #add correct file types
            #python pymol_scripts.py filename 301,302
            continue
        else:
            continue
        
    #Step 6 Create Zip File
    folder_path=path[:path.rfind('/')]
    output_path=output_path[:output_path.rfind('/')]+name+".zip"
    shutil.make_archive(output_path, 'zip', folder_path)
    zipPath="" #path of the zip file
    return zipPath





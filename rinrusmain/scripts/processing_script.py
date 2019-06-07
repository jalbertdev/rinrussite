import os, shutil
#import rinrus_algs.probe2rins as p2r

def run_scripts(path, residues, chains,name): #path in the format starting at the static folder
    os.system("chmod u+x rinrus_algs/probe")
    probe_string='./rinrus_algs/probe -unformated -self "all"'
    probe_string+=path
    
    probe_path=(path[:path.rfind('/')])+name+".probe" #make probe file path
    probe_string+=" > "
    probe_string+=probe_path
    os.system(probe_string)

    probe2rins_string="python rinrusAlgs/probe2rins.py "
    probe2rins_string+=probe_path
    probe2rins_string+=" A:300,A:301,A:302"
    os.system(probe2rins_string)

    #probe_freq_2pdb.py: python ../scripts/probe_freq_2pdb.py 3bwm_h_mg_ts_wGlu199.ent file.probe file.probe A,300,A,301,A,304

    pymol -qc log.pymol

    for files:
        #python pymol_scripts.py filename 301,302

    shutil.make_archive(outputpath, 'zip', folderpath)





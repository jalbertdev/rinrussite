import os
#import rinrus_algs.probe2rins as p2r

def runScripts(path):
    os.system("chmod u+x rinrus_algs/probe")
    probe_string="./rinrus_algs/probe "
    probe_string+=path
    os.system(probe_string)

    probe2rins_string="python rinrusAlgs/probe2rins.py
    p2r.run()



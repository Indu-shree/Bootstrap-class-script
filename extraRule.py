import os
import logging 
from pprint import *
from bs4 import BeautifulSoup
import itertools
from numpy.lib.function_base import append
logging.basicConfig(filename="/home/spaneos/Indushree/BOOTSTRP_3/share/Remaining_Rules/other_folder/01_.log", 
                    format='%(asctime)s %(message)s %(levelname)s', 
                    filemode='w',
                    level='DEBUG')  
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger() 

filelist = []
count  =0
directory = '/home/spaneos/Desktop/STAGING_BOOTSTRAP_UPGRADE/dhi-angular/src/app/+spaneos-admin/admin-course-enrollment'
count_dict = {}
file_count = 0
total_changes = 0
for root,dirnames,filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".html"):
            count_dict[os.path.join(root,filename)] = {}
            count_dict[os.path.join(root,filename)]["<mfBootstrapPaginator>"] =0
            filedata = open(os.path.join(root,filename))
            for line in filedata:               
                if "href" in line:
                    count_dict[os.path.join(root,filename)]["<mfBootstrapPaginator>"] +=1
final_list =[]
for k, v in count_dict.items():     
    if count_dict[k]["<mfBootstrapPaginator>"] > 0 and count_dict[k]["<mfBootstrapPaginator>"] != 0:
        final_list.append(count_dict) if count_dict not in final_list else final_list 

logging.debug(pformat(final_list))
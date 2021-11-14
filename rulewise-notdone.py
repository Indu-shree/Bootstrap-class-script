import os
import logging 
from pprint import *
from bs4 import BeautifulSoup
import itertools
logging.basicConfig(filename="/home/spaneos/Indushree/BOOTSTRP_3/share/not_completed/common/13NC_student-pre-registration-config", 
                    format='%(asctime)s %(message)s %(levelname)s', 
                    filemode='w',
                    level='DEBUG')  
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger() 
rules_dict = {
3:['form-horizontal'],
5:['radio','radio-inline','checkbox','checkbox-inline'],
9:['btn-default'],
10:['btn-xs'],
11:['input-group-btn','input-group-addon'],
14:['btn-group-justified'],
15:['btn-group-xs'],
16:['navbar-form'],
18:['pagination'],
19:['previous','next'],
20:['label'],
21:['glyphicon'],
22:['page-header'],
24:['in'],
25:['panel-default','panel'],
26:['panel-group'],
31:['breadcrumb'],
32:['item']
}
filelist = []
directory = '/home/spaneos/Desktop/STAGING_BOOTSTRAP_UPGRADE/dhi-angular/src/app/+student-pre-registration-config'
count_dict = {}
file_count = 0
total_changes = 0
for root,dirnames,filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".html"):
            pprint(filename)
            filedata = open(os.path.join(root,filename))
            count_dict[os.path.join(root,filename)] = {}
            for k,v in rules_dict.items():
                count_dict[os.path.join(root,filename)][k] = {}
                for rule in v:
                    count_dict[os.path.join(root,filename)][k][rule] = 0
            # for f in filedata:
            #     for key,value in rules_dict.items():
                    # for v in value:
                    #     if v == '<label':
                    #         if v in f:
                    #             count_dict[os.path.join(root,filename)][key][v] += 1
                    #             total_changes += 1
            soup = BeautifulSoup(filedata,"html.parser")
            lst = [node['class'] for node in soup.find_all() if node.has_attr('class')]
            ruleList = list(itertools.chain.from_iterable(lst))
            for key,value in rules_dict.items():
                    for v in value:
                        if v in ruleList:
                            filelist.append(filename) if filename not in filelist else filelist
                            count_dict[os.path.join(root,filename)][key][v] = ruleList.count(v)
                            total_changes += ruleList.count(v)
            # print(ruleList)
# pprint(count_dict)
final_dict ={}
for k,v in rules_dict.items():
    final_dict[k]={}
    for val in v:
        final_dict[k][val]=[]
    
for k,v in final_dict.items():
    for rname,rval in v.items():
        for key,value in count_dict.items():
            for rk,r in value.items():
                for val,vel  in r.items():
                    if vel > 0:
                        if rk == k and rname == val:
                            rdict ={}
                            rdict[key]= vel
                            final_dict[k][rname].append(rdict) if rdict not in final_dict[k][rname] else final_dict[k][rname]

final_dict["number of files"] = len(filelist)
final_dict["total Changes"] = total_changes

logging.debug(pformat(final_dict))
# pprint(final_dict)
                             




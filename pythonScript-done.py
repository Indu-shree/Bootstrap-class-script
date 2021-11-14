import os
import logging 
from pprint import *
from bs4 import BeautifulSoup
import itertools
logging.basicConfig(filename="doneRules.log", 
                    format='%(asctime)s %(message)s %(levelname)s', 
                    filemode='w',
                    level='DEBUG')  
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger() 
rules_dict = {1:['col-md-offset','col-sm-offset','col-lg-offset'],
2:['table-condensed'],
4:['control-label'],
6:['input-lg','input-sm'],
7:['help-block'],
8:['form-control-static'],
12:['img-responsive'],
13:['divider'],
17:['navbar-fixed-top','navbar-fixed-bottom'],
23:['list-group-item'],
27:['panel-heading'],
28:['panel-title'],
29:['panel-body'],
30:['panel-footer']
}
directory = '/home/spaneos/dhi-mcq-angular/src'
count_dict = {}
file_count = 0
total_changes = 0
for root,dirnames,filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".html"):
            file_count += 1
            filedata = open(os.path.join(root,filename))
            count_dict[os.path.join(root,filename)] = {}
            for k,v in rules_dict.items():
                count_dict[os.path.join(root,filename)][k] = {}
                for rule in v:
                    count_dict[os.path.join(root,filename)][k][rule] = 0
            soup = BeautifulSoup(filedata,"html.parser")
            lst = [node['class'] for node in soup.find_all() if node.has_attr('class')]
            ruleList = list(itertools.chain.from_iterable(lst))
            for key,value in rules_dict.items():
                    for v in value:
                        count_dict[os.path.join(root,filename)][key][v] = 0
                        if v == 'col-md-offset' or 'col-sm-offset' or 'col-lg-offset':
                            for rules in ruleList:
                                if v in rules:
                                    count_dict[os.path.join(root,filename)][key][v] += 1
                                    total_changes += 1
                        if v in ruleList:
                            count_dict[os.path.join(root,filename)][key][v] = ruleList.count(v)
            count_dict["number of files"] = file_count 
            count_dict["total Changes"] = total_changes

logging.debug(pformat(count_dict))
             

            

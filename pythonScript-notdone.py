import os
import logging 
from pprint import *
from bs4 import BeautifulSoup
import itertools
logging.basicConfig(filename="notDoneRules.log", 
                    format='%(asctime)s %(message)s %(levelname)s', 
                    filemode='w',
                    level='DEBUG')  
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger() 
rules_dict = {3:['form-horizontal'],
5:['radio','radio-inline','checkbox','checkbox-inline'],
9:['btn-default'],
10:['btn-xs'],
11:['input-group-btn'],
14:['btn-group-justified'],
15:['btn-group-xs'],
16:['navbar-form'],
18:['pagination'],
19:['previous','next'],
20:['<label'],
21:['glyphicon glyphicon'],
22:['page-header'],
24:['in'],
25:['panel-default'],
26:['panel-group'],
31:['breadcrumb'],
32:['item']
}
directory = '/home/spaneos/dhi-university-angular/src'
count_dict = {}

for root,dirnames,filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".html"):
            filedata = open(os.path.join(root,filename))
            count_dict[os.path.join(root,filename)] = {}
            for k,v in rules_dict.items():
                count_dict[os.path.join(root,filename)][k] = {}
                for rule in v:
                    count_dict[os.path.join(root,filename)][k][rule] = 0
            for f in filedata:
                for key,value in rules_dict.items():
                    for v in value:
                        if v == '<label':
                            if v in f:
                                count_dict[os.path.join(root,filename)][key][v] += 1
            soup = BeautifulSoup(filedata,"html.parser")
            lst = [node['class'] for node in soup.find_all() if node.has_attr('class')]
            ruleList = list(itertools.chain.from_iterable(lst))
            for key,value in rules_dict.items():
                    for v in value:
                        if v in ruleList:
                            count_dict[os.path.join(root,filename)][key][v] = ruleList.count(v)

logging.debug(pformat(count_dict))
                             




import os
import logging 
from pprint import *
from bs4 import BeautifulSoup
import itertools
# logging.basicConfig(filename="/home/spaneos/Desktop/BOOTSTRP_3/share/not_completed/common/31NC_prospect-student-report.log", 
#                     format='%(asctime)s %(message)s %(levelname)s', 
#                     filemode='w',
#                     level='DEBUG')  
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
20:['label'],
21:['glyphicon glyphicon'],
22:['page-header'],
24:['in'],
25:['panel-default'],
26:['panel-group'],
31:['breadcrumb'],
32:['item']
}
filelist = []
directory = '/home/spaneos/Desktop/STAGING_BOOTSTRAP_UPGRADE/dhi-angular/src/app/prospect-student-report'
count_dict = {}
file_count = 0
total_changes = 0
for root,dirnames,filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".html"):
            pprint(filename)
              




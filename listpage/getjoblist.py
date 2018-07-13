from mdr import region_to_dict,Region
from dep import Depta
import os
import time

_url="https://www.aamccareers.org/job-search-results/"
d = Depta()
seeds = d.extract(url=_url)
if seeds is not None:
    result=None
    for seed in seeds:
        table = seed.as_html_table()
        if table is not None:
            result=table
            pass
        
        if result:
            print result
        

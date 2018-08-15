import os
import glob

cms_skin_ids = []

skins_to_cms = []
PATH = "../web-project/js/skins/"

os.chdir(PATH)

for filename in glob.glob('*.js'):
    with open(filename, 'r') as outfile:
        not_include = False
        is_gms = False
        for line in outfile:
            for i in cms_skin_ids:
                if "GmsPlatform:true" in line or "GmsPlatform: true" in line:
                    is_gms = True
                if 'site_id: '+'"'+str(i)+'"' in line:
                    not_include = True
        if not not_include:
            if is_gms:
                skins_to_cms.append(filename)


for j in skins_to_cms:
    if "terminal" and "betconstruct" not in j:
        print j
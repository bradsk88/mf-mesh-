import os
import subprocess

ftyps = []
mdats = []

offset = 0

for filename in os.listdir('.'):
    if filename.endswith("_mdat.mov"):
        mdats.append(filename)
        continue
    if filename.endswith("_ftyp.mov"):
        ftyps.append(filename)
        continue

reverse = False
if reverse:
    ftyps = reversed(ftyps[offset:])
    mdats = reversed(mdats)

ffounds = [
        'f0044032',
        'f0044288',
        'f0044800',
        'f0045312',
        'f0045568',
        'f0046080',
        'f0046592',
        'f0047104',
        'f0047872',
        'f0048384',
        'f0048640',
        'f0048896',
        'f0049408',
        'f0053760',
        'f0054272',
        'f0054528',
        'f0054784',
        'f0055296',
        'f0055552',
        'f0056320',
        'f0056576',
        'f0056832',
        'f0057344',
        'f0057600',
        'f0057856',
        'f0058112',
        'f0058368',
        'f0058624',
        'f0059136',
        'f0059648',
        'f0060160',
        'f0060928',
        'f0061184',
        'f0061952',
        'f0062464',
        'f0062976',
        'f0063232',
        'f0063744',
        'f0064512',
        'f0066048',
        ]
mfounds = [
        'f3506176',
        'f4685824',
        'f7176192',
        'f9535488',
        'f10584064',
        'f12812288',
        'f14516224',
        'f17399808',
        'f22249472',
        'f22511616',
        'f24739840',
        'f23560192',
        'f25526272',
        'f26181632',
        'f27361280',
        'f28409856',
        'f28803072',
        'f29982720',
        'f30900224',
        'f36274176',
        'f36536320',
        'f37060608',
        'f37715968',
        'f39813120',
        'f40206336',
        'f40468480',
        'f40861696',
        'f41517056',
        'f42827776',
        'f46366720',
        'f47415296',
        'f52920320',
        'f53051392',
        'f56590336',
        'f58163200',
        'f60653568',
        'f60784640',
        'f62750720',
        'f65372160',
        'f68780032',
        ]

fskips = 50
mskips = 27

with open('bashfile', 'w') as outfile:
    for i, f in enumerate(ftyps[fskips:]):
        f_name = f.split('_')[0]
        if f_name in ffounds:
            print("Already found {} skipping".format(f_name))
            continue
        for j, m in enumerate(mdats[mskips:]):  # Already got working copies of the first to mdats
            m_name = m.split('_')[0]
            if m_name in mfounds:
                print("Already found M {} skipping".format(m_name))
                continue
            output_name = '{}_{}_{}_{}.mov'.format(i+fskips, j+mskips, f_name, m_name)
            if reverse:
                output_name = 'test{}_{}_r.mov'.format(offset, i)
            outfile.write("echo -e \"Creating {} from {} and {}\"\n".format(output_name, f, m))
            command = 'cat {} {} > output/{}'.format(f, m, output_name)
            outfile.write(command)
            outfile.write('\n')
	    command = 'ffmpeg -i output/{} -vf "select=eq(n\,0)" -q:v 3 output/{}.jpg'.format(output_name)
	    outfile.write(command)
	    outfile.write('\n')

count = 0
for i in range(53):
    for i in range(53):
        count = count + 1
print(count)

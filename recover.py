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
        ]
mfounds = [
        ]

fskips = 0
mskips = 0

with open('bashfile', 'w') as outfile:
    for i, f in enumerate(ftyps[fskips:]):
        f_name = f.split('_')[0]
        if f_name in ffounds:
            print("Already found {} skipping".format(f_name))
            continue
        for j, m in enumerate(mdats[mskips:]):  # Already got working copies of the first N mdats
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

            command = """
if ffmpeg -loglevel panic -y -i "output/{0}" -f image2 -ss 10 -vframes 1 -an "output/{0}.jpg" ; then
    echo "Possible Success"
else 
    echo "Detected failure.  Removing {0}";
    rm output/{0}
fi
            """
            outfile.write(command.format(output_name))
            outfile.write('\n')

count = 0
for i in range(53):
    for i in range(53):
        count = count + 1
print(count)

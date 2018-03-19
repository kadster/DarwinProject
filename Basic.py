import os
from bs4 import BeautifulSoup

folder = '/Users/nt/Desktop/Darwin'
files = os.listdir(folder)
tagnames = ['date']

files = [f for f in files[:] if 'xml' in f]

output_strs = []

for fname in files:
    with open(os.path.join(folder, fname), "r") as infile:
        file_data = []
        content = infile.read()
        soup = BeautifulSoup(content,'xml')

        for tagname in tagnames:
            tag_data = soup.find(tagname)
            if tag_data is None:
                tag_text="MISSING"
            else:
                transcription = soup.find(type="transcription")
                temp = tag_data.get_text()
                if transcription is not None:
                    tag_text = transcription.get_text()
                else:
                    tag_text = tag_data.get_text()
                    if tag_text is not soup.find(type="transcription"):
                        tag_text="TRANSCRIPTION MISSING"

            file_data.append(',\"' + tag_text + '\"')

        output_strs.append("{}\t{}\n".format(fname, "\t".join(file_data).replace('\n', ' ')))


print(len(output_strs))
with open('/Users/nt/Desktop/transcription.csv', 'w+') as outfile:
    outfile.writelines(output_strs)

#
#  Covert PDF into text files
#
import os
import sys
import utils


def main(argv):
    pdf_dir = './pdf/'
    txt_dir = './txt/'

    for file in os.listdir(pdf_dir):
        if file.lower().endswith('.pdf'):
            file_prefix = file[:-4]
            pdf_path = pdf_dir + file_prefix + '.pdf'
            text_path = txt_dir + file_prefix + '.txt'

            print('Processing', file, ':')
            print('- Coverting PDF to text and images...')
            cmd = 'node extract_text.js ' + pdf_path + ' ' + text_path
            os.system(cmd)


if __name__ == '__main__':
    main(sys.argv)

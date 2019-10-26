#
#  Process all PDF in dir
#
import os
import sys
import utils


def main(argv):
    txt_dir = './txt/'
    keywords_file = './keywords.txt'

    '''
        keywords: list of all keywords set in txt
        stat_sig: statistic for every single file
        stat_all: statistic for all keywords
        stat_clf: statistic for keywords classified into two
    '''
    keywords = []
    stat_all = {}
    stat_sig = {}
    stat_clf = {}

    with open(keywords_file, encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            line = line.strip().split()
            keywords += line

    SPLIT = keywords.index('新')

    for file in os.listdir(txt_dir):
        if file.lower().endswith('.txt'):
            file_prefix = file[:-4]
            company_id = file_prefix[:6]
            file_path = txt_dir + file

            print('Processing', file, ':')
            print('- Count keywords in text...')

            stat = utils.AnalyzeText(file_path, keywords)

            stat_sig[file_prefix] = stat

            if(company_id in stat_all):
                stat_all[company_id] = utils.MergeDict(stat_all[company_id], stat)
            else:
                stat_all[company_id] = stat

            
            '''
            pic_dir = file_prefix + '_pic'
            utils.mkdir(pic_dir)
            cmd = 'python extract_image.py ' + file_full_path + ' ' + pic_dir
            os.system(cmd)
            print('- Count keywords in images ...')
            '''

            print('--- DONE')

    '''
        Merge keywords for each feature
    '''
    for (k, v) in stat_all.items():
        valueE = 0
        valueN = 0
        for i in range(0, SPLIT): valueE += v[keywords[i]]
        for i in range(SPLIT, len(keywords)): valueN += v[keywords[i]]
        stat_clf[k] = {'Efficiency': valueE, 'Novelty': valueN}

    utils.StatWriter('company_single_pdf.xls', keywords, stat_sig)
    utils.StatWriter('company_keywords.xls', keywords, stat_all)
    utils.StatWriter('company_features.xls', ['Efficiency', 'Novelty'], stat_clf)


if __name__ == '__main__':
    main(sys.argv)

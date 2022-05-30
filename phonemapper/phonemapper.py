import csv
import string
import json
import itertools

def load_map(map_file):
    return json.load(open (map_file, 'r'))
    
def map_phoneme(mapping, phoneme):
    try:
        return mapping[phoneme]
    except:
        return '<UNK>'

def read_in_data(in_file):
    return next(itertools.islice(csv.reader(open(in_file, 'r')), 0, None))

def write_to_csv(open_file, line):
    open_file.write(line)

def invert_mapping(map_dict):
    return {value:key for key, value in map_dict.items()}

def map_row(mapping, row, missing_phonemes):
    word = row[0]
    ipa = row[1].translate(str.maketrans('', '', string.punctuation))
    before_after = [[phoneme, map_phoneme(mapping, phoneme)] for phoneme in ipa]
    missing_phonemes = missing_phonemes.union({item[0] for item in before_after if item[1]=='<UNK>'})
    mapped= ' '.join([item[1] for item in before_after])
    return word, ipa, mapped, missing_phonemes

def main():
    map_file = 'cmu_to_ipa.json'
    cmu_to_ipa_map = load_map(map_file)
    in_file = 'alessia.csv'
    data = read_in_data(in_file)
    out_file = 'alessia_with_cmu.csv'
    global ipa_to_cmu_map
    ipa_to_cmu_map = invert_mapping(cmu_to_ipa_map)
    missing_phonemes = set()
    with open(out_file, 'w+') as o:
        for row in data:
            word, ipa, cmu, missing_phonemes = map_row(ipa_to_cmu_map, row, missing_phonemes)
            write_to_csv(o, f'{word}, {ipa}, {cmu}\n')
            
if __name__ == '__main__':
    main()

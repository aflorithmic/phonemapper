import csv
import string
import json
import itertools

# this mapping is only useful as a helper for manual transcribing. since CMU tokens map to multiple IPA phones, ambiguous ones are 

def load_map(map_file):
        return json.load(open (map_file, 'r'))
    
def map_phoneme(map, phoneme):
    return map[phoneme]

def read_in_data(in_file):
    return next(itertools.islice(csv.reader(open(in_file, 'r')), 0, None))

def write_to_csv(open_file, line):
    open_file.write(line)

def catch_except(func, *args, handle=lambda e : '<UNK>', **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # print(args[0][-1])
        # if __name__ == "__main__":
        missing_phonemes.add(args[0][-1])
        return handle(e)

def invert_mapping(map_dict):
    return {value:key for key, value in map_dict.items()}

def map_row(map, row):
    word = row[0]
    ipa = row[1].translate(str.maketrans('', '', string.punctuation))
    return word, ipa, ' '.join([catch_except(map_phoneme, (map, phoneme)) for phoneme in ipa])

def main():
    # with open ('cmu_to_ipa.json', 'r') as open_map:
    map_file = 'cmu_to_ipa.json'
    cmu_to_ipa_map = load_map(map_file)
    in_file = 'alessia.csv'
    data = read_in_data(in_file)
    out_file = 'alessia_with_cmu.csv'
    global ipa_to_cmu_map
    ipa_to_cmu_map = invert_mapping(cmu_to_ipa_map)
    global missing_phonemes
    missing_phonemes = set()
    with open(out_file, 'w+') as o:
        for row in data:
            word, ipa, cmu = map_row(ipa_to_cmu_map, row)
            write_to_csv(o, f'{word}, {ipa}, {cmu}\n')
    # print(missing_phonemes)
if __name__ == '__main__':
    main()


    # change dictionary to ipa-to-cmu to remove ambiguities
    # read in IPA to CMU mapping from separate file
    # add CMU to IPA mapping functionality



    # testing
    # write tests in this file first - to start of main()
    # add -test mode 
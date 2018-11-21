import copy
import json
import os

from tokenizer_tools.tagset.NER.IOB import IobSequenceEncoderDecoder

decoder = IobSequenceEncoderDecoder()

DATA_DIR = "data/raw_data/ms-cntk-atis"

import pickle

print(os.listdir(DATA_DIR))


def load_ds(fname='atis.train.pkl'):
    with open(fname, 'rb') as stream:
        ds, dicts = pickle.load(stream)
    print('Done  loading: ', fname)
    print('      samples: {:4d}'.format(len(ds['query'])))
    print('   vocab_size: {:4d}'.format(len(dicts['token_ids'])))
    print('   slot count: {:4d}'.format(len(dicts['slot_ids'])))
    print(' intent count: {:4d}'.format(len(dicts['intent_ids'])))
    return ds, dicts


train_ds, dicts = load_ds(os.path.join(DATA_DIR, 'atis.train.pkl'))
test_ds, dicts = load_ds(os.path.join(DATA_DIR, 'atis.test.pkl'))

t2i, s2i, in2i = map(dicts.get, ['token_ids', 'slot_ids', 'intent_ids'])
i2t, i2s, i2in = map(lambda d: {d[k]: k for k in d.keys()}, [t2i, s2i, in2i])
query, slots, intent = map(train_ds.get,
                           ['query', 'slot_labels', 'intent_labels'])

for i in range(5):
    print('{:4d}:{:>15}: {}'.format(i, i2in[intent[i][0]],
                                    ' '.join(map(i2t.get, query[i]))))
    for j in range(len(query[i])):
        print('{:>33} {:>40}'.format(i2t[query[i][j]],
                                     i2s[slots[i][j]]))
    print('*' * 74)


def to_rasa_nlu_format(query, slots, intent, output_file):
    tpl = {
        "rasa_nlu_data": {
            "common_examples": [],
            "regex_features": [],
            "lookup_tables": [],
            "entity_synonyms": []
        }
    }

    example_tpl = {
        "text": "",
        "intent": "",
        "entities": []
    }

    entity_tpl = {
        "start": 0,
        "end": 0,
        "value": "",
        "entity": ""
    }

    data = copy.deepcopy(tpl)

    data_len = len(query)

    for i in range(data_len):
        example = copy.deepcopy(example_tpl)
        text_msg = ''.join(map(i2t.get, query[i]))

        raw_query_text_list = query[i]
        query_text_list = raw_query_text_list[1: -1]  # remove BOS and EOS tag

        example['text'] = ' '.join(map(i2t.get, query_text_list))
        example['intent'] = i2in[intent[i][0]]

        tag_seq = [i2s[j] for j in slots[i]]

        offset_list = decoder.decode_to_offset(tag_seq)
        print(offset_list)

        entities_list = []

        for offset in offset_list:
            entity = copy.deepcopy(entity_tpl)
            entity['start'] = len(' '.join(map(i2t.get, raw_query_text_list[1: offset[0]]))) + 1
            entity['end'] = len(' '.join(map(i2t.get, raw_query_text_list[offset[0]: offset[1]]))) + entity['start']
            entity['value'] = ' '.join(map(i2t.get, raw_query_text_list[offset[0]: offset[1]]))
            entity['entity'] = offset[2]

            entities_list.append(entity)

        example['entities'] = entities_list

        data['rasa_nlu_data']['common_examples'].append(example)

    with open(output_file, 'wt') as fd:
        json.dump(data, fd, ensure_ascii=False, indent=4)


to_rasa_nlu_format(query, slots, intent, 'train.json')

query, slots, intent = map(test_ds.get,
                           ['query', 'slot_labels', 'intent_labels'])
to_rasa_nlu_format(query, slots, intent, 'test.json')

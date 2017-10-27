import numpy
import os

from sem_relatd import load_and_predict


if __name__ == '__main__':
    model_name = '../../best_models/sem839.npz'
    print 'in main ..'
    load_and_predict(
    load_from=model_name,
    n_words= 2260,
    valid_batch_size = 32,
    test_datasets    = ['../../data/word_sequence/premise_SICK_test_annotated.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_test_annotated.txt.tok',
                        '../../data/sem_relatd/scores_SICK_test_annotated.txt'],
    dictionary       = '../../data/word_sequence/vocab_cased.pkl',
    embedding        = '../../data/glove.840B.300d.txt',
    output_file      = 'results/taskb.txt'

    )

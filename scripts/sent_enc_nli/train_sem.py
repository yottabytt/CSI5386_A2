import numpy
import os

from sem_relatd import train

if __name__ == '__main__':
    model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    train(
    saveto           = 'models/sem_rel7.npz',
    reload_          = False,
    dim_word         = 300,
    dim              = 300,
    max_epochs       = 300,
    patience         = 6,
    n_words          = 2260,
    decay_c          = 0.,
    clip_c           = 10.,
    lrate            = 0.0002,
    optimizer        = 'adadelta',
    maxlen           = 100,
    batch_size       = 32,
    valid_batch_size = 32,
    dispFreq         = 10,
    validFreq        = 1000,
    saveFreq         = 1000,
    use_dropout      = True,
    verbose          = False,
    datasets         = ['../../data/word_sequence/premise_SICK_train.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_train.txt.tok',
                        '../../data/sem_relatd/scores_SICK_train.txt'],
    valid_datasets   = ['../../data/word_sequence/premise_SICK_trial.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_trial.txt.tok',
                        '../../data/sem_relatd/scores_SICK_trial.txt'],
    test_datasets    = ['../../data/word_sequence/premise_SICK_test_annotated.txt.tok',
                        '../../data/word_sequence/hypothesis_SICK_test_annotated.txt.tok',
                        '../../data/sem_relatd/scores_SICK_test_annotated.txt'],
    dictionary       = '../../data/word_sequence/vocab_cased.pkl',
    embedding        = '../../data/glove.840B.300d.txt',
    )

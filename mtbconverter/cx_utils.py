"""Definition of constant variables in the CentraXX context."""

CV_PREFIX = 'QBIC_'

CV_EFFECT_SSNV = ['activating','inactivating','function_changed','probably_activating',
                    'probably_inactivating','probable_function_change','ambigious','benign','NA']

CV_BASES = ['C','A','T','G']

CV_CHROMOSOMES = list(range(1,24)) + ['X', 'Y']
import pytest
#import os

from utils import pad_sents

def test_alignment():
    sents = [['ciao'],['ciao','sono'],['ciao','sono','luca'],['sono','luca']]
    pad_token = 'BAM'
    
    expected_output = [['ciao','BAM','BAM'],['ciao','sono','BAM'],['ciao','sono','luca'],['sono','luca','BAM']]
    
    assert pad_sents(sents,pad_token) == expected_output, 'Something went wrong'

# -*- coding: UTF-8 -*-

from memegenerator.lib import the_called_function
import pytest

def cat_tester():
    assert the_called_function() == 'this is your meme cat'

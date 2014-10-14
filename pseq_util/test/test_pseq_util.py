from __future__ import print_function
import unittest
try:
    unittest.skip
except AttributeError:
    import unittest2 as unitest

import os
import doctest

import pseq_util
from pseq_util import *
from pseq_util.phenotypes_snpmax  import *

suite = doctest.DocTestSuite(pseq_util)


def fh(fname, mode='rt'):
    return open(os.path.join(os.path.dirname(__file__), fname), mode)

class TestPhenotypes(unittest.TestCase):

    def setUp(self):
        self.p = phenotype.Phenotype("test","test","Float","test")

    def test_create_pheno(self):
        assert self.p.get_type == "Float"
        assert self.p.get_name == "test"
        assert self.p.get_description == "test"
        assert self.p.get_missing_code == "test"

    def test_add_sample(self):
        self.p.add_data('1','1.0')
        res = self.p.get_data('1')
        assert res == '1.0'
    
    def test_print_header(self):
        header = self.p.get_header()
        assert header == '##test,Float,test,"test"\n'

class TestSnpMaxConverter(unitest.TestCase):

    def test_is_number(self):
        assert phenotypes_snpmax.is_number(1.0) == True
        assert phenotypes_snpmax.is_number(1) == True
        assert phenotypes_snpmax.is_int(1) == True
        assert phenotypes_snpmax.is_int('blah') == False

    def test_is_int(self):
        assert phenotypes_snpmax.is_int(0.8) == False
        assert phenotypes_snpmax.is_int(1) == True
        assert phenotypes_snpmax.is_int(3.0) == True
        assert phenotypes_snpmax.is_int('blah') == False

    def test_sniff_datatype(self):
        phenotypes_snpmax.sniff_datatype([1.0,1.0,1.0],'') == 'Integer'
        phenotypes_snpmax.sniff_datatype([1,1,1,0],0,)  == 'Integer'
        phenotypes_snpmax.sniff_datatype(["blah",1,1,1],'') == 'String'
        phenotypes_snpmax.sniff_datatype(['1.0','1.5',' '],' ') == "Float"

    def test_parse_phenotypes(self):
        input_phenotypes = os.path.join(os.path.dirname(__file__),'test_data/test_phenotypes.txt') 
        output_phenotypes= os.path.join(os.path.dirname(__file__),'test_data/out.txt')
        missing = ' '
        delim = '\t'
        phenotypes_snpmax.parse_phenotypes(input_phenotypes,output_phenotypes,missing,delim)
        with open(output_phenotypes) as out:
            for i, line in enumerate(out):
                if ( i==1 ):
                    assert line == '##FLOAT2,Float,.,"1"\n'
        os.remove(output_phenotypes)

suite.addTests(unitest.TestLoader().loadTestsFromTestCase(TestPhenotypes))
suite.addTests(unitest.TestLoader().loadTestsFromTestCase(TestSnpMaxConverter))

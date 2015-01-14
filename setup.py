from setuptools import setup, find_packages
setup(
    name = "pseq_util",
    version = "0.1",
    packages =['pseq_util','pseq_util.test'],
    test_suite='pseq_util.test.test_pseq_util',
    author="James Boocock",
    author_email="james.boocock@otago.ac.nz",
    description="Plink/SEQ utilities",
    entry_points = {
        'console_scripts' : [
            'snpmax_to_pseq = pseq_util.phenotypes_snpmax:main',
            'cadd_to_vcf = pseq_util.cadd_to_vcf:main',
            'bed_to_varset = pseq_util.bed_to_varset:main'
            ]
        },
    url="https://github.com/smilefreak/pseq_utilities",
)


    

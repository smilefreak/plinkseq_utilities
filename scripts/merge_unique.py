import argparse
import pandas
import sys

phenotypes = {}

def merge_phenotypes(sample_name, pheno_information,gout_header, diabetes_header):
    """ 
        Merges using the diabetes dat, eg. l_split [1:], which is the the diabetes dataset we are using.

    """
    try: 
        temp_row = phenotypes[sample_name]
    except KeyError:
        phenotypes[sample_name] = [' ' for i in range(len(gout_header))]
    for i, new in enumerate(diabetes_header):
        try:
            index = gout_header.index(new)
            #print(i)
            #print(pheno_information)
            #print(new)
            #print(index)
            #print(len(pheno_information))
            #print(phenotypes[sample_name])
            #print(len(diabetes_header))
            #print(diabetes_header)
            phenotypes[sample_name][index] = pheno_information[i]
        except ValueError:
            continue
            #sys.stderr.write(new + ' does not exist\n')

def update_diabetes_info(diabetes, gout_header):
    """
        Update diabetes information
    """
    with open(diabetes) as f:
        d_header = []
        for i, line in enumerate(f):
            line = line.replace('\n','')
            l_split = line.split('\t')
            if ( i == 0 ):
                d_header = l_split[1:]
            else:
                samp_name = l_split[0]
                merge_phenotypes(samp_name, l_split[1:], gout_header, d_header)
    return(d_header)

def phenotype_information(gout_input):
    """
        add_phenotype_information for new samples
    """
    with open(gout_input) as f:
        phenotype_header = []  
        for i, line in enumerate(f):
            line = line.replace('\n','')
            l_split = line.split('\t')
            if ( i == 0 ):
                phenotype_header = l_split[1:]
            else:
                samp_name = l_split[0]
                phenotypes[samp_name] = l_split[1:]
    return(phenotype_header)

def print_phenotypes(header):
    print('PATIENT'+'\t'+'\t'.join(header))
    for key, value in phenotypes.items():
        print(key +'\t' +'\t'.join(value))


def main():
    parser = argparse.ArgumentParser(description="Get Unique columns")
    parser.add_argument('-g','--gout',dest='gout')
    parser.add_argument('-d','--diabetes',dest='diabetes')
    args = parser.parse_args()
    header = phenotype_information(args.gout)
    update_diabetes_info(args.diabetes, header)
    print_phenotypes(header)

if __name__=="__main__":
    main()

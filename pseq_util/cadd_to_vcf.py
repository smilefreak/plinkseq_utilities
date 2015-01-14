# CADD to VCF
import gzip
import argparse
vcf_header="""##fileformat=VCFv4.1
##INFO=<ID=RC,Number=1,Type=Float,Description="Raw CADD scores"
##INFO=<ID=PC,Number=1,Type=Float,Description="Phread CADD scores"
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"""
def cadd_to_vcf(cadd_file):
    print(vcf_header)
    with gzip.open(cadd_file) as f:
        for line in f:
            if "#" in line:
                continue
            line = line.strip().split()
            chrom = line[0]
            pos = line[1]
            ref = line[2]
            alt = line[3]
            raw_score = line[4]
            p_score = line[5]
            info_column='RC='+raw_score+';PC='+p_score
            print('\t'.join([chrom,pos,'.',ref,alt,'100','PASS',info_column]))

def main():
    parser = argparse.ArgumentParser(description="CADD to VCF")
    parser.add_argument(dest='cadd_file')
    args = parser.parse_args()
    cadd_to_vcf(args.cadd_file)

if __name__=="__main__":
    main()

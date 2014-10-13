class Phenotype:
    """
        Class represents a phenotype for using PLINK/SEQ
        
        For each phenotype you add.

        Format description given at 
        https://atgu.mgh.harvard.edu/plinkseq/input.shtml
    """
    def __init__(self, name, description,type,missing):
        self.name = name
        self.type = type
        self.description = description
        self.missing = missing
        self.ids = {}

    def add_data(self,sample,value):
        self.ids[sample] = value

    def get_header(self)
        s = "##"
        s += name + ","
        s += missing +","
        s += "\"" + description +"\""
        return(s)

    

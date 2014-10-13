class Phenotype:
    """
        Class represents a phenotype for using PLINK/SEQ
        
        For each phenotype you add.

        Format description given at 
        https://atgu.mgh.harvard.edu/plinkseq/input.shtml
    """
    def __init__(self, name, description,type,missing):
        self._name = name
        self._type = type
        self._description = description
        self._missing = missing
        self._ids = {}

    def add_data(self,sample,value):
        self._ids[sample] = value

    def get_id(self,sample)
        return(self._ids[sample])
    
    def get_header(self)
        s = "##"
        s += self._name + ","
        s += self._missing +","
        s += "\"" + self._description +"\"" + "\n"
        return(s)

    

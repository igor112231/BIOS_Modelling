from modeller import *
from modeller.automodel import *

def main():
    env = Environ()
    a = AutoModel(env, alnfile = './Preprocessing_Data/MSA_Alignment.txt',
    knowns = ('3J4Q_D', '6F14_A', '6Y05_A', '1CTP_E'), sequence = 'cAMP_kinase')
    a.starting_model = 1
    a.ending_model = 5
    a.make()
    a.write('Final_Model', format ='PDB')


if __name__ == '__main__':
    main()
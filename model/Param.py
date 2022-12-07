DATANAME = 'PEMS04'
TIMESTEP_IN = 12
TIMESTEP_OUT = 12

DATASETNAMELIST = ['PEMS03', 'PEMS04', 'PEMS07', 'PEMS08']
N_NODELIST = [358, 307, 883, 170]
CHANNELLIST = [1, 3, 1, 3]
FLOWPATHLIST = ['../data/PEMS03.npz', '../data/PEMS04.npz', '../data/PEMS07.npz', '../data/PEMS08.npz']
ADJPATHLIST = ['../data/PEMS03.csv','../data/PEMS04ADJ.csv','../data/PEMS07ADJ.csv','../data/PEMS08ADJ.csv']


BATCHSIZE = 64
LEARN = 0.001
EPOCH = 200
PATIENCE = 10
OPTIMIZER = 'Adam'
# OPTIMIZER = 'RMSprop'
# LOSS = 'MSE'
LOSS = 'MaskMAE'
TRAINRATIO = 0.8  # TRAIN + VAL
TRAINVALSPLIT = 0.25  # val_ratio = 0.8 * 0.125 = 0.1

DATASETCHOOSE = 0
N_NODE = N_NODELIST[DATASETCHOOSE]
CHANNEL = CHANNELLIST[DATASETCHOOSE]
FLOWPATH = FLOWPATHLIST[DATASETCHOOSE]
ADJPATH = ADJPATHLIST[DATASETCHOOSE]

CHANNEL = 1
OUT_CHANNEL = 1

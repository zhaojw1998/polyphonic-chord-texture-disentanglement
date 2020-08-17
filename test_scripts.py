import numpy as np
data=np.load('D:/Computer Music Research/polyphonic-chord-texture-disentanglement/data/POP09-PIANOROLL-4-bin-quantization/001.npz')
beat = data['beat']
chord = data['chord']
melody = data['melody']
bridge = data['bridge']
piano = data['piano']
print(bridge[:12, :])

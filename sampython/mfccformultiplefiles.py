#!/usr/bin/env python
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
#note scipy numpy anf python_speech_features must be installed using pip
#wav.read reads the wav file 
#to change the mfcc samplerate and other stuff do
#python def mfcc(signal,samplerate=16000,winlen=0.025,winstep=0.01,numcep=13,nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97,ceplifter=22,appendEnergy=True)
#where the columns are
#Parameter		Description
#signal			the audio signal from which to compute features. Should be an N*1 array
#samplerate		the samplerate of the signal we are working with.
#winlen			the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
#winstep			the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
#numcep			the number of cepstrum to return, default 13
#nfilt			the number of filters in the filterbank, default 26.
#nfft			the FFT size. Default is 512
#lowfreq			lowest band edge of mel filters. In Hz, default is 0
#highfreq		highest band edge of mel filters. In Hz, default is samplerate/2
#preemph			apply preemphasis filter with preemph as coefficient. 0 is no filter. Default is 0.97
#ceplifter		apply a lifter to final cepstral coefficients. 0 is no lifter. Default is 22
#appendEnergy	if this is true, the zeroth cepstral coefficient is replaced with the log of the total frame energy.
#returns			A numpy array of size (NUMFRAMES by numcep) containing features. Each row holds 1 feature vector.
j=1
for i in xrange(1,91):
	(rate,sig) = wav.read("/home/samim/audiotrainingset/training/n%d.wav"%i)
	#to generate the mfcc
	mfcc_feat = mfcc(sig,rate)
	np.savetxt('/home/samim/train%d.txt'%j,mfcc_feat)
	j=j+1
#for i in xrange(101,111):
#	(rate,sig) = wav.read("/home/samim/audiotrainingset/training/n%d.wav"%i)
	#to generate the mfcc
#	mfcc_feat = mfcc(sig,rate)
#	np.savetxt('/home/samim/test%d.txt'%j,mfcc_feat)
#	j=j+1
j=1
for i in xrange(1,68):
	(rate,sig) = wav.read("/home/samim/audiotrainingset/training/sp%d.wav"%i)
	#to generate the mfcc
	mfcc_feat = mfcc(sig,rate)
	np.savetxt('/home/samim/train1%d.txt'%j,mfcc_feat)
	j=j+1
# HAR classification 
# Author: Burak Himmetoglu
# 8/15/2017

import pandas as pd 
import numpy as np
import os
import tqdm

def read_data(data_path, split = "train"):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 2000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata_" + split + ".csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_t_" + split + ".csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_p(data_path, split = "train"):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 1000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata_" + split + ".csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_p_" + split + ".csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_all(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 2000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_t.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_all_p(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 1000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_p.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_all2(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 2000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results2")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_t.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_all2_p(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 1000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results2")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	bands = ['u', 'g', 'r', 'i', 'z', 'y']
	
	channel_files = []
	
	for band in bands:
		channel_files.append(os.path.join(path_signals, band + "_band_p.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[:,:,i_ch] = dat_.as_matrix()

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_old(data_path, split = "train"):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 1000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata_" + split + ".csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	channel_files = []
	
	for obj in objid.tolist():
		channel_files.append(os.path.join(path_signals, "int_" + str(obj) + "_p.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[i_ch,:,:] = dat_.as_matrix().T

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_full(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 2000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results2")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	channel_files = []
	
	for obj in objid.tolist():
		channel_files.append(os.path.join(path_signals, "int_" + str(obj) + "_t.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[i_ch,:,:] = dat_.as_matrix().T

		# iterate
		i_ch += 1

	# Return 
	return X, labels
	
def read_data_full_p(data_path):
	""" Read data """

	# Fixed params
	n_class = 14
	n_steps = 1000
	n_channels = 6

	# Paths
	path_ = os.path.join(data_path)
	path_signals = os.path.join("F:\\Documents\\Kaggle\\Results2")

	# Read labels and one-hot encode
	metadata_path = os.path.join(path_, "training_set_metadata.csv")
	metadata = pd.read_csv(metadata_path, header = None)

	# Read time-series data
	
	#channel_files.sort()
	#n_channels = len(channel_files)
	#posix = len(split) + 5
	labels = metadata.iloc[:,11]
	objid = metadata.iloc[:,0]
	
	channel_files = []
	
	for obj in objid.tolist():
		channel_files.append(os.path.join(path_signals, "int_" + str(obj) + "_p.csv"))	

	# Initiate array
	X = np.zeros((len(labels), n_steps, n_channels))
	i_ch = 0
	for fil_ch in tqdm.tqdm(channel_files):
		dat_ = pd.read_csv(fil_ch, delim_whitespace = False, header = None)
		X[i_ch,:,:] = dat_.as_matrix().T

		# iterate
		i_ch += 1

	# Return 
	return X, labels

def standardize(train, test):
	""" Standardize data """

	# Standardize train and test
	X_train = (train - np.mean(train, axis=0)[None,:,:]) / np.std(train, axis=0)[None,:,:]
	X_test = (test - np.mean(test, axis=0)[None,:,:]) / np.std(test, axis=0)[None,:,:]

	return X_train, X_test
	
def standardize_full(data):
	""" Standardize data """

	# Standardize train and test
	X = (data - np.mean(data, axis=0)[None,:,:]) / np.std(data, axis=0)[None,:,:]

	return X
	
def standardize_feats(train, test):
	""" Standardize data """

	# Standardize train and test
	X_train = (train - np.mean(train, axis=0)) / np.std(train, axis=0)
	X_test = (test - np.mean(test, axis=0)) / np.std(test, axis=0)

	return X_train, X_test
	
def standardize_feats_full(data):
	""" Standardize data """

	# Standardize train and test
	X = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

	return X

def one_hot(labels, n_class = 14):
	""" One-hot encoding """
	expansion = np.eye(n_class)
	y = expansion[:, labels-1].T
	assert y.shape[1] == n_class, "Wrong number of labels!"

	return y

def get_batches(X, y, X_f, X_p, batch_size = 100):
	""" Return a generator for batches """
	n_batches = len(X) // batch_size
	X, y, X_f, X_p = X[:n_batches*batch_size], y[:n_batches*batch_size], X_f[:n_batches*batch_size], X_p[:n_batches*batch_size]

	# Loop over batches and yield
	for b in range(0, len(X), batch_size):
		yield X[b:b+batch_size], y[b:b+batch_size], X_f[b:b+batch_size], X_p[b:b+batch_size]
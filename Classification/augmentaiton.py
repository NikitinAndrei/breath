
import librosa
import librosa.display
import pandas as pd
import soundfile as sf
import warnings
import os
warnings.filterwarnings('ignore')

# Read Data
data = pd.read_csv('C:/Users/Andreuff/OMG1.csv')
valid_data = data[['filename','ClassID', 'Class']]
valid_data['path'] =  valid_data['Class'].astype('str') + '/' + valid_data['filename'].astype('str')
path_to = r'C:/Users/Andreuff/wavfiles/'


def vary_speed(rate, DataSet = 'DataSet_test'):
    """ Изменение скорости """
    data_path = 'C:/Users/Andreuff/' + DataSet + '.csv'
    data = pd.read_csv(data_path)
    valid_data = data[['filename','ClassID', 'Class']]
    valid_data['path'] =  valid_data['Class'].astype('str') + '/' + valid_data['filename'].astype('str')
    path_to = r'C:/Users/Andreuff/wavfiles/'
    str_rate = str(rate)
    newpath = path_to + 'Augmented/'
    for row in valid_data.itertuples():
        if not os.path.exists(newpath + row.Class):
            os.makedirs(newpath + row.Class)
        y, sr = librosa.load(path_to + row.path)  
        y_changed = librosa.effects.time_stretch(y, rate=rate)
        sf.write(newpath + row.Class + '/' + 'speed_' + str_rate + '_' + row.filename,y_changed, sr)


def vary_pitch(step, DataSet = 'DataSet_test'):
    """Изменение тональности по полутонам"""
    data_path = 'C:/Users/Andreuff/' + DataSet + '.csv'
    data = pd.read_csv(data_path)
    valid_data = data[['filename','ClassID', 'Class']]
    valid_data['path'] =  valid_data['Class'].astype('str') + '/' + valid_data['filename'].astype('str')
    path_to = r'C:/Users/Andreuff/wavfiles/'
    str_step = str(step)
    newpath = path_to + 'Augmented/'
    for row in valid_data.itertuples():
        if not os.path.exists(newpath + row.Class):
            os.makedirs(newpath + row.Class)
        y, sr = librosa.load(path_to + row.path)  
        y_changed = librosa.effects.pitch_shift(y, sr, n_steps=step)
        sf.write(newpath + row.Class + '/' + 'pitch_' + str_step + '_' + row.filename,y_changed, sr)


def vary_noise(step, rate=1):
    path_1 = 'C:/Users/Andreuff/wavfiles_old/'
    
    _files = os.listdir(path_1)

    for j in (_files):
        path = path_1 + j + '/' 
        files = os.listdir(path)
        for i in range(len(files)):
            y,sr = librosa.load(path + files[i])
            if rate == 1:
                y_c = librosa.effects.pitch_shift(y, sr, n_steps=step)
                n_n = path + str(files[i][:-4]) + '_' + str(step) + '.wav'
            else:
                y_c = librosa.effects.pitch_shift(y, sr, n_steps=step)
                y_c = librosa.effects.time_stretch(y_c, rate=rate)
                n_n = path + str(files[i][:-4]) + '_pitch_' + str(step) + '_speed_' + str(rate) + '.wav'
            sf.write(n_n, y_c, sr)
# vary_speed(1.2,'OMG2')

vary_noise(-5, 1)




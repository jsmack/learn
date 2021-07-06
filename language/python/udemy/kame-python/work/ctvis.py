import pandas as pd
from glob import glob
import numpy as np
import nibabel as nib

# _をつけるとprivate functiontとして定義するが呼ぶことはできる
# from ctvis import * だと_から始まるfunctionは呼ばれない

def _get_df4(base_path='public_covid_data', folder='rp_im'):
    data_dict = pd.DataFrame({'FilePath': glob(f'{base_path}/{folder}/*'),
                              'FileName': [x.split('/')[-1] for x in glob(f'{base_path}/{folder}/*')]})
    return data_dict

def get_df_all3(base_path='public_covid_data'):
    rp_im_df = _get_df4(base_path, folder='rp_im')
    rp_msk_df = _get_df4(base_path, folder='rp_msk')
    return rp_im_df.merge(rp_msk_df, on='FileName', suffixes=('Image', 'Mask'))


def load_nifti(path):
    #　nibでロード
    nifti = nib.load(path)
    
    # 画像配列にアクセスするため
    data = nifti.get_fdata()
    
    # 配列の回転
    data_rolled =  np.rollaxis(data, axis=1, start=0)
    return data_rolled
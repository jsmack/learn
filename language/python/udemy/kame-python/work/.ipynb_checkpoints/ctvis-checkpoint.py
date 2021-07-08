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


def label_color(mask_volume, 
               gg_color=[255,0,0],
               consolidation_color=[0, 255, 0],
               effusion_color=[0, 0, 255]):
    
    shp = mask_volume.shape
    # 箱の作成
    mask_color = np.zeros((shp[0], shp[1], shp[2], 3), dtype=np.float32)

    # カラー作成
    ggo_color = [255, 0, 0]
    consolidation_color = [0, 255, 0]
    effusion_color = [0, 0, 255]

    # それぞれ色を指定
    mask_color[np.equal(mask_volume, 1 )] = ggo_color
    mask_color[np.equal(mask_volume, 2 )] = consolidation_color
    mask_color[np.equal(mask_volume, 3 )] = effusion_color
    
    return mask_color
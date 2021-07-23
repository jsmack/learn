import pandas as pd
from glob import glob
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

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

def hu_to_gray(volume):
    maxhu = np.max(volume)
    # 最小値を取得
    minhu = np.min(volume)
    # 数値を0-1に変換 0になったらinfinityになるのでmax関数で0なら10-3乗(０．００1)にする
    volume_rerange = (volume - minhu ) / max((maxhu - minhu), 1e-3)
    # 値 * 255にする
    volume_rerange = volume_rerange * 255

    # 3次元(RGB)するため、stackで追加する。axisの-1で最後に追加
    volume_rerange = np.stack([volume_rerange, volume_rerange, volume_rerange], axis=-1)
    
    return volume_rerange.astype(np.uint8)
    

def overlay(gray_volume, mask_volume, mask_color, alpha=0.3):
    mask_filter = np.greater(mask_volume, 0)
    mask_filter = np.stack([mask_filter, mask_filter, mask_filter], axis=-1)
    
    overlayed = np.where(mask_filter > 0,
                         ((1 - alpha) * gray_volume + alpha * mask_color).astype(np.uint8), gray_volume)
    
    return overlayed


def vis_overlay(overlayed, original_vlume, mask_volume, cols=5, display_num=25, figsize= (15, 15)):
    

    # 列数 全体の表示数から行数であまりなしで割って+1
    rows= (display_num - 1) // cols + 1

    # (630, 630, 66, 3) の後ろから２個目が枚数
    total_num = overlayed.shape[-2]

    # 表示する画像の感覚を　全体の枚数から表示したい枚数を割るが、0.xxとかだと0になるのでその場合1を設定する
    interval = total_num / display_num
    if interval < 1:
        interval = 1

    # 画像のサイズ
    fig, ax = plt.subplots(rows, cols, figsize=figsize)

    for i in range(display_num):
        row_i = i // cols
        col_i = i % cols
        # 表示する画像を設定
        idx = int((i * interval))

        #　インデックス数がが総数を上回った場合に抜ける
        if idx >= total_num:
                break
        
        stats = get_hu_stats(original_vlume[:, :, idx], mask_volume[:, :, idx])
        title = f'slice #:{idx}'
        #title += f'ggo mean: {stats['ggo_mean']}±{stats['ggo_std']}'
        title += '\nggo mean: {:.0f}±{:.0f}'.format(stats['ggo_mean'], stats['ggo_std'])
        #title += f'consolidation mean: {stats['consolidation_mean']}±{stats['consolidation_std']}'
        title += '\nconsolidation mean: {:.0f}±{:.0f}'.format(stats['consolidation_mean'], stats['consolidation_std'])
        #title += f'effusion mean: {stats['effusion_mean']}±{stats['effusion_std']}'
        title += '\neffusion mean: {:.0f}±{:.0f}'.format(stats['effusion_mean'], stats['effusion_std'])
        ax[row_i, col_i].imshow(overlayed[:, :, idx])
        ax[row_i, col_i].set_title(title)
        ax[row_i, col_i].axis('off')
        
    # 文字と画像が重なって見にくいので修正
    fig.tight_layout()
        
        
        
def get_hu_stats(volume,
                 mask_volume,
                 label_dict = {1: 'ggo', 2: 'consolidation', 3: 'effusion'}):
    
    
    result = {}
    for label in label_dict.keys():
        # labelを設定
        prefix = label_dict[label]

        roi_hu = volume[np.equal(mask_volume, label)]

        result[prefix + '_mean'] = np.mean(roi_hu)
        result[prefix + '_std']  = np.std(roi_hu)

        
    return result
        
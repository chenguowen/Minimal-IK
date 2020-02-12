from config import *
import pickle
import numpy as np


def prepare_smpl_model():
  with open(OFFICIAL_MANO_PATH, 'rb') as f:
    data = pickle.load(f, encoding='latin1')
  params = {
    'pose_pca_basis': np.array(data['hands_components']),
    'pose_pca_mean': np.array(data['hands_mean']),
    'J_regressor': data['J_regressor'].toarray(),
    'skinning_weights': np.array(data['weights']),
    'mesh_pose_basis': np.array(data['posedirs']),
    'mesh_shape_basis': np.array(data['shapedirs']),
    'mesh_template': np.array(data['v_template']),
    'faces': np.array(data['f']),
    'parents': data['kintree_table'][0].tolist(),
  }
  params['parents'][0] = None
  with open(MANO_MODEL_PATH, 'wb') as f:
    pickle.dump(params, f)


if __name__ == '__main__':
  prepare_smpl_model()
import pickle
path = 'C:/Users/hangge/Desktop/2020-CCF-Crowd-Flow-Prediction-master/solution/cache/area_embedding_0/area_flow_hour_embed_0.pkl'  # path='/root/……/aus_openface.pkl'   pkl文件所在路径
f = open(path, 'rb')
data = pickle.load(f)
print(data)
print(len(data))
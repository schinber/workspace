# from progressbar import progressbar

from tqdm import tqdm

import time
from tqdm import tqdm
# from tqdm._tqdm import trange

for i in tqdm(range(10000)):
    time.sleep(0.01)
# def Run():
#     for i in progressbar(range(100)):
#         b.Download(hero_url[i], "images/head", hero_name[i])
#     print("下载完成")

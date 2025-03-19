"""
@author: Junguang Jiang
@contact: JiangJunguang1123@outlook.com
"""
from typing import Optional
import os
from .imagelist import ImageList
from ._util import download as download_data, check_exits


class S2M(ImageList):
    """Office31 Dataset.

    Args:
        root (str): Root directory of dataset
        task (str): The task (domain) to create dataset. Choices include ``'A'``: amazon, \
            ``'D'``: dslr and ``'W'``: webcam.
        download (bool, optional): If true, downloads the dataset from the internet and puts it \
            in root directory. If dataset is already downloaded, it is not downloaded again.
        transform (callable, optional): A function/transform that  takes in an PIL image and returns a \
            transformed version. E.g, :class:`torchvision.transforms.RandomCrop`.
        target_transform (callable, optional): A function/transform that takes in the target and transforms it.

    .. note:: In `root`, there will exist following files after downloading.
        ::
            amazon/
                images/
                    backpack/
                        *.jpg
                        ...
            dslr/
            webcam/
            image_list/
                amazon.txt
                dslr.txt
                webcam.txt
    """
    download_list = [
        # ("image_list", "image_list.zip", "https://cloud.tsinghua.edu.cn/f/c107de37b8094c5398dc/?dl=1"),
        # ("synth", "synth.tgz", "https://cloud.tsinghua.edu.cn/f/c5f3ce59139144ec8221/?dl=1"),
        # ("real", "real.tgz", "https://cloud.tsinghua.edu.cn/f/da70e4b1cf514ecea562/?dl=1"),
        # ("trans", "trans.tgz", "https://cloud.tsinghua.edu.cn/f/da70e4b1cf514ecea562/?dl=1"),
        # ("trans2", "trans2.tgz", "https://cloud.tsinghua.edu.cn/f/da70e4b1cf514ecea562/?dl=1")
    ]
    image_list = {
        "T3": "image_list/trans3.txt",
        "T2": "image_list/trans2.txt",
        "T": "image_list/trans.txt",
        "qpm": "image_list/sample_qpm.txt",
        "decibel": "image_list/sample_decibel.txt",
        "R": "image_list/real.txt",
    }
    CLASSES = ['2s1','bmp2','btr70','t72','zsu23']

    def __init__(self, root: str, task: str, split: Optional[str] = 'train', download: Optional[bool] = True, **kwargs):
        assert task in self.image_list
        data_list_file = os.path.join(root, self.image_list[task])

        # if download:
        #     list(map(lambda args: download_data(root, *args), self.download_list))
        # else:
        #     list(map(lambda file_name, _: check_exits(root, file_name), self.download_list))

        super(S2M, self).__init__(root, S2M.CLASSES, data_list_file=data_list_file, **kwargs)

    @classmethod
    def domains(cls):
        return list(cls.image_list.keys())
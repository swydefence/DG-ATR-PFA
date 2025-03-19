"""
@author: Junguang Jiang
@contact: JiangJunguang1123@outlook.com
"""
from typing import Optional
import os
from .imagelist import ImageList
from ._util import download as download_data, check_exits


class mstareoc(ImageList):
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

    ]
    image_list = {
        "eoc6": "image_list/eoc5.txt",
        "eoc5": "image_list/eoc5.txt",
        "eoc4": "image_list/eoc4.txt",
        "eoc3": "image_list/eoc3.txt",
        "eoc2": "image_list/eoc2.txt",
        "eoc1": "image_list/eoc1.txt",
        "soc": "image_list/soc.txt",
    }
    CLASSES = ['2s1','brdm2','t72','zsu23']

    def __init__(self, root: str, task: str, split: Optional[str] = 'train', download: Optional[bool] = True, **kwargs):
        assert task in self.image_list
        data_list_file = os.path.join(root, self.image_list[task])

        # if download:
        #     list(map(lambda args: download_data(root, *args), self.download_list))
        # else:
        #     list(map(lambda file_name, _: check_exits(root, file_name), self.download_list))

        super(mstareoc, self).__init__(root, mstareoc.CLASSES, data_list_file=data_list_file, **kwargs)

    @classmethod
    def domains(cls):
        return list(cls.image_list.keys())
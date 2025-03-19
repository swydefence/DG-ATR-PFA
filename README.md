# DG-ATR-PFA
code and datasets for "Domain generalization for SAR target recognition  based on pixel- and feature-level augmentation:  Training on fully simulated data"



code can be used like:

!python main_sample.py data/sample -d Sample -s S T T3 -t R -a resnet50  --log logs/sample/seed0  --phase train -j 1 -b 12 --epochs 30  --mix-layers layer1 layer2 layer3 --seed 0


Our code is developed based on https://github.com/thuml/Transfer-Learning-Library

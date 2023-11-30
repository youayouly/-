from paddlex import transforms as T
import paddlex as pdx

train_transforms = T.Compose([          #定义训练集的数据增强算子
    T.RandomCrop(crop_size=224),
    T.RandomHorizontalFlip(),
    T.Normalize()])

eval_transforms = T.Compose([			#定义评价集的数据增强算子
    T.ResizeByShort(short_size=256),
    T.CenterCrop(crop_size=224),
    T.Normalize()
])

train_dataset = pdx.datasets.ImageNet(		#定义训练集
    data_dir='rubbish',
    file_list='rubbish/train.txt',
    label_list='rubbish/labels.txt',
    transforms=train_transforms,
    shuffle=True)
eval_dataset = pdx.datasets.ImageNet(		#定义评价集
    data_dir='rubbish',
    file_list='rubbish/eval.txt',
    label_list='rubbish/labels.txt',
    transforms=eval_transforms)

num_classes = len(train_dataset.labels)
model = pdx.cls.MobileNetV3_small(num_classes=num_classes)		#定义分类模型

model.train(num_epochs=10,										#模型训练
            train_dataset=train_dataset,
            train_batch_size=64,
            eval_dataset=eval_dataset,
            lr_decay_epochs=[4, 6, 8],
            save_dir='output/mobilenetv3_small',
            use_vdl=True)




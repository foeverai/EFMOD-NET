_base_ = [
    '../_base_/models/deeplabv3_unet_dt_s5-d16.py',
    '../_base_/datasets/deepglobe_1024x1024.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_320k.py'
]
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    test_cfg=dict(crop_size=crop_size, stride=(300, 300)))

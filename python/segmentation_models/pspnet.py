import tensorflow as tf
import segmentation_models as sm


sm.set_framework('tf.keras')

IMG_SIZE = 624

def get_compiled_psp(BACKBONE='efficientnetb3', LR=0.001, n_classes=1, activation='sigmoid', input_shape=(IMG_SIZE, IMG_SIZE, 3)):
    preprocess_input = sm.get_preprocessing(BACKBONE)

    model = sm.PSPNet(BACKBONE, input_shape=input_shape, classes=n_classes, activation=activation)

    optim = tf.keras.optimizers.Adam(LR)

    total_loss = sm.losses.binary_focal_dice_loss

    metrics = [sm.metrics.IOUScore(threshold=0.5), sm.metrics.FScore(threshold=0.5)]

    model.compile(optim, total_loss, metrics)

    return model


model = get_compiled_psp()
model.save('/workspaces/playground/python/pspnet')
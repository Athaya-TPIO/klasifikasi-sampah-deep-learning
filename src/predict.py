"""Prediksi satu gambar dengan model CNN/MLP TrashNet hasil eksperimen UTS.

Contoh:
    python src/predict.py --image contoh.jpg
    python src/predict.py --image contoh.jpg --model models/trashnet_mlp.keras
"""
import argparse
from pathlib import Path

import tensorflow as tf

LABELS = ('cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash')


def predict(model_file: Path, image_file: Path) -> list[tuple[str, float]]:
    model = tf.keras.models.load_model(str(model_file))
    # Sama dengan preprocessing pada notebook (decode JPEG, tf.image.resize, /255).
    raw = tf.io.read_file(str(image_file))
    image = tf.io.decode_jpeg(raw, channels=3)
    image = tf.image.resize(image, (64, 64))
    arr = tf.cast(image, tf.float32) / 255.0
    probs = model.predict(tf.expand_dims(arr, axis=0), verbose=0)[0]
    return sorted(zip(LABELS, (float(x) for x in probs)), key=lambda x: -x[1])


def main():
    parser = argparse.ArgumentParser(description='Prediksi jenis sampah TrashNet')
    parser.add_argument('--image', type=Path, required=True, help='Path gambar sampah')
    parser.add_argument('--model', type=Path, default=Path('models/trashnet_cnn.keras'), help='Model Keras (.keras)')
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f'Gambar tidak ditemukan: {args.image}')
    if not args.model.is_file():
        parser.error(f'Model tidak ditemukan: {args.model}')
    preds = predict(args.model, args.image)
    print(f'Prediksi: {preds[0][0]} (probabilitas {preds[0][1]:.2%})')
    print('Semua probabilitas:')
    for label, p in preds:
        print(f'  {label:<10} {p:.2%}')
    print('Catatan: model UTS eksperimental; tidak untuk pemilahan otomatis tanpa verifikasi.')


if __name__ == '__main__':
    main()

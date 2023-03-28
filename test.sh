python3 app.py
python3 normalization.py
cp dataset/visual.png /Users/mac/Desktop/TAILIEUHOC/PYTHON/PYTHON_CLASS/day16_django/dannyweb/static/images
python3 eval_STGAN.py --loadGP=0/test0_warp5_it50000 --warpN=5 --loadImage=dataset/visual.png
python3 export.py
cp dataset/Figure.png /Users/mac/Desktop/TAILIEUHOC/PYTHON/PYTHON_CLASS/day16_django/dannyweb/static/images

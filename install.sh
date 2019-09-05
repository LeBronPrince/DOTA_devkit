sudo apt-get install swig

swig -c++ -python polyiou.i

python setup.py build_ext --inplace

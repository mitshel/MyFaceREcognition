#Бмблиотеки для FaceRecognition
- OpenCV
- DLib  (http://dlib.net/)
- face_recognition
- OpenFace
- OpenBP

# Интересное железо
- Nvidia Jetson Nano (https://vc.ru/dev/70278-sozdat-sistemu-raspoznavaniya-lic-u-vhodnoy-dveri-za-150-s-pomoshchyu-odnoplatnogo-kompyutera-i-koda-na-python)

# VR маркеры
- ArUco-маркеры (https://clever.copterexpress.com/ru/aruco.html)

# Установка необходимых паетов в Anaconda
conda create --name FR numpy scipy dlib opencv imutils 
conda activate FR
conda config --add channels conda-forge
pip install --no-dependencies face_recognition

# ИСпользование CUDA библиотекой dlib
#First, Check whether dlib identifies your GPU or not.
import dlib.cuda as cuda;
print(cuda.get_num_devices());

#Secondly, dlib.DLIB_USE_CUDA if it's false, simply allow it to use GPU support by
dlib.DLIB_USE_CUDA = True.

# Для ускорения работы dlib необходимо его скомпилировать с поддержкой CUDA
# для этго нужно устанавливать Visual Studio, cmake... etc...
# https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

# Статьи
https://habr.com/ru/company/netologyru/blog/434354/


I also had the same issue. For those who deals with it now -
Firstly you have to install visual studio, and than install there the extension "tools for CMake". 
Look at the installation part here: 
https://docs.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=vs-2019
Only after that you will be able to pip install this package.
So:

    Install VS
    Install the extension "tools for CMake"
    Of course you should also have the python interpreter installed
    In the command line:
        pip install CMake
        pip install face_recognition


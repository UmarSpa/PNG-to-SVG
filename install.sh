pip install svgpathtools
sudo apt-get update
apt install -y imagemagick
apt-get install libtool
sudo apt install intltool imagemagick libmagickcore-dev pstoedit libpstoedit-dev autopoint

git clone https://github.com/autotrace/autotrace.git
cd ./autotrace
./autogen.sh
LD_LIBRARY_PATH=/usr/local/lib ./configure --prefix=/usr
make
sudo make install

autotrace -v

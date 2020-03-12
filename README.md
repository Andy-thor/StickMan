<div align="center">
  <h1>StickMan</h1>
</div>

<div align="center">
  <a href="https://andy-thor.github.io/StickMan">StickMan</a>
  <strong> is a toon being interacting on your desktop.</strong>
</div>

<div align="center">
  StickMan is a free software developed in Python and GTK for the Linux systems.
</div>


<br><br>

## Prerequirements
*1*. Use the package manager [pip] to install the dependencies.
```bash
pip install -r requirements.txt
```
*2*. Install the following packages depending on your system.

___Ubuntu / Debian___:
```bash
sudo apt install libgirepository1.0-dev gcc libcairo2-dev make \
pkg-config python3-dev python3-pip gir1.2-gtk-3.0
```
___Fedora___:
```bash
sudo dnf install gcc gobject-introspection-devel cairo-devel \
make pkg-config python3-devel python3-pip gtk3
```

___Arch Linux___:
```bash
sudo pacman -S python python3-pip cairo pkgconf \
gobject-introspection gtk3 make
```
___openSUSE___:
```bash
sudo zypper install cairo-devel make pkg-config python3-devel \
python3-pip gcc gobject-introspection-devel
```

<br><br>
## Installation

You can install the app typing next sentences:

```bash
sudo python setup.py install --prefix=/usr
```
or simply if you have installed _Make_ you can run these sentences:
```bash
sudo make install
```
More information on the installation method is available in the __*INSTALL*__ file.

<br>

## Usage

### Run without install it:
```bash
python stickman
```
### If it is installed just type:
```bash
stickman
```

[pip]: https://pip.pypa.io/en/stable/

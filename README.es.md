<div align="center">
  <h1>StickMan</h1>
</div>

<br>
<div align="center">
  <a href="https://andy-thor.github.io/StickMan">StickMan</a>
  <strong> es una caricatura interactuando en tu escritorio.</strong>
</div>

<div align="center">
  StickMan es un software libre desarrollado en Python y GTK para los sistemas Linux, Windows y macOS.
</div>

<div align="center">
  <strong>Si eres un usuario de Windows  <img src="https://www.iconfinder.com/icons/386480/download/png/16" alt="Windows icon"> tienes la posibilidad de descargar el <a href="https://github.com/Andy-thor/StickMan/releases/download/v0.3.1/stickman-0.3.1.exe">instalador</a></strong> 
</div>

<br>

*Read this in other languages: [English](README.md), [Spanish](README.es.md).*

## Prerequisitos
*1*. Instalar los siguientes paquetes dependiendo de tu distribución(Linux).
| Distro                                   | Comando  |
|----------------------------------------|:-------------|
| ![ubuntu-icon]___Ubuntu/Debian___ | _sudo apt install libgirepository1.0-dev gcc libcairo2-dev make pkg-config python3-dev gir1.2-gtk-3.0_ |
| ![fedora-icon]___Fedora___ | _sudo dnf install gcc gobject-introspection-devel cairo-devel make pkg-config python3-devel gtk3_ |
| ![arch-icon]___Arch Linux___ | _sudo pacman -S python cairo pkgconf gobject-introspection gtk3 make_ |
| ![opensuse-icon]___openSUSE___ | _sudo zypper install cairo-devel make pkg-config python3-devel gcc gobject-introspection-devel_ |

*2*. Usa el gestor de paquetes [pip] para instalar las dependencias restantes(Linux y __macOS__?). <br> :warning: Esto no funciona en Windows.
```bash
pip install -r requirements.txt
```
<br>

## Instalación

Puedes instalar la app con las siguientes instrucciones:

```bash
sudo python setup.py install --prefix=/usr
```
o simplemente, si tienes instalado _Make_, puedes ejecutar estas instrucciones:
```bash
sudo make install
```
Más información acerca de la instalación se encuentra disponible en el archivo __*INSTALL*__.

<br>

## Uso

#### Ejecutarlo sin instalar:
```bash
python stickman
```
#### Si se encuentra instalado sólo ingrese el nombre:
```bash
stickman
```

[pip]: https://pip.pypa.io/en/stable/
[ubuntu-icon]: https://www.iconfinder.com/icons/4375122/download/png/16
[fedora-icon]: https://www.iconfinder.com/icons/386460/download/png/16
[arch-icon]: https://www.iconfinder.com/icons/386451/download/png/16
[opensuse-icon]: https://www.iconfinder.com/icons/386483/download/png/16

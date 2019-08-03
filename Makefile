BIN = stickman
PREFIX = /usr/share/
PATHBIN = /usr/bin/$(BIN)
DATADIR = $(PREFIX)$(BIN)
DESKTOPDIR = $(PREFIX)applications/$(BIN).desktop
PIXMAPDIR = $(PREFIX)pixmaps/$(BIN).png

install: 
	sudo python setup.py install

uninstall:
	@echo "\033[31mUninstalling the app.\033[0m"
	sudo rm -rf $(PATHBIN)
	sudo rm -rf $(DATADIR)
	sudo rm -rf $(DESKTOPDIR)
	sudo rm -rf $(PIXMAPDIR)

.PHONY: clean
clean:
	rm -rf build/
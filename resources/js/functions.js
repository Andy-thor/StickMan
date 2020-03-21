var devYear = 2019;
var developerFullName = "Andrés Segovia";

function generateTextCopyright() {
	var currentYear = new Date();
	var strTime = "";
	if (devYear === currentYear.getFullYear()) {
		strTimeLapse = devYear.toString();
	} else {
		strTimeLapse = devYear.toString() + "-" + currentYear.getFullYear().toString();
	}

	$("#owner").html("Copyright &copy; " + strTimeLapse + "<br>" + developerFullName);
}

function collapsibleButton () {
	var coll = document.getElementsByClassName("collapsible");
	var i;

	for (i = 0; i < coll.length; i++) {
		coll[i].addEventListener("click", function() {
			this.classList.toggle("active");
			var content = this.nextElementSibling;
			if (content.style.maxHeight) {
				content.style.maxHeight = null;
			} else {
				content.style.maxHeight = content.scrollHeight + "px";
			}
		});
	}
}

function configureEffects() {
	showSlidesAutomatically();
	collapsibleButton();
}

function init() {
	configureEffects();
	generateTextCopyright();
}

function getOS() {
  var userAgent = window.navigator.userAgent,
      platform = window.navigator.platform,
      macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
      windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
      iosPlatforms = ['iPhone', 'iPad', 'iPod'],
      os = null;

  if (macosPlatforms.indexOf(platform) !== -1) {
    os = 'Mac OS';
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    os = 'iOS';
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = 'Windows';
  } else if (/Android/.test(userAgent)) {
    os = 'Android';
  } else if (!os && /Linux/.test(platform)) {
    os = 'Linux';
  }

  return os;
}

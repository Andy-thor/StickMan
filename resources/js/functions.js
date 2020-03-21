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

function generateButtonDownload() {
	var nameFile = "";
	var sizeFile = "";
	var currentOS = getOS();
	var urlDownload = "https://codeload.github.com/Andy-thor/StickMan/zip/master";
	if (currentOS === "Windows") {
		nameFile = "stickman-0.3.1.exe";
		sizeFile = "1.9 MB";
		urlDownload = "https://github.com/Andy-thor/StickMan/releases/download/v0.3.1/stickman-0.3.1.exe";
	} else {
		nameFile = "StickMan-master.zip";
		sizeFile = "483 kB";
	}
	$("#details-download-file").html(
		"<p><span id='name-file' class='bold-text'>Name file:</span> " + nameFile + "</p>" +
		"<p><span id='size-file' class='bold-text size-bytes'>Size:</span> " + sizeFile + "</p>" +
		"<p><span id='platform' class='bold-text'>OS supported:</span> " + currentOS + "</p>");
	$("a.button-download").html("<a href='" + urlDownload + "'>Download StickMan V0.3.1 para Linux</a>");
}

function collapsibleButton() {
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
	generateButtonDownload();
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

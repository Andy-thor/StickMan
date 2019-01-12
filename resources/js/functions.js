var devYear = 2019;
var developerFullName = "Andrés Segovia";

function generateTextCopyright() {
	var currentYear = new Date();
	var strTime = "";
	if (devYear === currentYear.getFullYear()) {
		strTimeLapse = devYear.toString();
	} else {
		strTimeLapse = devYear.toString() + "-" + currentYear.toString();
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
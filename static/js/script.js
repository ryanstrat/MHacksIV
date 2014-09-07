$(document).ready(function () {

	$("#sentimentTab").addClass("hidden");

	$("#closeAnnouncement").click(function (e) {
		e.preventDefault();
		console.log('Hiding');
		$("#announcement").toggle("slide");
	});
	$("#sentimentLink").click(function (e) {
		e.preventDefault();
		$("#investLink").removeClass("active");
		$("#sentimentLink").addClass("active");
		$("#sentimentTab").removeClass("hidden");
		$("#investmentTab").addClass("hidden");
	});
	$("#investLink").click(function (e) {
		e.preventDefault();
		$("#investLink").addClass("active");
		$("#sentimentLink").removeClass("active");
		$("#sentimentTab").addClass("hidden");
		$("#investmentTab").removeClass("hidden");
	});
	$("#close").click(function (e) {
		e.preventDefault();
		$("#proGrow").removeClass("hidden");
		$("#breakdown").addClass("hidden");
	});

});
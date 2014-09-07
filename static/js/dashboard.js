$(document).ready(function () {

	var pieData = [
		{
			value: 50,
			color: "#3498DB",
			highlight: "#32AFDD",
			label: "Bonds"
        },
		{
			value: 50,
			color: "#6EBF87",
			highlight: "#89D2AA",
			label: "Stocks"
        }
    ];

	var pieOptions = {
		responsive: true,
		maintainAspectRatio: true,
		beizierCurve: true,
		bezierCurveTension: 0.4,
		segmentShowStroke: true,
		segmentStrokeColor: "#fff",
		segmentStrokeWidth: 2,
		percentageInnerCutout: 40,
		animationSteps: 50,
		animationEasing: "easeOutQuart",
		animateRotate: true,
		animateScale: true,
		legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>"
	};

	var ctx = document.getElementById("pieChart").getContext("2d");
	var doughnutChart = new Chart(ctx).Doughnut(pieData, pieOptions);

	canvas.onclick = function (evt) {
		var activePoints = doughnutChart.getSegmentsAtEvent(evt);
		$("#stockOrBond").text(activePoints[0].label);
		$("#proGrow").addClass("hidden");
		$("#breakdown").removeClass("hidden");
	};


	var lineData = {
		labels: ["July", "Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
		datasets: [
			{
				label: "My First dataset",
				fillColor: "rgba(47,196,175,0.7)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "#fff",
				pointStrokeColor: "rgba(220,220,220,1)",
				pointHighlightFill: "#fff",
				pointHighlightStroke: "rgba(220,220,220,1)",
				data: [65, 59, 80, 81, 56, 55, 40]
            }
        ]
	};

	var lineOptions = {
		responsive: true,
		maintainAspectRatio: true,
		scaleShowGridLines: true,
		scaleGridLineColor: "rgba(0,0,0,.05)",
		scaleGridLineWidth: 1,
		bezierCurve: false,
		bezierCurveTension: 0.4,
		pointDot: true,
		pointDotRadius: 8,
		pointDotStrokeWidth: 1,
		pointHitDetectionRadius: 20,
		datasetStroke: true,
		datasetStrokeWidth: 2,
		datasetFill: true,
		legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].lineColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
	};

	var ctx = document.getElementById("lineChart").getContext("2d");
	var lineChart = new Chart(ctx).Line(lineData, lineOptions);

	$("#slider").on("change mousemove", function () {
		console.log('fired');
		var stock = 50;
		var bond = 50;
		var value = $("#slider").val();
		stock = value;
		bond = (100 - stock);
		doughnutChart.segments[0].value = bond;
		doughnutChart.segments[1].value = (100 - bond);
		$("#bondVal").text(bond);
		$("#stockVal").text(stock);
		$("#value").text(value);
		doughnutChart.update();
	});


});
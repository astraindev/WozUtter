$(function() {
	$("#bubble-header-update").click(
			function() {
				if (($("#content-display").css("display") === "none")
						&& ($("#content-delete").css("display") === "none")) {
					$("#content-display").show();
					$("#content-delete").hide();
					$("#content-update").hide();
				} else {
					$("#content-display").hide();
					$("#content-delete").hide();
					$("#content-update").show();
				}
			});

	$("#bubble-header-delete").click(function() {
		if (($("#content-display").css("display") === "none")
				&& ($("#content-update").css("display") === "none")) {
			$("#content-display").show();
			$("#content-delete").hide();
			$("#content-update").hide();
		} else {
			$("#content-display").hide();
			$("#content-delete").show();
			$("#content-update").hide();
		}
	});

	$("#content-delete-no").click(function () {
		$("#content-display").show();
		$("#content-delete").hide();
	});
});

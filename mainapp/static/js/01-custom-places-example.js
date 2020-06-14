function runExample3() {
    $("#custom-places").mapsed({
		showOnLoad: 	
		[
			// Random made up CUSTOM place
			{
				// flag that this place should have the tooltip shown when the map is first loaded
				autoShow: true,
				lat: 53.79,
				lng:-1.5426760000000286,
				name: "AMBEDKAR PUBLIC SCHOOL",
				street: "63 Netaji Subhash Path",
				userData: 99
			}

		]
		
	});									
}


$(document).ready(function() {
	runExample3();
});



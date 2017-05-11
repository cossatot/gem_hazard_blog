Title: GEM Global Active Faults
Slug: global-active-fault-viewer
Scripts: leaflet.js, leaflet.ajax.min.js
Styles: leaflet.css

does this work?

<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>

  var mymap = L.map('mapid').setView([31.1, 83.3], 8);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

  var faults = new 
  L.geoJson.ajax("https://raw.githubusercontent.com/cossatot/gem-global-active-faults/master/geojson/gem_active_faults.geojson",{dataType:"jsonp"});

  faults.addTo(mymap)


</script>

I wanna see the faults!

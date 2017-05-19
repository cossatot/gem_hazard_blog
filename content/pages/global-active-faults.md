Title: GEM Global Active Faults
Slug: global-active-fault-viewer


The GEM Global Active Faults project is compiling a global dataset of active
faults for seismic hazard assessment as well as research, education and
general interest. While this is a work in progress, we've got a lot of the
world covered already. Check out the map below, and click on any fault for more
information!

<script src='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.js'></script>
<link href='https://api.mapbox.com/mapbox.js/v3.1.0/mapbox.css' rel='stylesheet' />


<div id="mapid" style="width: 800px; height: 600px;"></div>
<script>

  var mymap = L.map('mapid').setView([31.1, 83.3], 4);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
			'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);

  var faultColors = {
    "Normal": "red",
    "Sinistral-Normal": "#b936ff",
    "Normal-Sinistral": "red",
    "Reverse": "black",
    "Anticline": "grey",
    "Sinistral-Reverse": "#b936ff",
    "Blind Thrust": "black",
    "Sinistral": "#b936ff",
    "Reverse-Sinistral": "black",
    "Dextral-Reverse": "blue",
    "Dextral": "blue",
    "Dextral-Normal": "blue",
    "Thrust": "black",
    "Dextral Normal": "blue",
    "Sinistral Normal": "#b936ff",
    "Strike-Slip": "yellow",
    "Reverse strike-slip": "black",
    "Thrust strike-slip": "black",
    "Sinistral-reverse": "#b936ff",
    "Strike-slip": "yellow",
    "Strike-slip thrust": "yellow",
    "Strike-slip reverse": "yellow",
    "Dextral-reverse": "blue",
    "Syncline": "grey",
    "Strike-Slip-Normal": "yellow",
    "Normal-Dextral": "red",
    "Reverse-Dextral": "black",
    "Strike-Slip-Reverse": "yellow",
    "Strike Slip": "yellow",
    "Reverse-Strike-Slip": "black",
    "": "green"
  };

  var faults = L.mapbox.featureLayer()
    .loadURL("https://raw.githubusercontent.com/GEMScienceTools/gem-global-active-faults/master/geojson/gem_active_faults.geojson")
    .on('ready', function() {
      faults.eachLayer(function(layer) {
        //layer.bindPopup(layer.feature.properties.fz_name);
        var out = [];
        for(key in layer.feature.properties){
          if (layer.feature.properties[key] != null){
            out.push(key+": "+layer.feature.properties[key]);
            }
          }
        layer.bindPopup(out.join("<br />"));
        //  layer.bindPopup(key+": "+feature.properties[key]+"<br />")
        });
      })
      .on('ready', function() {
      faults.eachLayer(function(layer) {
        if (layer.feature.properties.slip_type != null){
        //  layer.feature["marker-color"] = "blue";
        //console.log("slip type \n");
          layer.setStyle({"color": faultColors[layer.feature.properties.slip_type]});
        } else {
        // console.log("no slip type \n")
          //layer.feature["marker-color"] = "green";
          layer.setStyle({"color": "green"});
        };
      });
    })
    .addTo(mymap);


</script>

Many thanks to USAID for funding the GEM Global Active Faults project, and to
the many geoscientists and organizations who have made the regional catalogs
used in this work.

### Data Sources

Catalog                | Publication           | Data Link
-----------------------|-----------------------|-----------
USGS Hazfaults 2014    | [Machette et. al 2003][qf] | [https://earthquake.usgs.gov/hazards/qfaults/](https://earthquake.usgs.gov/hazards/qfaults/)
SHARE                  | [Woessner et al. 2013][sh] | [www.efehr.org](www.efehr.org)
Active Tectonics of the Andes | [Veloza et al. 2012][vz] | [https://github.com/ActiveTectonicsAndes/ATA](https://github.com/ActiveTectonicsAndes/ATA)
Macgregor Africafaults | [Macgregor 2015][mac]      | (*none*)
EMME                   | [Danciu et al. 2014][em]   | [www.efehr.org](www.efehr.org)
GEM Active Faults      | (*none*)                   | [https://github.com/GEMScienceTools/gem-global-active-faults](https://github.com/GEMScienceTools/gem-global-active-faults)
HimaTibetMap           | [Styron et al. 2010][st]   | [https://github.com/HimaTibetMap/HimaTibetMap](https://github.com/HimaTibetMap/HimaTibetMap)
Myanmar                | (*none*)                   | (*none*)
GEM Central Am. Carib  | Styron et al. *in prep*.         | [https://github.com/GEMScienceTools/central_am_carib_faults](https://github.com/GEMScienceTools/central_am_carib_faults)
GEM N. Africa          | Styron, *in prep*.  | [https://github.com/GEMScienceTools/n_africa_active_faults](https://github.com/GEMScienceTools/n_africa_active_faults)
Philippines            | (*none*)                   | (*none*)
SARA                   | (*none*)                   | [http://ftp.openquake.org/data/sara/hazard/t2/SARA_T2_HF.zip](http://ftp.openquake.org/data/sara/hazard/t2/SARA_T2_HF.zip)
Thailand               | (*none*)                   | (*none*)
Taiwan                 | [Shyu et al. 2016][sh]     | [http://tao.cgu.org.tw/index.php/articles/archive/geophysics/item/download/2182_65e077a158d69f598522df397124c99d](http://tao.cgu.org.tw/index.php/articles/archive/geophysics/item/download/2182_65e077a158d69f598522df397124c99d)


<br>
Questions? Concerns? Suggestions about data? Please contact Richard Styron at
richard.styron (at) globalquakemodel.org.


[qf]: https://pubs.er.usgs.gov/publication/ofr03417
[sh]: http://link.springer.com/article/10.1007/s10518-015-9795-1
[vz]: https://www.geosociety.org/gsatoday/archive/22/10/article/i1052-5173-22-10-4.htm
[mac]: http://www.sciencedirect.com/science/article/pii/S1464343X14003240
[em]: http://link.springer.com/article/10.1007/s10518-017-0096-8
[st]: http://onlinelibrary.wiley.com/doi/10.1029/2010EO200001/full
[sh]: http://tao.cgu.org.tw/index.php/articles/archive/geophysics/item/1376


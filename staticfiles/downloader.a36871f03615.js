function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return JSON.parse(Httpreq.responseText);
}
var json_obj = Get('https://gist.githubusercontent.com/cfahlgren1/38167a6c7befae3549ad5815ff4f377f/raw/7b6e0c015e248da0fe7af00198f2022870fc47e7/court_info');
self.postMessage(json_obj);





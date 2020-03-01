importScripts('https://cdn.jsdelivr.net/npm/@turf/turf@5/turf.min.js');

self.addEventListener('message', function (e) {
    searchedFeature = e.data[0];
    all_courts = e.data[1];

    // loop through entire geojson and find nearest stores
    var options = {units: 'miles'};
    var i = 0;

    all_courts.forEach(function (court) {
        // format coordinates
        var coordinates = String(court.coordinates).replace("[", "").replace("]", ""); //needs fixing
        coordinates = coordinates.split(",");
        coordinates = coordinates.map(Number);

        i++; // iterate count

        Object.defineProperty(court, 'coordinates', {
            value: coordinates,
            writable: true,
            enumerable: true,
            configurable: true
        });

        Object.defineProperty(court, 'distance', {
            value: turf.distance(searchedFeature, court, options),
            writable: true,
            enumerable: true,
            configurable: true
        });
    });
    all_courts.sort(function (a, b) {
        if (a.distance > b.distance) {
            return 1;
        }
        if (a.distance < b.distance) {
            return -1;
        }
        // a must be equal to b
        return 0;
    });
    // Send the message back.
    self.postMessage(all_courts);
}, false);

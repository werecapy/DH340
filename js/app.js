// navigation
map.doubleClickZoom.enable();

// error handling
console.log("Adding marker for", venue.Name, venue.Latitude, venue.Longitude);
console.log("Performances:", perfList);
riseOnHover= true
autoPanOnFocus= true
//testing
map.on('onmouseover', function(ev) {
    alert(ev.latlng); // ev is an event object (MouseEvent in this case)
});
function getAllUniqueDates() {
  const dates = new Set();
  venuesData.forEach(venue => {
    const venueName = venue.Name.trim();
    const performances = performancesData[venueName] || [];
    performances.forEach(p => dates.add(p.date));
  });

  return Array.from(dates).sort((a, b) => new Date(a) - new Date(b));
}
setupSlider();
setupSearch(); // if you're still using search too
popupContent += `<br><a href="/?venue=${encodeURIComponent(venueName)}">Add Performance</a>`;


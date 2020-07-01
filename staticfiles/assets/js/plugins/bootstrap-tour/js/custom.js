$(function() {



// Instance the tour
var tour = new Tour({
steps: [
  {
    element: "#metrics",
    title: "See your key metrics",
    content: "Key metrics across all locations",
    backdrop:true,
    placement:"auto bottom"
  },
  {
    element: "#AllVisits",
    title: "Explore recent visits",
    content: "See a list of the most recent visits across your locations, filter and export the data.",
    backdrop:true,
    placement:"auto top"
  },
  {
    path: "/locations/",
    element: "#addButton",
    title: "Title of my step",
    content: "Content of my step",
    backdrop:true,
    placement:"auto top",
  },
],
backdropContainer: 'body',
backdropPadding: 0,
debug:true,
storage:false,
});

// Initialize the tour
tour.init();

// Start the tour
tour.start();

})

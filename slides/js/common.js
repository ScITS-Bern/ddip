remark.macros.scale = function (percentage) {
  var url = this;
  return '<img src="' + url + '" style="width: ' + percentage + '" />';
};

var slideshow = remark.create({
  highlightLanguage: "terminal",
  highlightStyle: "tomorrow-night-bright",
  countIncrementalSlides: false
});

$('code.terminal span.hljs-ansi').replaceWith(function(i, x) {
  return x.replace(/&lt;(\/?(\w+).*?)&gt;/g, '<$1>');
});

$('.quiz td').click(function() {
  $(this).addClass('clicked');
});

slideshow.on('showSlide', function (slide) {
  $('.quiz td').removeClass('clicked');
});

// If loaded locally, try to inject livereload
if (location.protocol === "file:") {
  var s = document.createElement("script");
  s.src = "http://localhost:35729/livereload.js?snipver=1";
  document.body.appendChild(s);
}

(function() {
  var eventsource = new EventSource("https://stream.wikimedia.org/v2/stream/recentchange");
  
  var feedNode = document.getElementById('feed');
  var rateMinNode = document.getElementById('rate-min');
  var rateAvgNode = document.getElementById('rate-avg');
  var errorNode = document.createElement('div');
  errorNode.className = 'alert alert-danger';
  var infoNode = document.createElement('div');
  infoNode.className = 'alert alert-info';
  var updateBuffer = makeDisplayBuffer(10);
  var freq;
  printEvent({
    type: 'info',
    message: 'Connecting...'
  });
  eventsource.onopen = function() {
    printEvent({
      type: 'info',
      message: 'Connected! Listening for events...'
    });
    freq = new Frequency(1000, function (count, average) {
      rateMinNode.textContent = count;
      rateAvgNode.textContent = average;
    });
  };

  eventsource.onmessage = function(msg) {
    if (freq) { freq.add(1); }
    printEvent({type: 'message', data: msg.data});
  };

  eventsource.onerror = function(msg) {
    // Don't print {isTrusted: true}.  (Is this an error?)
    if (!msg.isTrusted) {
      printEvent({
       type: 'error',
       data: msg
      });
    }
  };

  function printEvent(event) {
    var node;
    if (event.type === 'message') {
      var node = document.createTextNode(event.data + '\n\n');
      $(feedNode).prepend(node);
      updateBuffer(node);
    } else if (event.type === 'error') {
      $(errorNode).empty().text('ERROR: ' + JSON.stringify(event.data));
      if (!errorNode.parentNode) {
        $(feedNode).before(errorNode);
      }
    } else if (event.type === 'info') {
      $(infoNode).text(event.message);
      if (!infoNode.parentNode) {
        $(feedNode).prepend(infoNode);
        updateBuffer(infoNode);
      }
    }
  }

  function makeDisplayBuffer(size) {
    var buffer = [];
    return function (element) {
      buffer.push(element);
      if (buffer.length > size) {
        var popped = buffer.shift();
        popped.parentNode.removeChild(popped);
      }
    }
  }
}());

function Frequency(interval, callback) {
  var freq = this;
  var rAF = window.requestAnimationFrame || setTimeout;

  this.interval = interval;
  this.callback = callback;
  this.count = 0;
  this.total = 0;
  this.since = this.start = this.now();
  function checker() {
    freq.check();
    rAF(checker);
  }
  rAF(checker);
}
Frequency.prototype.now = ( function () {
  var perf = window.performance;
  return perf.now ?
    function () { return perf.now(); } :
    function () { return +new Date(); };
}() );
Frequency.prototype.add = function (count) {
  this.count += count;
  this.total += count;
  this.check();
};
Frequency.prototype.check = function () {
  var count, avg, ellapsedTotal;
  var ellapsed = this.now() - this.since;
  if (ellapsed >= this.interval) {
    ellapsedTotal = this.now() - this.start;
    count = this.count;
    // One optional digit
    avg = (this.total / (ellapsedTotal / this.interval)).toFixed(1).replace('.0', '');
    this.since = this.now();
    this.count = 0;
    this.callback(count, avg);
  }
};
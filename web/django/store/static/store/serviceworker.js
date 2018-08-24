// Empty Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in
// settings.py

var CACHE_NAME = 'itlabstore-cache-v1';
var urlsToCache = [
  '/',
  '/static/store/bootstrap.3.3.7.min.css',
  '/static/store/jquery.3.2.1.min.js',
  '/static/store/bootstrap.3.3.7.min.js'
];

// Performs install steps
self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened Cache');
        return cache.addAll(urlsToCache);
      })
  )
});

// Fetch events with SW
self.addEventListener('fetch', function(event) {
  event.respondWith(caches.open(CACHE_NAME).then(function(cache) {
      return fetch(event.request).then(function(response){
        cache.put(event.request, response.clone());
        return response;
      }).catch(function(){
        return cache.match(event.request);
      });
    })
  );
});
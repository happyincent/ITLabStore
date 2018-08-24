# ITLabStore ([PWA](https://developers.google.com/web/progressive-web-apps/))

## Enviroments
* Nginx
* Django + uWSGI

## Usage
### First time
```
# docker-compose.yml
51 - ./conf/nginx_init.conf:/etc/nginx/nginx.conf:ro
52 # - ./conf/nginx.conf:/etc/nginx/nginx.conf:ro

# run
docker-compose up -d noip web nginx
docker-compose up letsencrypt
```
### Then
```
# docker-compose.yml
51 # - ./conf/nginx_init.conf:/etc/nginx/nginx.conf:ro
52 - ./conf/nginx.conf:/etc/nginx/nginx.conf:ro

# run
docker-compose down
docker-compose up -d
```

## References
* Service Worker
    * https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API
* ICON & UI
    * https://www.flaticon.com/
    * https://www.w3schools.com/bootstrap/bootstrap_tabs_pills.asp
* DNS (No-IP)
    * https://github.com/coppit/docker-no-ip
* HTTPS (Let’s Encrypt)
    * https://github.com/kvaps/docker-letsencrypt-webroot

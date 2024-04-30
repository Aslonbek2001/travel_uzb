# server {
#     listen 8030;
#     server_name 146.190.172.173;

#     location = /favicon.ico { access_log off; log_not_found off; }

#     location /static/ {
#             alias /home/Travel/travel_uzb/static/;
#     }
#     location /media/ {
#             alias /home/Travel/travel_uzb/media/;
#     }

#     location / {
#             include proxy_params;
#             proxy_pass http://146.190.172.173:8030;
#     }
# }
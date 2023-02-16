#!/bin/sh
gnome-terminal --window-with-profile=scriptMonkey -- bash -c "source airflow_env/bin/activate; cd airflow; airflow scheduler" & gnome-terminal --window-with-profile=scriptMonkey -- bash -c "source airflow_env/bin/activate; cd airflow; airflow webserver"

sleep 20
gnome-terminal -- bash -c "google-chrome http://localhost:8080/." 



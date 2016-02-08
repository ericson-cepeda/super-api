source /env/bin/activate
nohup watchmedo shell-command --patterns="*.py;*.jade" --recursive --command='supervisorctl restart api:api_00' . &
nohup watchmedo shell-command --patterns="*.js;*.styl" --recursive --command='python manage.py collectstatic --noinput' . &

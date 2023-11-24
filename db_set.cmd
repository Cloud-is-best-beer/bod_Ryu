@echo off
flask db init
flask db migrate
flask db upgrade
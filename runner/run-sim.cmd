cd %1
poetry install
poetry run stw_leosim --config .\config\sim_config.yml --models sat_config --init-state duty_mode --duration 100000
pause
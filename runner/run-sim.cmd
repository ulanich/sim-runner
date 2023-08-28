cd %1
poetry install
poetry env info
pause
poetry run stw_leosim --config .\config\sim_config.yml --models %2 --init-state %3 --duration %4 %5
pause
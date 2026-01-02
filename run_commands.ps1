# Student Management System - PowerShell Commands
# Usage: .\run_commands.ps1 [command]

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Student Management System - Available Commands" -ForegroundColor Cyan
    Write-Host "==============================================" -ForegroundColor Cyan
    Write-Host ".\run_commands.ps1 install    - Install dependencies"
    Write-Host ".\run_commands.ps1 init       - Initialize database"
    Write-Host ".\run_commands.ps1 seed       - Seed sample data"
    Write-Host ".\run_commands.ps1 run        - Run development server"
    Write-Host ".\run_commands.ps1 test       - Run tests"
    Write-Host ".\run_commands.ps1 clean      - Clean up generated files"
    Write-Host ".\run_commands.ps1 setup      - Complete setup (install + init)"
}

function Install-Dependencies {
    Write-Host "Installing dependencies..." -ForegroundColor Green
    pip install -r requirements.txt
}

function Initialize-Database {
    Write-Host "Initializing database..." -ForegroundColor Green
    python scripts\init_db.py
}

function Seed-Data {
    Write-Host "Seeding sample data..." -ForegroundColor Green
    python scripts\seed_data.py
}

function Start-Server {
    Write-Host "Starting development server..." -ForegroundColor Green
    python run.py
}

function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Green
    pytest
}

function Clean-Files {
    Write-Host "Cleaning up generated files..." -ForegroundColor Green
    Remove-Item -Path __pycache__ -Recurse -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Directory -Recurse | Where-Object { $_.Name -eq '__pycache__' } | Remove-Item -Recurse -Force
    Remove-Item -Path .pytest_cache -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path htmlcov -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path .coverage -Force -ErrorAction SilentlyContinue
    Write-Host "Cleanup complete!" -ForegroundColor Green
}

function Complete-Setup {
    Write-Host "Running complete setup..." -ForegroundColor Cyan
    Install-Dependencies
    Initialize-Database
    Write-Host "`nSetup complete! Run '.\run_commands.ps1 run' to start the server." -ForegroundColor Green
}

# Main command router
switch ($Command.ToLower()) {
    "install" { Install-Dependencies }
    "init" { Initialize-Database }
    "seed" { Seed-Data }
    "run" { Start-Server }
    "test" { Run-Tests }
    "clean" { Clean-Files }
    "setup" { Complete-Setup }
    "help" { Show-Help }
    default {
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Show-Help
    }
}
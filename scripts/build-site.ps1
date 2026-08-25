[CmdletBinding()]
param(
    [switch]$VerifyOnly
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = 'py'
    $pythonArgs = @('-3')
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = 'python'
    $pythonArgs = @()
} else {
    throw 'Python 3 is required. Install Python and make either py or python available on PATH.'
}

$arguments = @((Join-Path $root 'scripts\verify_site.py'))
if (-not $VerifyOnly) { $arguments += '--build' }

Push-Location $root
try {
    & $pythonCommand @pythonArgs @arguments
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
    Pop-Location
}

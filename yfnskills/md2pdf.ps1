# md -> PDF wrapper for yfnskills deliverables (Windows convenience).
#
#   .\md2pdf.ps1 <file.md | directory> [-Serif] [-KeepHtml]
#   .\md2pdf.ps1 -Check
#
# Locates a Python interpreter, makes sure a markdown parser is importable, then
# calls md2pdf.py. All the real work and all platform detection live in the .py,
# so `python md2pdf.py <target>` works identically without this wrapper.

param(
  [Parameter(Position = 0)][string]$Target,
  [switch]$Serif,
  [switch]$KeepHtml,
  [switch]$Check
)

$ErrorActionPreference = 'Stop'

if (-not $Target -and -not $Check) { throw "usage: .\md2pdf.ps1 <file.md | directory> [-Serif] [-KeepHtml] | -Check" }

# Interpreter discovery: PATH first, then the py launcher, then the standard
# per-user and machine-wide install roots. No pinned version numbers.
$py = $null
foreach ($n in @('python3', 'python')) {
  $c = Get-Command $n -ErrorAction SilentlyContinue
  # Windows ships an App Execution Alias stub that resolves but cannot run.
  if ($c -and $c.Source -and $c.Source -notlike '*WindowsApps*') { $py = $c.Source; break }
}
if (-not $py) {
  $launcher = Get-Command py -ErrorAction SilentlyContinue
  if ($launcher) {
    $p = (& $launcher.Source -3 -c "import sys; print(sys.executable)" 2>$null)
    if ($LASTEXITCODE -eq 0 -and $p) { $py = $p.Trim() }
  }
}
if (-not $py) {
  $roots = @("$env:LOCALAPPDATA\Programs\Python", "$env:ProgramFiles\Python*", "C:\") |
           Where-Object { $_ }
  foreach ($r in $roots) {
    $hit = Get-ChildItem -Path $r -Filter 'python.exe' -Recurse -Depth 2 -ErrorAction SilentlyContinue |
           Sort-Object FullName -Descending | Select-Object -First 1
    if ($hit) { $py = $hit.FullName; break }
  }
}
if (-not $py) { throw "python not found. Install Python 3 from python.org, or add it to PATH." }

& $py -c "import markdown" 2>$null
if ($LASTEXITCODE -ne 0) {
  & $py -c "import markdown_it" 2>$null
  if ($LASTEXITCODE -ne 0) {
    Write-Host "installing a markdown parser..."
    & $py -m pip install --quiet markdown
    if ($LASTEXITCODE -ne 0) {
      throw "no markdown parser and pip install failed (offline?). Run: $py -m pip install markdown"
    }
  }
}

$script = Join-Path $PSScriptRoot 'md2pdf.py'
if (-not (Test-Path $script)) { throw "md2pdf.py not found next to this wrapper" }

$argv = @($script)
if ($Check) { $argv += '--check' } else { $argv += $Target }
if ($Serif)    { $argv += '--serif' }
if ($KeepHtml) { $argv += '--keep-html' }

& $py @argv
exit $LASTEXITCODE

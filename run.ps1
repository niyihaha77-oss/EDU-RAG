# 一键运行 Python 脚本，自动加载 .env 里的环境变量
#
# 用法：
#   .\run.ps1 test_redis.py
#   .\run.ps1 test_milvus.py
#   .\run.ps1 day01\01-ollama.py
#
# 如果提示"禁止运行脚本"，先执行一次：
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Script,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ScriptArgs
)

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$envFile = Join-Path $root ".env"

# 加载 .env（格式：KEY=VALUE，忽略空行和 # 注释）
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
            $idx = $line.IndexOf("=")
            $key = $line.Substring(0, $idx).Trim()
            $val = $line.Substring($idx + 1).Trim()
            # 去掉可能存在的引号
            $val = $val.Trim('"').Trim("'")
            Set-Item -Path "env:$key" -Value $val
        }
    }
    Write-Host "[env] 已加载 $envFile" -ForegroundColor DarkGray
} else {
    Write-Host "[env] 未找到 .env，使用系统环境变量" -ForegroundColor Yellow
}

# 保证中文输出不乱码
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

# 切换到项目根目录后运行
Push-Location $root
try {
    python $Script @ScriptArgs
    $code = $LASTEXITCODE
} finally {
    Pop-Location
}
exit $code

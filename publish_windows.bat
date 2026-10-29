@echo off
setlocal
cd /d "%~dp0"
where git >nul 2>&1
if errorlevel 1 (
  echo Git belum tersedia. Instal Git for Windows dari https://git-scm.com/downloads/win
  pause
  exit /b 1
)
echo ===========================================
echo  Publikasi repo UTS Kelompok 6 ke GitHub
echo ===========================================
echo Buat repo KOSONG terlebih dahulu di https://github.com/new
set /p REPO_URL=Masukkan URL HTTPS repo (contoh https://github.com/username/klasifikasi-sampah-deep-learning.git): 
if "%REPO_URL%"=="" (
  echo URL repo wajib diisi.
  pause
  exit /b 1
)
if not exist .git (
  git init
  if errorlevel 1 goto failed
)
git branch -M main
if errorlevel 1 goto failed
git add .
if errorlevel 1 goto failed
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "Initial commit: UTS TrashNet MLP CNN"
  if errorlevel 1 goto failed
)
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin "%REPO_URL%"
  if errorlevel 1 goto failed
) else (
  echo Remote origin sudah ada. Menggunakan remote yang tersedia:
  git remote -v
)
git push -u origin main
if errorlevel 1 goto failed
echo.
echo Berhasil! Periksa repositori di GitHub.
pause
exit /b 0
:failed
echo.
echo Perintah Git gagal. Cek pesan error di atas dan ikuti panduan PANDUAN_UPLOAD_GITHUB.md
pause
exit /b 1

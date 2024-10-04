@echo off

REM Diretório onde os arquivos serão criados
set "diretorio=C:\caminho\do\diretorio"

REM Criação dos arquivos
for /L %%i in (1,1,20) do (
    set "numero=000%%i"
    set "nome_arquivo=File_!numero:~-5!.py"
    echo. > "%diretorio%\!nome_arquivo!"
)

echo Arquivos criados com sucesso!
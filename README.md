# CNAB-Python

Essa aplicação serve como um leitor de arquivos CNAB. Basta fazer o upload do seu arquivo que as informações serão renderizadas em tela.

Tecnologias utilizadas: Python e Django.

Para inicializar o seu ambiente virtual, digite o seguinte comando no terminal:

python -m venv venv

Para ativá-lo:

Windows:
.\venv\Scripts\activate

Linux:
source venv/bin/activate

Para desativá-lo:
deactivate

Para instalar as dependências:

pip install -r requirements.txt

Para rodar o servidor:

python manage.py runserver

Uma vez com o servidor rodando, para acessar digite no seu browser:

http://localhost:8000/api/files/

Faça o upload do arquivo CNAB, e clique em "view data".

Pronto, as informações do seu arquivo serão renderizadas.

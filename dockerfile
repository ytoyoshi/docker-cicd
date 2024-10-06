FROM python:3.10-slim

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリを設定
WORKDIR /code

# 依存関係をインストール
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトをコピー
COPY . /code/

# アプリケーションを実行
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "dockercicd.wsgi:application"]
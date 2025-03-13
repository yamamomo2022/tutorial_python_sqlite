# ベースイメージを指定
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# プロジェクトの依存関係をコピーしてインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .

# コンテナ起動時に実行するコマンドを指定
CMD ["python", "app.py"]
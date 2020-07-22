# dht11-influx

ラズパイで温湿度センサ DHT11 を使って温度と湿度を取得し、InfluxDB に保存、grafana で可視化します。

## Requirements

- docker
- docker-compose

## Installation

```
docker-compose up -d
```

コンテナが立ちあがったら http://localhost:3000 で grafana にアクセスできます。初期 ID, PW はどちらも admin です。grafana からは

```
URL: http://influxdb:8086
database: dht11
```

でデータベースにアクセスできます。

# 📊 Dockerized Node.js App with Monitoring

This project runs a Node.js application inside a Docker container with Prometheus and Grafana configured for monitoring.

---

## 🔧 Stack
- Node.js (Express)
- Docker & Docker Compose
- Prometheus
- Grafana

---

## 🐳 How to Run

```bash
docker-compose up --build
```

- Access the app: http://localhost:3000/
- Prometheus: http://localhost:9090/
- Grafana: http://localhost:3001/ (default login: admin / admin)

---

## 📈 Monitoring

- Prometheus scrapes metrics from the Node.js app.
- Grafana visualizes data (you can import a dashboard from Prometheus data source).

---

## 📁 Structure

```
.
├── app/
│   ├── app.js
│   └── package.json
├── Dockerfile
├── docker-compose.yml
├── monitoring/
│   └── prometheus.yml
└── README.md
```

---

## 📌 Notes

- The Node.js app in this example does not expose Prometheus-compatible metrics.
- You can integrate metrics using libraries like `prom-client`.

---
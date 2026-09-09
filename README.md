# Robotics TurtleBot3 - Modul 1

Repositori pengembangan ROS 2 Humble berbasis Docker untuk praktikum TurtleBot3.

## Prasyarat
- Docker Engine >= 24
- Docker Compose plugin >= v2.20
- Git >= 2.34
- Linux / WSL2 Ubuntu 22.04

## Struktur Repositori
```text
robotics-turtlebot3/
├── docker/
│   ├── Dockerfile
│   ├── compose.yaml
│   └── entrypoint.sh
├── src/
│   └── my_first_robot_package/
├── docs/
│   └── screenshots/
└── README.md
```

## Langkah Build dan Menjalankan

### 1. Persiapan Host
Pastikan izin akses X11 dan variabel lingkungan telah disetel:
```bash
cd docker
export UID=$(id -u) GID=$(id -g) ROS_DOMAIN_ID=31
xhost +local:docker 2>/dev/null || true
```

### 2. Build Docker Image
```bash
docker compose build
```

### 3. Menjalankan Container
```bash
docker compose up -d
```

### 4. Masuk ke Container & Build Workspace
```bash
docker compose exec dev bash
```
Di dalam container:
```bash
cd /ws
colcon build --symlink-install
source install/setup.bash
```

### 5. Menjalankan Node ROS 2
```bash
ros2 run my_first_robot_package hello_robot
```
Output yang diharapkan:
```text
Hi from my_first_robot_package.
```

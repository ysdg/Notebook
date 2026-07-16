docker run -d \
  --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  -v /root/yq/data:/data \
  -p 30002:19592 \
  --name tsdb-rtdservice-0 \
  registry.supos.ai/jenkins/tsdb-rtdservice:Master-7.0-Debug

nohup ./bootstrap.sh > output.log 2>&1 &

/os/open-api/tsdb/v3/config
docker stop tsdb-rtdservice-0 
docker rm tsdb-rtdservice-0 
docker exec -it platform-tsdb-service-1 /bin/bash

docker inspect platform-tsdb-service-1 | grep -A 15 "NetworkSettings"
docker inspect platform-tsdb-service-1 | grep -A 15 Mounts
cd /volumes/data/docker/volumes/platform-vxbase-tsdb-service-workspace/_data
cd /volumes/data/docker/volumes/platform-vxbase-data/_data

curl -X 'GET' 'http://127.0.0.1:19592/os/inter-api/iot-config/v3/config/database/duration' 
curl -X 'POST' 'http://127.0.0.1:19592/os/inter-api/iot-config/v3/config/database/duration' -d '{"duration": 365}'

curl -X GET "http://127.0.0.1:17022/api/ps/cmd?dest=BsRtdService.BsRtdService&cmd=sd%20dump%20tag%20_ts_file2_734a33bfb226420b89cf"
curl -X GET "http://127.0.0.1:17022/api/ps/cmd?dest=BsAlarmHistoryService.BsAlarmArchiveService&cmd=?"


ngrep -W byline -qd any 'tags/query' tcp port 19592
curl -X 'POST' 'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/tags/query' -d '{"resultType":"updated","pageNo":1,"pageSize":2, "conditions":[{"field":"alias","opr":"in","value":["test_collector72_DataItem_0003","test_collector72_DataItem_0004"]}]}'
curl -X 'POST' 'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/tags/query' -H 'Content-Type: application/json' -d '{"resultType": "updated","pageNo": 1,"pageSize": 2}'

curl -X 'POST' \
  'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/tags/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "resultType": "updated",
  "pageNo": 1,
  "pageSize": 2
}'

curl -X 'GET' \
  'http://127.0.01:19592/os/inter-api/iot-config/v3/config/database/duration' \
  -H 'accept: application/json'

curl -X 'POST' \
  'http://127.0.01:19592/os/inter-api/iot-config/v3/config/database/duration' \
  -H 'accept: application/json' \
  -d '
	{
	"duration": 364,
	"unit": "day",
	}
  '

curl -X 'GET' \
  'http://127.0.01:19592/os/open-api/tsdb/v3/config/devices?aliasQuery=col&pageNo=1&pageSize=20' \
  -H 'accept: application/json'
curl -X 'GET' \
  'http://127.0.01:19592/os/inter-api/iot-config/v3/config/devices?pageNo=1&pageSize=20' \
  -H 'accept: application/json'

curl -X 'GET' \
  'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/tags?device=col1&pageNo=1&pageSize=20' \
  -H 'accept: application/json'

curl -X 'GET' \
  'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/deviceSources?pageNo=1&pageSize=20' \
  -H 'accept: application/json'

curl -X 'GET' \
  'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/dispatcher/tasks?name=aaa&pageNo=1&pageSize=20'
curl -X 'GET' \
  'http://127.0.0.1:19592/os/open-api/tsdb/v3/config/dispatcher/tasks/81803fb4-9a07-477a-b0a1-8a4c61ab5d7f/tags?order=asc&orderBy=name&pageNo=1&pageSize=5000'

curl -X GET "http://127.0.0.1:21087/inter-api/tsdb-service/api/v1/event/odsx5nd1-4nnj-ypyh-icz4-1774242196368" 
curl -X GET "http://127.0.0.1:19598/inter-api/tsdb-service/smt/devices/event/3vgw7gz2-ftgd-s5ij-hicw-1752123921805" 

curl -X 'GET' \
  'http://127.0.0.1:19592/os/inter-api/iot-config/v3/config/status' \
  -H 'accept: application/json'


cp -f /data/libBsAPIServerHttpCfg.so /app/bin/VxBase/plugin/BsAPIService/
cp -f /data/isys-config   /app/icore/config/

scp lib/linux/libBsAPIServerHttpCfg.so root@192.168.12.68:/var/lib/docker/volumes/platform-vxbase-data/_data
scp bin/linux/isys-config root@192.168.12.68:/var/lib/docker/volumes/platform-vxbase-data/_data


set env LD_LIBRARY_PATH=/app/lib
set args   -configfile -nodeport 17020 -dpname Project_001 -dppath /data

http://192.168.236.56:8091/inter-api/supos/uns/sync/cli
curl -X 'GET' \
  'http://192.168.237.111:8091/os/inter-api/supos/uns/sync/cli' \
  -H 'accept: application/json'

ulimit -c unlimited
echo '/tmp/core.%t.%e.%p' | sudo tee /proc/sys/kernel/core_pattern

CONTAINER_PID=$(docker inspect --format {{.State.Pid}} platform-tsdb-service-1)
sudo nsenter --target $CONTAINER_PID --mount --uts --ipc --net --pid gdb

# 时序容器内部安装gdb的步骤,执行以下三条命令：
sed -i s#http://deb.debian.org/debian#http://mirrors.supos.ai/debian#g  /etc/apt/sources.list.d/debian.sources
apt update
apt install gdb -y
apt install sqlite3 -y

CONTAINER_PID=$(docker inspect --format {{.State.Pid}} platform-tsdb-service-1)
sudo nsenter --target $CONTAINER_PID --mount --uts --ipc --net --pid gdb


curl --header 'X-Client-From: ops' --location --request POST 'http://192.168.13.40:30010/os/open-api/installer/v1/install' --form 'downloadPath="http://192.168.10.2/supos7/apps-package/VxBase/VxBase%40V7.05.00.00-C-R1-amd64.zip"'

curl --header 'X-Client-From: ops' --location --request POST 'http://192.168.13.40:30010/os/open-api/installer/v1/install' --form 'downloadPath="http://192.168.10.2/supos7/apps-package/alarm/alarm%40V7.05.00.00-C-R1-amd64.zip"'

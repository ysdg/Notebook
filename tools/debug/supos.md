# supOS & k8s 常用命令

## pod操作

```bash
# 进入tsdb-dproxy
kubectl exec -it  $(kubectl get po | grep tsdb-dproxy | awk '{print $1}') -- bash
 
# 进入tsdb-service
kubectl exec -it tsdb-service-0 -c=tsdb-service -- bash
 
# 查看内存：
kubectl top pods | sort -k3 -hr
 
# k8s拉包&删包，自动启动：
docker pull registry.supos.ai/jenkins/tsdb-service:5.00.01.00-C-M6-T2 && kubectl delete po $(kubectl get po | grep tsdb-service | awk '{print $1}')
```

## 编辑启动参数

```bash

# 修改tsdb-service
kubectl edit sts tsdb-service
 
#修改tsdb-dproxy
kubectl edit deploy tsdb-dproxy
 
# 开放ip端口
kubectl edit svc tsdb-service-dt
#type中的ClusterIP，改成NodePort
```

## 查看日志

```bash

# 查看日志
kubectl logs -f $(kubectl get po | grep tsdb-api | awk '{print $1}')
kubectl logs tsdb-service-0 -c=tsdb-service
 
# 查看描述
kubectl describe pod my-pod
kubectl describe pod tsdb-service-0
```

## 网络

```bash
# k8s 转发
kubectl port-forward tsdb-service-0 30000:17022 --address=0.0.0.0
# 直接使用socat转发。k8s无法访问socat时使用
socat TCP-LISTEN:local_port,fork TCP:kubernetes_node_ip:kubernetes_node_port
socat TCP-LISTEN:30000,fork TCP:$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022
curl -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022/api/ps/cmd?dest=BsRtdService.BsRtdService&cmd=opr%20devinfo%20DefaultVirtualDevice"
curl -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022/api/ps/cmd?dest=BsRtdService.BsRtdService&cmd=tag%20dump%20t3:dhb_col_ae/ae"
curl -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/database"
curl -H "X-Tenant-Id:dt" -X POST "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/meta/collectors/select" -d '{"page_index":1,"page_size": 1}'
curl -H "X-Tenant-Id: dt"  -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/meta/tags" -d '{"filter":{"conditions":[{"field":"device.code","opr":"=","value":{"str_val":"dt:yq_sim1"}}]},"page_index":1,"page_size":1}'

curl -H "X-Tenant-Id: dt"  -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/meta/tags/changes" -d '{"query":{"filter":{"conditions":[{"field":"name","opr":"in","values":{"values":[{"str_val":"col1/str2"}]}}]},"result_type":1}}'
curl -X DELETE "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/database" -d '{"name": "bb"}'

curl -X GET "http://$(kubectl  get pod -o wide | grep lake-resource-0 | awk '{print $6}'):32564/api/v3/instance/lake-mariadb"


# 查看授权服务接口
curl -X GET "http://$(kubectl  get pod -o wide | grep license-service | awk '{print $6}'):8080/service-api/license/quota/feature/tenant?tenantId=dt&productNo=1&featureId=4"

# 根据租户，查询设备
curl -H "X-Tenant-Id:dt" -X POST "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):19592/service-api/rtdb/v2/meta/collectors/select" -d '{"full_filter":{"conditions":[{"field":"id","opr":"=","value":{"str_val":"yq_sim12"}}]}}'

curl -H "X-Tenant-Id:dt" -X DELETE "http://127.0.0.1:19592/service-api/rtdb/v2/meta/tags" -d '{"tag_names":[]}'
 
 
ngrep -W byline -qd any 'service-api/license/quota/statistic/tenant' tcp port 8080


#查看pod ip
kubectl get pods -o wide
 
#网络抓包：
nsenter -t $(docker inspect $(docker ps | grep tsdb-service-0 | grep -av pause | awk '{print $1}') | jq .[0].State.Pid) -n ngrep -x tcp and port 19592
docker inspect $(docker ps | grep tsdb-service-0 | grep -av pause | awk '{print $1}')
 
# 查看消息：
kubectl get po -owide |grep tsdb-service | grep -av migrate| awk '{print $6}' | xargs -i http get http://{}:19592/service-api/rtdb/v2/database
```

## 冗余

```bash
# 通过停止redis，进行切主：
kubectl scale deploy middleware-redis --replicas=0
 
# 查看主从信息
cat /var/local/share/cluster/cluster-info.json
```

## 集群

```bash
# 获取主节点
http GET http://127.0.0.1:8848/nacos/v1/cs/configs group==DEFAULT_GROUP dataId==tsdb-service:default
curl  -X GET  "http://127.0.0.1:8848/nacos/v1/cs/configs?group=DEFAULT_GROUP&dataId=tsdb-service:default"
 
 
 
# 修改主节点
http PUT http://127.0.0.1:19599/inter-api/tsdb-service/deploy/api/v1/services/status X-Tenant-Id:dt id=tsdb-service-0
# 获取注册节点，启动的r2t信息，是否为空
curl -X GET '127.0.0.1:8848/nacos/v1/ns/instance/list?serviceName=DEFAULT_GROUP@@tsdb-service-internal'
```

## docker本地推送

```bash

# 拉取包
docker pull registry.supos.ai/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2-ARM64
 
# 本地打tag
docker tag registry.supos.ai/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2-ARM64 registry:5000/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2
 
# 向本地推送
docker push registry:5000/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2
 
# 提交本地容器
docker commit your-container-id new-image-name
 
#导出镜像
docker save -o tsdb-service.tar registry.supos.ai/jenkins/tsdb-service:5.00.02.00-C-R11-T3
#导入镜像 
docker load -i tsdb-service.tar
```

## Influxdb查询

```bash
#influxdb的8086端口，转发至30000
#http接口，查询influxdb数据；
http://127.0.0.1:30000/query?db=supos_dt&q=SELECT fVal, quality  FROM "iot_test/iot_test_double0" WHERE  time >= 1715069556000000000 AND time < 1715070156000000000 ORDER BY time  DESC  LIMIT 11 OFFSET 0
 
#统计查询
http://127.0.0.1:30000/query?db=supos_dt&ms=10&q=SELECT first(fVal) as value, first(quality) as quality, time FROM "dhb_sim/dhb_simTAG0" WHERE  time >= 1717399598000000000 AND time < 1717400157000000000 GROUP BY time(100ms, 400ms) ORDER BY time  DESC  LIMIT 11 OFFSET 0

curl -G 'http://127.0.0.1:8086/query?db=supos_dt' --data-urlencode 'q=SELECT time, sVal, quality  FROM "/system/Template_2/Instance_3/system/Property_9" ORDER BY time    LIMIT 11 OFFSET 0'

```

## 调试

```bash
#截取dump
nsenter -t $(docker inspect $(docker ps | grep tsdb-service-0 | grep -av pause | awk '{print $1}') | jq .[0].State.Pid) -m -p gdb -ex 'attach 152' -ex 'generate-core-file /data/104_BsRtdService_152'
 
#gdb排查内存
info proc mappings
# dump 出内存段的信息,具体要 dump 的内存段地址，可以借助之前pmap 排查的结果,以及 cat /proc/<pid>/maps 中指示的地址段得出
dump memory /path/dump.bin 0x0011  0x0021   
# 查看内存内容
strings /path/dump.bin | less
 
#系统命令
pmap -X <pid>
 
#配置测试环境的dns
#/etc/resolv.conf
nameserver 10.30.52.254
 
#gdb调试
#忽略停止信号
handle SIGPIPE nostop
handle SIGPIPE ignore
# 进入子进程调试
set follow-fork-mode child
set args  -configfile -nodeport 17020 -dpname Project_001 -dppath /data
set env LD_LIBRARY_PATH=/var/lib/isys
 
 
#jemalloc 启用调试配置
export MALLOC_CONF="tcache:false,junk:true"
#启用dump配置
# tcache:初始化内存； junk:内存填充0X5A；prof_leak:内存分析；prof:性能分析；lg_prof_sample: 采样间隔2^n次方，0不采样；lg_prof_interval: 内存分析间隔，单位为秒；
export MALLOC_CONF="prof_leak:true,prof:true,tcache:false,lg_prof_sample:4,lg_prof_interval:4,junk:true"
 
#查看oom
dmesg -T | grep -E -i -B100 'killed process'
 
#查看磁盘io使用率
iostat -x 1 10
#查看磁盘空间使用率
df -h
#查看目录大小
du -sh
#查看文件描述符
ll /proc/$(pgrep BsAPI)/fd
kill -9 $(pgrep BsMemoryTag)

```


## gerrit

```bash

# 拉取未通过gerrit的代码
# 设置change_id，域名和仓库名
change_id=I7a79195da887b565f5df06698261d154a1906c2b
user_domain=yuanquan@gerrit.supos.ai
reposity_name=i-SYS-icore-config
# 仓库中拉取
change_ref=`ssh -p 29418 ${user_domain} gerrit query  --current-patch-set change:${change_id} | sed 's/\s*//g' |grep  'ref:ref' | cut -c5-`
git fetch ssh://${user_domain}:29418/${reposity_name} ${change_ref} && git cherry-pick FETCH_HEAD;
```

## kafka

```bash

进入 kafka 容器后执行 ↓
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic inner_meta_action --from-beginning

# 查看虚位号数据
# 启动容器，并捕获数据
docker run --entrypoint sh -v /volumes/logs/flink-tm:/tmp   --network=container:$(docker ps | grep -E "oodm-runtime" | grep -av "pause" | awk '{print $1}') -it registry.supos.ai/jenkins/proto-receiver:develop
KAFKA_CONSUMER_GROUP_ID=supngin_stream_model KAFKA_BROKERS=kafka:9092 KAFKA_TOPIC=inner_value_event ./proto-receiver -format=values.tpl | grep 'p21' | tee /tmp/all.txt

# 查看实位号数。启动容器，并捕获数据
docker run --entrypoint sh  --network=host -it registry.supos.ai/jenkins/proto-receiver:develop 
KAFKA_CONSUMER_GROUP_ID=supngin_stream_model KAFKA_BROKERS=172.21.2.203:9092,172.21.2.204:9092,172.21.2.205:9092 KAFKA_TOPIC=rtd_value_event ./proto-receiver -format=values.tpl | grep 'double_code_1' | tee /tmp/all.txt


```
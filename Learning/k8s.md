# K8S��������

## pod����

```bash
# ����tsdb-dproxy
kubectl exec -it ?$(kubectl get po | grep tsdb-dproxy | awk '{print $1}') -- bash

# ����tsdb-service
kubectl exec -it tsdb-service-0 -c=tsdb-service -- bash

# �鿴�ڴ棺
kubectl top pods | sort -k3 -hr

# k8s����&ɾ�����Զ�������
docker pull registry.supos.ai/jenkins/tsdb-service:5.00.01.00-C-M6-T2 && kubectl delete po $(kubectl get po | grep tsdb-service | awk '{print $1}')
```

## �༭��������

```bash
# �޸�tsdb-service
kubectl edit sts tsdb-service

#�޸�tsdb-dproxy
kubectl edit deploy tsdb-dproxy

# ����ip�˿�
kubectl edit svc tsdb-service-dt
#type�е�ClusterIP���ĳ�NodePort
```

## �鿴��־

```bash
# �鿴��־
kubectl logs -f $(kubectl get po | grep tsdb-api | awk '{print $1}')
kubectl logs tsdb-service-0 -c=tsdb-service

# �鿴����
kubectl describe pod my-pod 
kubectl describe pod tsdb-service-0
```

## ����

```bash
# k8s ת��
kubectl port-forward tsdb-service-0 30000:17022 --address=0.0.0.0
# ֱ��ʹ��socatת����k8s�޷�����socatʱʹ��
socat TCP-LISTEN:local_port,fork TCP:kubernetes_node_ip:kubernetes_node_port
socat TCP-LISTEN:30000,fork TCP:$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022
curl -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022/api/ps/cmd?dest=BsRtdService.BsRtdService&cmd=opr%20devinfo"
curl -X GET "http://$(kubectl  get pod -o wide | grep tsdb-service-0 | awk '{print $6}'):17022/api/ps/cmd?dest=BsRtdService.BsRtdService&cmd=tag%20dump%20t3:dhb_col_ae/ae"

#�鿴pod ip
kubectl get pods -o wide

#����ץ����
nsenter -t $(docker inspect $(docker ps | grep tsdb-service-0 | grep -av pause | awk '{print $1}') | jq .[0].State.Pid) -n ngrep -x tcp and port 19592

# �鿴��Ϣ��
kubectl get po -owide |grep tsdb-service | grep -av migrate| awk '{print $6}' | xargs -i http get http://{}:19592/service-api/rtdb/v2/database
```

## ����

```bash
# ͨ��ֹͣredis������������
kubectl scale deploy middleware-redis --replicas=0

# �鿴������Ϣ
cat /var/local/share/cluster/cluster-info.json
```

## ��Ⱥ

```bash
# ��ȡ���ڵ�
http GET http://192.168.12.57:8848/nacos/v1/cs/configs group==DEFAULT_GROUP dataId==tsdb-service:default
curl  -X GET  "http://192.168.237.26:8848/nacos/v1/cs/configs?group=DEFAULT_GROUP&dataId=tsdb-service:default"


# �޸����ڵ�
http PUT http://100.114.209.16:19599/inter-api/tsdb-service/deploy/api/v1/services/status X-Tenant-Id:dt id=tsdb-service-0
```



## docker��������

```bash
# ��ȡ��
docker pull registry.supos.ai/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2-ARM64

# ���ش�tag
docker tag registry.supos.ai/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2-ARM64 registry:5000/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2

# �򱾵�����
docker push registry:5000/jenkins/tsdb-migrate-tools:5.00.01.00-C-R1-T2

# �ύ��������
docker commit your-container-id new-image-name
```

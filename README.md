# hadoop環境部屬

![image](https://github.com/teddyhome123/hadoop/assets/89484381/724d5330-3552-4711-801b-938ad6d96c93)

## 環境說明
- **操作系统**：Ubuntu 22.04
- **軟體**：Apache Hadoop、Redis、Prometheus、Grafana
- **部署方式**：Docker

## Docker部署

在這次練習中皆是使用Docker進行部署，如下圖
![image](https://github.com/teddyhome123/hadoop/assets/89484381/ca4abb99-7f2d-4f66-b91a-303afccdc2c3)


使用Docker-compose部署Hadoop，配置如下：

- 2個DataNode
- 1個ResourceManager
- 2個NodeManager

Hadoop的Docker-compose架構如下：
![image](https://github.com/teddyhome123/hadoop/assets/89484381/79e410e2-9e5c-4010-a3a7-5b53cc87848e)

## Prometheus 監控

在前面設定中，使用jmx_prometheus_javaagent對外映射了30002的port做為prometheus的mertic，
<img width="521" alt="image" src="https://github.com/teddyhome123/hadoop/assets/89484381/79afdd6c-ff6d-481a-87b7-ffdf8fbd4ef4">
<img width="525" alt="image" src="https://github.com/teddyhome123/hadoop/assets/89484381/ac258144-4af3-46e3-ad4a-1724e217fb98">

prometheus的yaml設定如下，對應了前面所說開了30002的port去做metric的收集
![image](https://github.com/teddyhome123/hadoop/assets/89484381/851bc68e-9232-4d6a-95f0-36cf4d230959)

prometheus的web UI成功獲取port:30002的mertic
![image](https://github.com/teddyhome123/hadoop/assets/89484381/fd17ec9c-c3b5-4a94-9c96-05a44496a017)

namenode.yaml透過dockercompose放置到需要監控的service上
![image](https://github.com/teddyhome123/hadoop/assets/89484381/f9cb96b0-e9e4-4995-b282-3417f6362fd1)

## Grafana 數據展示

最後透過grafana去繪製prometheus得到的mertic
![image](https://github.com/teddyhome123/hadoop/assets/89484381/715666c7-d29e-44fa-8848-166c9675e51f)


可以看到從prometheus得到的namenode mertic
<img width="346" alt="image" src="https://github.com/teddyhome123/hadoop/assets/89484381/67203abc-1af2-4468-8be1-9f2494881854">

grafana的部分在這次作業中主要只監控namenode，原因是因為監控datanode和namenode步驟預想上是一樣的，如HDFS，YARN，和MapReduce
目前只取幾個關鍵指標，如CPU使用量，JVM memory使用量、Metaspace、datanode數量等等
<img width="1243" alt="image" src="https://github.com/teddyhome123/hadoop/assets/89484381/eff05cb8-269d-48cc-8263-92476d401594">


最後測試JOB的部分，使用內建的範例去做測試，最後將得到的結果存到redis中當作cache使用。
![image](https://github.com/teddyhome123/hadoop/assets/89484381/25e9bdde-4980-4038-afb9-358ef5d49e66)


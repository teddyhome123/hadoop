# hadoop

![image](https://github.com/teddyhome123/hadoop/assets/89484381/724d5330-3552-4711-801b-938ad6d96c93)


環境：Ubuntu 22.04
軟體：apache hadoop、redis、prometheus、grafana


在這次作業中皆是使用Docker進行部署，如下圖


其中hadoop部分使用docker-compose進行部署，分別開了兩個datanode一個resourcemanager和兩個nodemanager1的container，如下圖


其中使用jmx_prometheus_javaagent對外映射了30002的port做為prometheus的mertic，


prometheus的yaml設定如下，對應了前面所說開了30002的port去做metric的收集

namenode.yaml透過dockercompose放置到需要監控的service上

最後透過grafana去繪製prometheus得到的mertic

grafana的部分在這次作業中主要只監控namenode，原因是因為監控datanode和namenode步驟預想上是一樣的，
目前只取幾個關鍵指標，如CPU使用量，memory使用量、硬碟使用量、datanode數量等等


最後測試JOB的部分，使用內建的範例去做測試，最後將得到的結果存到redis中當作cache使用。

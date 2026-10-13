from pymilvus import connections, utility

# 连接到 Milvus
connections.connect(host="localhost", port="19530")

# 检查版本
print(f"Milvus version: {utility.get_server_version()}")